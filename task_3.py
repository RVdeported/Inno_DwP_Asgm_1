import inspect
from datetime import datetime
from io import StringIO
import sys
from tabulate import tabulate


class decorator_3:
    """
    Decorator class which records various function's properties and records a report into a file.
    Decorator also keeps and can display ranks of the fastest functions passed through it.
    """
    ranks = {}
    count = 0

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # changing stdout stream
        out = StringIO()
        old_stdout = sys.stdout
        sys.stdout = out
        time = datetime.now()
        res = self.func(*args, **kwargs)
        time = datetime.now() - time
        func_out = out.getvalue()

        # count and time
        self.count += 1
        print(f'{self.func.__name__} call {self.count} executed in {time.total_seconds():.6f} sec')

        # printing properties
        self.print_properties(self.func, func_out, args, kwargs, res)

        # recording info for ranks. currently only the best time is recorded
        if not (self.func.__name__ in decorator_3.ranks) or \
                decorator_3.ranks[self.func.__name__] > time.total_seconds():
            decorator_3.ranks.update({self.func.__name__: time.total_seconds()})

        # writing out to file
        sys.stdout = old_stdout
        with open('./out_task_3.txt', 'a') as f:
            print(out.getvalue(), file=f)

        return res

    @staticmethod
    def print_properties(func, func_out, args, kwargs, res):
        # inspection
        print(f'Name:\t\t{func.__name__}')
        print(f'Type:\t\t{type(func)}')

        sig = inspect.signature(func)
        print(f'Sign:\t\t{sig}')

        print(f'Args:\t\tpositional {args}\n\t\tkey=worded {kwargs}')

        print(f'Doc:', end="")
        if not func.__doc__: print("\t\tNone")
        for n in str(func.__doc__).splitlines()[1:]:
            print(f'\t\t{n}')

        code = inspect.getsource(func)
        print("Source:", end="")
        for n in code.splitlines():
            print(f'\t\t{n}')

        print(f'Output:', end="")
        if len(func_out.splitlines()) == 0: print("")
        for n in func_out.splitlines():
            print(f'\t\t{n}')

        print(f'Return:', end="")
        for n in str(res).splitlines():
            print(f'\t\t{n}')

    @staticmethod
    def get_zip_ranks():
        return zip(list(decorator_3.ranks), decorator_3.ranks.values())

    @staticmethod
    def display_ranks():
        decorator_3.ranks = dict(sorted(decorator_3.get_zip_ranks(), key=lambda item: item[1]))
        name = decorator_3.ranks.keys()
        rank = [i for i in range(1, len(decorator_3.ranks)+1)]
        time = ["{:.6f}".format(t) for t in decorator_3.ranks.values()]
        print(time)
        print(tabulate(zip(name, rank, time), headers=['PROGRAM', 'RANK', 'TIME ELAPSED']))


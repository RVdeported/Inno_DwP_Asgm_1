import inspect
from datetime import datetime
from io import StringIO
import sys
from tabulate import tabulate


class decorator_4:
    """
    Decorator class which records various function's properties and records a report into a file.
    Decorator also keeps and can display ranks of the fastest functions passed through it.
    All errors in passed functions are recorded into separate file.
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
        try:
            time = datetime.now()
            res = self.func(*args, **kwargs)
            time = datetime.now() - time
        except Exception as e:
            sys.stdout = old_stdout
            with open('./error_log_task_4.txt', 'a') as f:
                f.writelines(f'{datetime.now()} function {self.func.__name__} encountered error: {e}\n')
            print(f"Function {self.func.__name__} encountered error, see the logs")
            return None

        func_out = out.getvalue()

        # count and time
        self.count += 1
        print(f'{self.func.__name__} call {self.count} executed in {time.total_seconds():.6f} sec')

        # printing properties
        self.print_properties(func_out, args, kwargs, res)

        # recording info for ranks. currently only the best time is recorded
        if not (self.func.__name__ in decorator_4.ranks) or \
                decorator_4.ranks[self.func.__name__] > time.total_seconds():
            decorator_4.ranks.update({self.func.__name__: time.total_seconds()})

        sys.stdout = old_stdout
        with open('./out_task_4.txt', 'a') as f:
            print(out.getvalue(), file=f)

        return res

    def print_properties(self, func_out, args, kwargs, res):
        print(f'Name:\t\t{self.func.__name__}')
        print(f'Type:\t\t{type(self.func)}')

        sig = inspect.signature(self.func)
        print(f'Sign:\t\t{sig}')

        print(f'Args:\t\tpositional {args}\n\t\tkey=worded {kwargs}')

        print(f'Doc:', end="")
        if not self.func.__doc__:
            print("\t\tNone")
        for n in str(self.func.__doc__).splitlines()[1:]:
            print(f'\t\t{n}')

        code = inspect.getsource(self.func)
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
        return zip(list(decorator_4.ranks), decorator_4.ranks.values())

    @staticmethod
    def display_ranks():
        decorator_4.ranks = {k: v for k, v in sorted(decorator_4.get_zip_ranks(), key=lambda item: item[1])}
        name = decorator_4.ranks.keys()
        rank = [i for i in range(1,len(decorator_4.ranks)+1)]
        time = decorator_4.ranks.values()
        print(tabulate(zip(name, rank, time), headers=['PROGRAM', 'RANK', 'TIME ELAPSED']))


def decorator_4_(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1

        out = StringIO()
        old_stdout = sys.stdout
        sys.stdout = out

        time = datetime.now()

        try:
            res = func(*args, **kwargs)
        except Exception as e:
            with open('./error_log_task_4.txt', 'a') as f:
                f.writelines(f'{datetime.now()} function {func.__name__} encountered error: {e}\n')
            sys.stdout = old_stdout
            print(f"Function {func.__name__} encountered error, see the logs")
            return None

        time = datetime.now() - time
        print(f'{func.__name__} call {count} executed in {time.total_seconds():.6f} sec')

        sys.stdout = old_stdout
        with open('./out_task_4.txt', 'a') as f:
            print(out.getvalue(), file=f)

        return res
    return wrapper

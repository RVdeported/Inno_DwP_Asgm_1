import inspect
from datetime import datetime
from io import StringIO
import sys
from tabulate import tabulate

class decorator_3:
    ranks = {}
    count = 0

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        time = datetime.now()

        # changing stdout stream
        out = StringIO()
        old_stdout = sys.stdout
        sys.stdout = out
        res = self.func(*args, **kwargs)
        f_out = out.getvalue()

        # count and time
        self.count += 1
        time = datetime.now() - time
        print(f'{self.func.__name__} call {self.count} executed in {time.total_seconds()} sec')

        # inspection
        print(f'Name:\t{self.func.__name__}')
        print(f'Type:\t{type(self.func)}')
        sig = inspect.signature(self.func)
        print(f'Sign:\t{sig}')
        var = locals()
        print(f'Args:\tpositional {var["args"]}\n\tkey=worded {var["kwargs"]}')
        print(f'Doc:\t{self.func.__doc__}')
        code = inspect.getsourcelines(self.func)
        fl = True
        for n in code[0]:
            if fl:
                fl = False
                print(f'Source:\t{n[:-1]}')
            else:
                print(f'\t{n[:-1]}')
        print(f'Output:\t{f_out}')

        # recording info for ranks. currently only the best time is recorded
        if not (self.func.__name__ in decorator_3.ranks) or \
                decorator_3.ranks[self.func.__name__] > time.total_seconds():
            decorator_3.ranks.update({self.func.__name__: time.total_seconds()})

        sys.stdout = old_stdout
        with open('./out_task_3.txt', 'a') as f:
            print(out.getvalue(), file=f)

        return res

    @staticmethod
    def get_zip_ranks():
        return zip(list(decorator_3.ranks), decorator_3.ranks.values())

    @staticmethod
    def display_ranks():
        decorator_3.ranks = {k: v for k, v in sorted(decorator_3.get_zip_ranks(), key=lambda item: item[1])}
        name = decorator_3.ranks.keys()
        rank = [i for i in range(1,len(decorator_3.ranks)+1)]
        time = decorator_3.ranks.values()
        print(tabulate(zip(name, rank, time), headers=['PROGRAM', 'RANK', 'TIME ELAPSED']))

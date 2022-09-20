from datetime import datetime
from io import StringIO
import sys
from traceback import format_exc

from task_3 import display_ranks, print_properties


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
                f.writelines(f'{datetime.now()} function {self.func.__name__} encountered error {e}:\n{format_exc()}')
            print(f"Function {self.func.__name__} encountered error {e}, see the logs for details")
            return None

        func_out = out.getvalue()

        # count and time
        self.count += 1
        print(f'{self.func.__name__} call {self.count} executed in {time.total_seconds():.6f} sec')

        # printing properties
        print_properties(self.func, func_out, args, kwargs, res)

        # recording info for ranks. currently only the best time is recorded
        if not (self.func.__name__ in decorator_4.ranks) or \
                decorator_4.ranks[self.func.__name__] > time.total_seconds():
            decorator_4.ranks.update({self.func.__name__: time.total_seconds()})

        sys.stdout = old_stdout
        with open('./out_task_4.txt', 'a') as f:
            print(out.getvalue(), file=f)

        return res

    @staticmethod
    def display_ranks():
        display_ranks(decorator_4)


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
                f.writelines(f'{datetime.now()} function {func.__name__} encountered error {e}:\n{format_exc()}')
            sys.stdout = old_stdout
            print(f"Function {func.__name__} encountered error {e}, see the logs for details")
            return None

        time = datetime.now() - time
        print(f'{func.__name__} call {count} executed in {time.total_seconds():.6f} sec')

        decorator_3.print_properties(func, out, args, kwargs, res)

        sys.stdout = old_stdout
        with open('./out_task_4.txt', 'a') as f:
            print(out.getvalue(), file=f)

        return res
    return wrapper

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:27:43 2022

@author: Roman Vetrin
"""

import inspect
from datetime import datetime
from io import StringIO
import sys


def decorator_2(func):
    """
    Prints various properties of the function including console out stream.
    """
    count = 0

    def wrapper(*args, **kwargs):
        # changing stdout stream while func executes
        out = StringIO()
        old_stdout = sys.stdout
        sys.stdout = out
        time = datetime.now()
        res = func(*args, **kwargs)
        time = datetime.now() - time
        out = out.getvalue()
        sys.stdout = old_stdout

        # count and time
        nonlocal count
        count += 1
        print(f'{func.__name__} call {count} executed in {time.total_seconds():.6f} sec')

        # printing properties
        print_properties(func, out, args, kwargs, res)

        return res

    def print_properties(func, out, args, kwargs, res):
        # inspection
        print(f'Name:\t\t{func.__name__}')
        print(f'Type:\t\t{type(func)}')

        sig = inspect.signature(func)
        print(f'Sign:\t\t{sig}')

        print(f'Args:\t\tpositional {args}\n\t\tkey=worded {kwargs}')

        print(f'Doc:', end="")
        if not func.__doc__:
            print("\t\tNone")
        for n in str(func.__doc__).splitlines()[1:]:
            print(f'\t\t{n}')

        code = inspect.getsource(func)
        print("Source:", end="")
        for n in code.splitlines():
            print(f'\t\t{n}')

        print(f'Output:', end="")
        for n in out.splitlines():
            print(f'\t\t{n}')

        print(f'Return:', end="")
        for n in str(res).splitlines():
            print(f'\t\t{n}')

    return wrapper
    
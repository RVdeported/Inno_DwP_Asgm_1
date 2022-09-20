#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:27:43 2022

@author: Roman Vetrin
"""

from task_3 import decorator_3

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
        decorator_3.print_properties(func, out, args, kwargs, res)

        return res

    return wrapper
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:27:43 2022

@author: thornail
"""

import inspect
from datetime import datetime

from io import StringIO
import sys


def decorator_2(func):
    count = 0
    name = '@decorator_2'

    def wrapper(*args, **kwargs):
        time = datetime.now()

        # changing stdout stream while func executes
        out = StringIO()
        old_stdout = sys.stdout
        sys.stdout = out
        res = func(*args, **kwargs)
        out = out.getvalue()
        sys.stdout = old_stdout

        # count and time
        nonlocal count
        count += 1
        time = datetime.now() - time
        print(f'{func.__name__} call {count} executed in {time.total_seconds()} sec')
        
        # inspection
        print(f'Name:\t{func.__name__}')
        print(f'Type:\t{type(func)}')
        sig = inspect.signature(func)
        print(f'Sign:\t{sig}')
        var = locals()
        print(f'Args:\tpositional {var["args"]}\n\tkey=worded {var["kwargs"]}')
        print(f'Doc:\t{func.__doc__}')
        code = inspect.getsourcelines(func)
        nonlocal name
        print(f'Source:\t{name}')
        for n in code[0]:
            print(f'\t{n[:-1]}')
        print(f'Output:\t{out}')

        return res
    return wrapper
    
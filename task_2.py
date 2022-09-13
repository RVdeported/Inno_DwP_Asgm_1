#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:27:43 2022

@author: thornail
"""

import inspect
from datetime import datetime

def decorator_2(func):
    count=0
    def wrapper(*args, **kwargs):
        # count and time
        nonlocal count
        count +=1
        time = datetime.now()
        out=func(args, kwargs)
        time = datetime.now() - time
        print(f'{func.__name__} call {count} executed in {time.total_seconds()} sec')
        
        # inspection
        print(f'Name:\t{func.__name__}')
        print(f'Type:\t{type(func)}')
        sig=inspect.signature(func)
        print(f'Sign:\t{sig}')
        var=locals()
        print(f'Args:\tpositional {var["args"]}\n\tkey=worded {var["kwargs"]}')
        print(f'Doc:\t{func.__doc__}')
        code=inspect.getsourcelines(func)
        print(f'Source:')
        for n in code[0]:
            print(f'\t{n[:-1]}')

        return out
    return wrapper
    
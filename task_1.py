#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:11:41 2022

@author: Roman Vetrin
"""


from datetime import datetime


def decorator_1(func):
    """
    Prints count of function's calls and execution time
    """
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        time = datetime.now()
        out = func(*args, **kwargs)
        time = datetime.now() - time
        print(f'{func.__name__} call {count} executed in {time.total_seconds()} sec')
        return out
    return wrapper
    
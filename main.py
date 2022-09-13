#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:14:23 2022

@author: thornail
"""

import random
from task_1 import decorator_1

@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
        
@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i

if __name__ == "__main__": 
    func()
    funx()
    func()
    funx()
    func()

#=========================================================

from task_2 import decorator_2

@decorator_2
def funh(bar1, bar2=""):
    """
    This function does something useful 
    :param bar1: description
    :param bar2: description
    """ 
    print("some\nmultiline\noutput")

if __name__ == "__main__": 
    funh(None, bar2="")

#============================================================

from task_3 import decorator_3

@decorator_3
def func():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)

@decorator_3
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i

@decorator_3
def funh(bar1, bar2=""):
    """
    This function does something useful
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")

if __name__=='__main__':
    func()
    funx(4, 5)
    funx(400, 500)
    funh("test")

    decorator_3.display_ranks()


#====================================================================

from task_4 import decorator_4, decorator_4_


@decorator_4
def func():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)

@decorator_4
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i

@decorator_4
def funh(x1, x2=5):
    return x1/x2

@decorator_4_
def funh_1(x1, x2=5):
    return x1/x2

if __name__=='__main__':
    funh(3, 6)
    funh(5, 0)
    funh_1(3, 6)
    funh_1(5, 0)

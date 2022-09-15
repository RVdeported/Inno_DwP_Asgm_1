#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:14:23 2022

@author: Roman Vetrin, MS_DS_01
"""

import random
from task_1 import decorator_1
import numpy as np


@decorator_1
def quadratic_eq(x2, x1, x0):
    """
    Solves quadratic equation of type ax^2 + bx + c = 0
    :param x2: a coefficient
    :param x1: b coefficient
    :param x0: c coefficient
    :return: a list of solutions or False in case there is no real solution
    """
    print("Start of quadratic function")
    x1, x0 = x1/(2*x2), x0/(2*x2)
    D = x1**2 - 2*x0
    if D < 0:
        print("There is no real solutions")
        return False

    return [-x1+np.sqrt(D), -x1-np.sqrt(D)]


@decorator_1
def derivative(funcs: list, args: list, delta: float = 0.000001) -> list:
    """
    Returns list of derivatives of the one-argument funcs at a given arguments args
    :param funcs: list of functions for derivative calculation
    :param args: list of arguments for calculation
    :param delta: required precision
    :return: a list of derivative values
    """
    return list(map(lambda f, x: (f(x + delta) - f(x)) / delta, funcs, args))


@decorator_1
def matrix_p_norm(matrix: list, p: float = 2.0) -> float:
    """
    Returns entry-wise norm of matrix in p-th degree
    :param matrix: 2D list of lists, np.ndarray or other iterable container
    :param p: p-value, degree of norm
    :return: a float norm of the matrix
    """
    return np.power(np.sum([list(map(lambda x: x**p, n)) for n in matrix]), 1/p)  # so nobody would ever maintain it


if __name__ == "__main__":
    quadratic_eq(1, 5, 2)
    matrix_p_norm([[1, 1, 1],
                   [1, 1, 2]])
    quadratic_eq(1, 2, 2)
    matrix_p_norm([[1, 1, 1],
                   [1, 1, 2]],
                  p=2.5)
    quadratic_eq(1, 2, 2)
    derivative([lambda x:x**2, lambda x:x**3 + 3*x**2], [3, 6])

#=========================================================

from task_2 import decorator_2


@decorator_2
def pascal(n: int, display:bool =False):
    """
    Function returns list of int lists in accordance with pascal triangle
    :param n: number of pascal triangle levels required
    :param display: is it required to display the triangle?
    """
    out = [[1]]
    for t in range(1, n):
        out += [[f+i for f, i in zip([0]+out[-1], out[-1]+[0])]]

    

    if display:
        for i, t in enumerate(out):
            print(" "*(n-i) + str(t))

    return out

if __name__ == "__main__": 
    pascal(5, display=True)

#============================================================

from task_3 import decorator_3


@decorator_3
def quadratic_eq(x2, x1, x0):
    """
    Solves quadratic equation of type ax^2 + bx + c = 0
    :param x2: a coefficient
    :param x1: b coefficient
    :param x0: c coefficient
    :return: a list of solutions or False in case there is no real solution
    """
    print("Start of quadratic function")
    x1, x0 = x1/(2*x2), x0/(2*x2)
    D = x1**2 - 2*x0
    if D < 0:
        print("There is no real solutions")
        return False

    return [-x1+np.sqrt(D), -x1-np.sqrt(D)]


@decorator_3
def pascal(n: int, display: bool = False):
    """
    Function returns list of int lists in accordance with pascal triangle
    :param n: number of pascal triangle levels required
    :param display: is it required to display the triangle?
    """
    out = [[1]]
    for t in range(1, n):
        out += [[f+i for f, i in zip([0]+out[-1], out[-1]+[0])]]



    if display:
        for i, t in enumerate(out):
            print(" "*(n-i) + str(t))

    return out


@decorator_3
def matrix_p_norm(matrix: list, p: float = 2.0) -> float:
    """
    Returns entry-wise norm of matrix in p-th degree
    :param matrix: 2D list of lists, np.ndarray or other iterable container
    :param p: p-value, degree of norm
    :return: a float norm of the matrix
    """
    return np.power(np.sum([list(map(lambda x: x**p, n)) for n in matrix]), 1/p)  # so nobody would ever maintain it


if __name__ == '__main__':
    quadratic_eq(1, 5, 2)
    pascal(15, True)
    pascal(25, True)
    matrix_p_norm(np.random.random((5, 5))*10)

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
def pascal(n: int, display: bool = False):
    """
    Function returns list of int lists in accordance with pascal triangle
    :param n: number of pascal triangle levels required
    :param display: is it required to display the triangle?
    """
    out = [[1]]
    for t in range(1, n):
        out += [[f+i for f, i in zip([0]+out[-1], out[-1]+[0])]]



    if display:
        for i, t in enumerate(out):
            print(" "*(n-i) + str(t))

    return out


@decorator_4
def div(x1, x2=5):
    return x1/x2


@decorator_4_
def div_(x1, x2=5):
    return x1/x2


@decorator_4_
def matrix_p_norm(matrix: list, p: float = 2.0) -> float:
    """
    Returns entry-wise norm of matrix in p-th degree
    :param matrix: 2D list of lists, np.ndarray or other iterable container
    :param p: p-value, degree of norm
    :return: a float norm of the matrix
    """
    return np.power(np.sum([list(map(lambda x: x**p, n)) for n in matrix]), 1/p)  # so nobody would ever maintain it


if __name__ == '__main__':
    div(3, 6)
    div(5, 0)  # class decorator
    div_(5, 0)  # function decorator
    pascal(7)
    matrix_p_norm(np.random.random((5, 5))*10)

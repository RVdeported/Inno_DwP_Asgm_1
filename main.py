#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:14:23 2022

@author: Roman Vetrin, MS_DS_01

Please note, that @decorator is used only in first task for demonstration of my understanding of a concept.
In the rest examples I use func = decorator(func) to avoid coping the function each time I want to change decorator.
"""


#================= KEY IMPORTS AND FUNCTIONS ======================================

from task_1 import decorator_1
import numpy as np


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


def quadratic_eq(x2: float, x1: float, x0: float) -> list:
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
        print("There are no real solutions")
        return False

    return [-x1+np.sqrt(D), -x1-np.sqrt(D)]


def matrix_p_norm(matrix: list, p: float = 2.0) -> float:
    """
    Returns entry-wise norm of matrix in p-th degree
    :param matrix: 2D list of lists, np.ndarray or other iterable container
    :param p: p-value, degree of norm
    :return: a float norm of the matrix
    """
    return np.power(np.sum([list(map(lambda x: x**p, n)) for n in matrix]), 1/p)  # so nobody would ever maintain it


def pascal(n: int, display: bool = False) -> list:
    """
    Function returns list of int lists in accordance with pascal triangle
    :param n: number of pascal triangle levels required
    :param display: is it required to display the triangle?
    :return: a list of int containing layers of pascal triangle
    """
    out = [[1]]
    print("Starting a Pascal triangle\nExpect triangle to appear\nnow")
    for _ in range(1, n):
        out += [[f+i for f, i in zip([0]+out[-1], out[-1]+[0])]]

    if display:
        for i, t in enumerate(out):
            print(" "*(n-i) + str(t))

    return out


def div(x1: float, x2: float = 5) -> float:
    return x1/x2

# ================= TASK 1 ======================================

from task_1 import decorator_1  # I repeated import of the first decorator for consistency with other tasks


if __name__ == "__main__":
    # assignment of decorators
    quadratic_eq_1 = decorator_1(quadratic_eq)
    matrix_p_norm_1 = decorator_1(matrix_p_norm)

    print("\nTesting of task_1\n")

    quadratic_eq_1(1, 5, 2)
    matrix_p_norm_1([[1, 1, 1],
                    [1, 1, 2]])
    quadratic_eq_1(1, 2, 2)
    matrix_p_norm_1([[1, 1, 1],
                    [1, 1, 2]],
                    p=2.5)
    quadratic_eq_1(1, 2, 2)
    derivative([lambda x:x**2, lambda x:x**3 + 3*x**2], [3, 6])
    print("\nTask_1 test complete\n")

# ================= TASK 2 ======================================

from task_2 import decorator_2

if __name__ == "__main__":
    pascal_2 = decorator_2(pascal)
    print("Testing of task_2\n")
    pascal_2(5, display=True)
    print("\nTask_2 test complete\n")

# ================= TASK 3 ======================================

from task_3 import decorator_3

if __name__ == '__main__':
    # assignment of decorators
    quadratic_eq_3 = decorator_3(quadratic_eq)
    pascal_3 = decorator_3(pascal)
    matrix_p_norm_3 = decorator_3(matrix_p_norm)

    print("Testing of task_3\n")

    quadratic_eq_3(1, 5, 2)
    pascal_3(15, True)
    pascal_3(25, True)
    matrix_p_norm_3(np.random.random((5, 5))*10)

    decorator_3.display_ranks()
    print("\nTask_3 test complete\n")


# ================= TASK 4 ======================================

from task_4 import decorator_4, decorator_4_


if __name__ == '__main__':
    # assignment of decorators
    pascal_4 = decorator_4(pascal)
    matrix_p_norm_4 = decorator_4(matrix_p_norm)
    div_4 = decorator_4(div)
    div_4_ = decorator_4_(div)

    print("Testing of task_4\n")

    pascal_4(9)
    div_4(3, 6)
    div_4(5, 0)  # class decorator
    div_4_(5, 0)  # function decorator
    pascal_4(7)
    matrix_p_norm_4(np.random.random((5, 5))*10)

    print("\nTask_3 test complete\n")

# Harbin Institute of Technology, Shenzhen
# MATH3010
# Instructor: Dr. XU Gangyan

from scipy import optimize
import numpy as np


def homework_1_2():
    c = np.array([700, 600, 600, 300, 350, 250, 900, 800, 700])
    A = np.array([[-700, -600, -600, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, -300, -350, -250, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, -900, -800, -700],
                  [1, 0, 0, 1, 0, 0, 1, 0, 0],
                  [0, 1, 0, 0, 1, 0, 0, 1, 0],
                  [0, 0, 1, 0, 0, 1, 0, 0, 1]])
    b = np.array([-130000, -40000, -250000, 200, 400, 600])

    result = optimize.linprog(-c, A_ub=A, b_ub=b)
    print(result)


def homework_1_3_1():
    x0_bound = (0, None)
    x1_bound = (0, None)

    c = np.array([1, 2])
    A = np.array([[1, 1], [0, 1]])
    b = np.array([2, 1])

    result = optimize.linprog(-c, A_ub=A, b_ub=b)
    print(result)


def homework_1_3_2():
    x0_bound = (0, None)
    x1_bound = (0, None)

    c = np.array([2, -10])
    A = np.array([[1, -1], [1, -5]])
    b = np.array([0, -5])

    result = optimize.linprog(c, A_ub=-A, b_ub=-b, bounds=(x0_bound, x1_bound))
    print(result)


def homework_2_1_1():
    c = np.array([1, 1, 1])
    A = np.array([[-1, 0, -2], [2, -3, 1], [2, -5, 6]])
    b = np.array([5, 3, 5])

    result = optimize.linprog(-c, A_ub=A, b_ub=b)
    print(result)


def homework_2_1_2():
    c = np.array([-1, -3, -3, 0, 0, 0])
    A = np.array([[3, 1, 2, 0, 1, 0], [1, 0, 1, 0, 2, 1], [1, 0, 2, 1, 2, 0]])
    b = np.array([5, 2, 6])

    result = optimize.linprog(c, A_eq=A, b_eq=b)
    print(result)


def homework_2_2_1():
    c = np.array([1, -1, 1])
    A = np.array([[1, 2, 3], [4, 5, -6]])
    b = np.array([6, 6])

    result = optimize.linprog(c, A_eq=A, b_eq=b)
    print(result)


def homework_2_2_2():
    c = np.array([1, 1])
    A = np.array([[1, 1], [1, -1]])
    b = np.array([1, 0])

    result = optimize.linprog(-c, A_ub=-A, b_ub=-b)
    print(result)






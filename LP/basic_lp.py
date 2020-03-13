# Harbin Institute of Technology, Shenzhen
# Dr. XU Gangyan
# MATH3010 Example 1.5

from scipy import optimize
import numpy as np

x0_bound = (0, None)
x1_bound = (0, None)

c = np.array([3, 4])
A = np.array([[1, 2], [3, 2], [0, 1]])
b = np.array([6, 12, 2])

result = optimize.linprog(-c, A_ub=A, b_ub=b, bounds=(x0_bound, x1_bound))
print(result)
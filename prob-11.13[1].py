#prob 11.12
#author: Rahul Shridhar

import numpy as np
import _linalg, _linalg4

A = np.array([
    [-8, 1, -2],
    [2, -6, -1],
    [-3, -1, 7],
])

b = np.array([
    -20,
    -38,
    -34,
])

print("A = \n{}".format(np.array(A)))
print("b = {}\n".format(np.array(b)))

x = _linalg4.gausseidel(A, b, es100=0.05)
print("\n(using gauss-seidel without relaxation)\nx = {}".format(x))

print('--------------------')

x = _linalg4.gausseidel(A, b, es100=0.05, lamb=1.2)
print("\n(using gauss-seidel with relaxation)\nx = {}".format(x))

print('--------------------')

x = _linalg.gauss(A, b)
print("\n(using gauss-elim)\nx = {}".format(x))
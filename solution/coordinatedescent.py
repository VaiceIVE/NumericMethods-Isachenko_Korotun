import numpy as np
from math import exp
from typing import Callable, List

import numpy.linalg.linalg
import scipy.optimize
from scipy.optimize import minimize
import sympy as sp

x, y = sp.symbols('x y')
f = 30 - (x - 2) * sp.exp(-x + 2) - (y - 1) * sp.exp(-y + 1)


def funcinx(func, x, vars):
    for i, var in enumerate(vars):
        func = sp.N(func.subs(var, x[i]))
    return float(func)



def gradinx(grads, x, vars):
    reslist = list()
    for i, grad in enumerate(grads):
        for j, var in enumerate(vars):
            grad = sp.N(grad.subs(var, x[j]))
        reslist.append(float(grad))
    return np.array(reslist)


def coordinate_descent(func,
                       x0: List[float],
                       eps: float = 0.0001,):
    k = 0
    x_points = [x0]
    grad = list()
    vars = func.free_symbols
    for var in vars:
        grad.append(sp.diff(func, var))
    grad = np.array(grad)
    print(gradinx(grad, x_points[k], vars))
    norm = numpy.linalg.norm(gradinx(grad, x_points[k], vars))
    print(norm)
    print("Start")
    while norm > eps:
        sk = -gradinx(grad, x_points[k], vars)/norm
        print("SK = ", sk)
        def functomin(lamb):
            nonlocal sk
            subfunc = func
            for i, var in enumerate(vars):
                subfunc = subfunc.subs(var, float(x_points[k][i] + lamb * sk[i]))
            return np.array(subfunc)

        res = scipy.optimize.minimize(functomin, 1, method='COBYLA')

        print('lambda', res)
        x_points.append(x_points[k] + res.x[0] * sk)
        norm = numpy.linalg.linalg.norm(gradinx(grad, x_points[k], list(vars)))
        k += 1
    return x_points[len(x_points) - 1]

print(coordinate_descent(f, [7, 7]))
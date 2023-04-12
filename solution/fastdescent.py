import numpy as np
from math import exp
from scipy.optimize import minimize
from typing import Callable, List

from dih import opt as find_min

def odm(fnc, x0, h):
    res = minimize(fnc, x0, method='nelder-mead',
                   options={'xatol': h, 'disp': False})
    return res.x[0]
def f(x, y, A=30, a=2, b=1):
    return A - (x - a) * exp(-x + a) - (y - b) * exp(-y + b)

def dist(x1, x0):
    return sum(map(lambda k: k**2, [i - j for i, j in list(zip(x1, x0))]))**0.5

def summary(A, a, b, starting_point, eps, n_iters, opt, opt_value):
    return f"Оптимизация целевой функции {A} - (x - {a}) * exp(-x + {a}) - (y - {b}) * exp(-y + {b})\nпроизводилась из точки {starting_point} с заданной точностью {eps}.\nБыло произведено {n_iters} итераций, найдено оптимальное решение {[round(i, 2) for i in opt]} и\nоптимальное значение целевой функции {round(opt_value, 2)}"

start_point = [150, 150]
x0 = start_point
eps = 0.001

def coordinate_descent(func: Callable[..., float],
                       x0: List[float],
                       odm: Callable[[Callable[[float], float], float, float], float],
                       eps: float = 0.0001,
                       step_crushing_ratio: float = 0.99):
    x_points = [x0]
    N = len(x0)
    k = 1
    h = np.array([1.]*N)

    while h[0] > eps:
        x_points.append([0] * N)
        if np.linalg.norm(np.array(x_points[k]) - np.array(x_points[k - 1])) <= eps:
            break






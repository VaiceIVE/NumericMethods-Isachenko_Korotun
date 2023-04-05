from math import exp

# возвращаемое значение opt (одномерная оптимизация) = точка минимума
# аргументы - функция f, границы a, b, точность эпсилон (e)
from dih import opt as find_min

# Целевая функция
def f(x, y, A=30, a=2, b=1):
    return A - (x - a) * exp(-x + a) - (y - b) * exp(-y + b)

# расстояние между текущей и предыдущей точками (для условия выхода из алгоритма)
def dist(x1, x0):
    return sum(map(lambda k: k**2, [i - j for i, j in list(zip(x1, x0))]))**0.5

# просто для вывода всей инфы (необязательно наверное)
def summary(A, a, b, starting_point, eps, n_iters, opt, opt_value):
    return f"Оптимизация целевой функции {A} - (x - {a}) * exp(-x + {a}) - (y - {b}) * exp(-y + {b})\nпроизводилась из точки {starting_point} с заданной точностью {eps}.\nБыло произведено {n_iters} итераций, найдено оптимальное решение {[round(i, 2) for i in opt]} и\nоптимальное значение целевой функции {round(opt_value, 2)}"

start_point = [150, 150]
x0 = start_point
eps = 0.001

# первый шаг алгоритма
l = find_min(lambda lmbd: f(x0[0] + lmbd, x0[1]), eps=eps)

x0 = [x0[0] + l, x0[1]]

# второй шаг алгоритма
l = find_min(lambda lmbd: f(x0[0], x0[1] + lmbd), eps=eps)

# x1 - текущая точка, x0 - полученная на предудыщем шаге
x1 = [x0[0], x0[1] + l]

# same
iters = 0
while (dist(x1, x0) > eps):
    iters += 1
    for i in range(2):
        l = find_min(lambda lmbd: f(
            x0[0] + lmbd * ((i + 1) % 2),
            x0[1] + lmbd * (i % 2),
        ),
        eps=eps)
        x0 = x1.copy()
        x1 = [x1[0] + l * ((i + 1) % 2), x1[1] + (l * (i % 2))]

    print(f(x1[0], x1[1]), x1, x0, dist(x1, x0))

print(summary(30, 2, 1, start_point, eps, iters, x1, f(x1[0], x1[1])))

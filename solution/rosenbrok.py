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

# нормализация вектора
def normalize(x):
    return [x[0] / (x[0]**2 + x[1]**2)**0.5, x[1] / (x[0]**2 + x[1]**2)**0.5]

# ортогонализация грамма-шмидта; принимает список исходной сис-мы векторов и номер вектора, с которого начинается процесс (индексация с нуля)
def get_ortonormal(x0, x1):
    y0 = x0.copy()
    l = (x1[0] * y0[0] + x1[1] * y0[1]) / (y0[0]**2 + y0[1]**2)
    y1 = [0, 0]
    y1[0] = x1[0] - l * y0[0]
    y1[1] = x1[1] - l * y0[1]

    return normalize([y1[0], y1[1]])

# просто для вывода всей инфы (необязательно наверное)
def summary(A, a, b, starting_point, eps, n_iters, opt, opt_value):
    return f"Оптимизация целевой функции {A} - (x - {a}) * exp(-x + {a}) - (y - {b}) * exp(-y + {b})\nпроизводилась из точки {starting_point} с заданной точностью {eps}.\nБыло произведено {n_iters} итераций, найдено оптимальное решение {[round(i, 2) for i in opt]} и\nоптимальное значение целевой функции {round(opt_value, 2)}"

start_point = [-50, -50]
x0 = start_point
eps = 0.001
dir0 = [1, 0]
dir1 = [0, 1]

# первый шаг покоординатного поиска
l = find_min(lambda lmbd: f(x0[0] + lmbd * dir0[0], x0[1] + lmbd * dir0[1]), eps=eps)

x0 = [x0[0] + l * dir0[0], x0[1] + l * dir0[1]]

# второй шаг покоординатного поиска
l = find_min(lambda lmbd: f(x0[0] + lmbd * dir1[0], x0[1] + lmbd * dir1[1]), eps=eps)

# x1 - текущая точка, x0 - полученная на предудыщем шаге
x1 = [x0[0] + l * dir1[0], x0[1] + l * dir1[1]]

# осуществлена первая итерация
iters = 1

while (dist(x1, x0) > eps):
    print(f(x1[0], x1[1]), dist(x1, x0), x0, x1, dir1, dir0)
    x_f = x0.copy()
    iters += 1
    for i in range(2):
        l = find_min(lambda lmbd: f(
            x1[0] + lmbd * (dir0[0] * ((i + 1) % 2) + dir1[0] * (i % 2)),
            x1[1] + lmbd * (dir0[1] * ((i + 1) % 2) + dir1[1] * (i % 2)),
        ),
        eps=eps)
        x0 = x1.copy()
        x1 = [x1[0] + l * (dir0[0] * ((i + 1) % 2) + dir1[0] * (i % 2)), x1[1] + l * (dir0[1] * ((i + 1) % 2) + dir1[1] * (i % 2))]

    dir0 = normalize([x1[0] - x_f[0], x1[1] - x_f[1]])
    dir1 = get_ortonormal(dir0, x_f)
    # print(dir0, dir1)

    # print(f(x1[0], x1[1]), x1, x0, dist(x1, x0))

print(summary(30, 2, 1, start_point, eps, iters, x1, f(x1[0], x1[1])))

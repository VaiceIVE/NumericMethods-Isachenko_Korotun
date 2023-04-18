from math import exp

# Целевая функция
def f(x, y, A=30, a=2, b=1):
    return A - (x - a) * exp(-x + a) - (y - b) * exp(-y + b)

# просто для вывода всей инфы (необязательно наверное)
def summary(A, a, b, starting_point, eps, n_iters, opt, opt_value):
    return f"Оптимизация целевой функции {A} - (x - {a}) * exp(-x + {a}) - (y - {b}) * exp(-y + {b})\nпроизводилась из точки {starting_point} с заданной точностью {eps}.\nБыло произведено {n_iters} итераций, найдено оптимальное решение {[round(i, 2) for i in opt]} и\nоптимальное значение целевой функции {round(opt_value, 2)}"

start_point = [30, 25]
x = start_point
eps = 0.001
l0 = 5
l1 = 5
iters = 0

while (l0 > eps or l1 > eps):
    iters += 1

    for i in range(2):
        pos_step = [x[0] + l0 * ((i + 1) % 2), x[1] + l1 * (i % 2)]

        neg_step = [x[0] - l0 * ((i + 1) % 2), x[1] - l1 * (i % 2)]
        
        if f(x[0], x[1]) < f(*pos_step) and f(x[0], x[1]) < f(*neg_step):
            if ((i + 1) % 2):
                l0 /= 2
            else:
                l1 /= 2
            
            continue

        x = pos_step if f(*pos_step) < f(*neg_step) else neg_step

    print(f(x[0], x[1]), x, l0, l1)

print(summary(30, 2, 1, start_point, eps, iters, x, f(x[0], x[1])))

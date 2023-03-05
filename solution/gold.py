def f(x):
    return (x + 5 )**4

a, b = sorted([-6, 2])

eps = 0.001
t = 0.618

while b - a > eps:
    L = b - a

    x1 = a + L * t
    x2 = b - L * t

    f1 = f(x1)
    f2 = f(x2)

    if f1 > f2:
        b = x1
        f1 = f2
        x1 = x2
        L = b - a
        x2 = b - L * t
        f2 = f(x2)
    else:
        a = x2
        f2 = f1
        x2 = x1
        L = b - a
        x1 = a + L * t
        f1 = f(x1)

print("Минимум функции f={} достигается в точке x={}".format(min(f1, f2), x1 if f1 < f2 else x2))

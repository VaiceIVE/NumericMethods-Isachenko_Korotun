def f(x):
    return (x + 5 )**4

a, b = sorted([-6, 2])

eps = 0.001

while b - a > 2*eps:
    x = (a + b) / 2

    x1 = x - eps / 2
    x2 = x + eps / 2
    f1 = f(x1)
    f2 = f(x2)

    if f1 > f2:
        a = x1
    else:
        b = x2

print("Минимум функции f={} достигается в точке x={}".format(f((a + b) / 2), (a + b) / 2))

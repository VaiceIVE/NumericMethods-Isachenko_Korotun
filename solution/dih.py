def opt(f, a=-5, b=5, eps=0.01):
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

    return (a + b) / 2

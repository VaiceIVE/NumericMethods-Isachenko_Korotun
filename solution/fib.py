def f(x):
    return (x + 5 )**4

def fib(n):
    result = [1, 1]
    for i in range(2, n):
        result.append(result[i-1] + result[i-2])
    return result

a, b = sorted([-6, 2])

n = 15
while n > 2:
    F = fib(n)
    L = b - a

    x1 = a + F[n-2] * L / F[n-1]
    x2 = b - F[n-2] * L / F[n-1]

    f1 = f(x1)
    f2 = f(x2)

    if f1 > f2:
        b = x1
        f1 = f2
        x1 = x2
        L = b - a
        x2 = b - F[n-3] * L / F[n-2]
        f2 = f(x2)
    else:
        a = x2
        f2 = f1
        x2 = x1
        L = b - a
        x1 = a + F[n-3] * L / F[n-2]
        f1 = f(x1)
    n -= 1

print("Минимум функции f={} достигается в точке x={}".format(min(f1, f2), x1 if f1 < f2 else x2))

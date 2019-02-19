x = lambda y : y * 7

print(x(10))


x = lambda a, b : (a * 10) + (b * 20)

print(x(10,20))


def func(n):
    return lambda a: a*n


doubleValue = func(2)
tripleValue = func(3)

print(doubleValue(10))
print(tripleValue(10))

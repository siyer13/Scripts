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


def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
C = map(celsius, F)

print(list(F))
print(list(C))

import string

vowels = ['a', 'e', 'i', 'o', 'u']

alphabets = list(string.ascii_lowercase)


output = filter(lambda vowel : (vowel in vowels), alphabets)

print(list(output))

countries = ['india', 'america', 'kenya', 'sweeden', 'singapore', 'peru']

cap_country = list(map(lambda country : country.upper(), countries))

print(cap_country)

from functools import reduce

number = [1,2,3,4,5]

final_number = reduce(lambda num1, num2 : num1 + num2 , number)
print(final_number)

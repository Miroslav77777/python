import math

X = int(input('Введите число '))

def is_in(x):
    return -15<x<=12 or 14<x<17 or 19<x<math.inf

print(is_in(X))
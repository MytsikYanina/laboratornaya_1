# -*- coding: cp1251 -*-
a, b, c = int(input()), int(input()), int(input())
if ((a + b) < c) or ((a + c) < b) or ((c + b) < a) or (a <= 0 or b <= 0 or c <= 0):
    print("Недопустимые значения длин сторон")
else:
    if a == b == c:
        print("Треугольник равносторонний")
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print("Площадь треугольника равна:", S)

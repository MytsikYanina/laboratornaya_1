# -*- coding: cp1251 -*-

a, b, c = int(input()), int(input()), int(input())
sides = [a, b, c]
maximum = max(sides)
sides_nomax = sides
sides_nomax.remove(maximum)

if ((a + b) < c) or ((a + c) < b) or ((c + b) < a) or (a <= 0 or b <= 0 or c <= 0):
    print("Недопустимые значения длин сторон")
else:
    if maximum ** 2 == sides_nomax[0] ** 2 + sides_nomax[1] ** 2:
        print("Треугольник прямоугольный")
    elif maximum ** 2 < sides_nomax[0] ** 2 + sides_nomax[1] ** 2:
        print("Треугольник остроугольный")
    elif maximum ** 2 < sides_nomax[0] ** 2 + sides_nomax[1] ** 2:
        print("Треугольник тупоугольный")
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("Площадь треугольника равна:", S)

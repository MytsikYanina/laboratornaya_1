# -*- coding: cp1251 -*-
a, b, c = int(input()), int(input()), int(input())

if ((a + b) < c) or ((a + c) < b) or ((c + b) < a) or (a <= 0 or b <= 0 or c <= 0):
    print("������������ �������� ���� ������")
else:
    if a == b == c:
        print("����������� ��������������")
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print("����������� ��������������")
    else:
        print("����������� ��������������")
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("������� ������������ �����:", S)

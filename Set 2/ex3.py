# 3. Fie un tuplu (x,y) reprezentarea unui punct intr-un sistem cartezian.
# Sa se scrie o functie care primeste ca parametru o lista de puncte si
# returneaza o lista de tuple (a,b,c) unice care reprezinta dreptele
# unice determinate de acele puncte ((a,b,c) corespunde dreptei
# ax + by + c = 0).

import math


def line_from_points(p1: tuple, p2: tuple) -> tuple:
    """Return the normalized (a, b, c) coefficients of the line through p1 and p2."""
    x1, y1 = p1
    x2, y2 = p2

    a = y2 - y1
    b = x1 - x2
    c = -(a * x1 + b * y1)

    divisor = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
    if divisor == 0:
        divisor = 1
    a, b, c = a // divisor, b // divisor, c // divisor

    # Normalize sign so the same line always maps to the same tuple.
    for value in (a, b, c):
        if value != 0:
            if value < 0:
                a, b, c = -a, -b, -c
            break

    return a, b, c


def unique_lines(points: list) -> list:
    """Return the unique lines (a, b, c) determined by the given points."""
    lines = set()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if points[i] == points[j]:
                continue
            lines.add(line_from_points(points[i], points[j]))
    return list(lines)


points = [(0, 0), (1, 1), (2, 2), (0, 2)]
print('\n Exercise 3')
print(f' Unique lines determined by {points}: {unique_lines(points)}')
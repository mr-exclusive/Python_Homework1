# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
#
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math

x1 = int(input('Enter the coordinate X for point A: '))
y1 = int(input('Enter the coordinate Y for point A: '))

x2 = int(input('Enter the coordinate X for point B: '))
y2 = int(input('Enter the coordinate Y for point B: '))

print(f'The distance between point A({x1}, {y1}) and point B({x2}, {y2}) is {round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)}')

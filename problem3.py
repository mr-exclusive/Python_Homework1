# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
#
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x = int(input('Enter the coordinate X: '))
y = int(input('Enter the coordinate Y: '))

if x == 0 and y == 0:
    print('Invalid input! Requirements: X ≠ 0 AND Y ≠ 0')
else:
    if x > 0:
        if y > 0:
            print('I quarter')
        elif y < 0:
            print('IV quarter')
        else:
            print('A point lies on +X axis')
    elif x < 0:
        if y > 0:
            print('II quarter')
        elif y < 0:
            print('III quarter')
        else:
            print('A point lies on -X axis')
    else:
        if y > 0:
            print('A point lies on +Y axis')
        else:
            print('A point lies on -Y axis')

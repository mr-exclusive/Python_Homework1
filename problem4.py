# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Enter a quarter: '))

if 1 <= quarter <= 4:
    if quarter == 1:
        print('x > 0, y > 0')
    elif quarter == 2:
        print('x < 0, y > 0')
    elif quarter == 3:
        print('x < 0, y < 0')
    else:
        print('x > 0, y < 0')
else:
    print('Invalid input! Requirements: from 1 to 4')

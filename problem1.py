# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

day_of_week = int(input("Enter a day of week (from 1 to 7): "))

if 1 <= day_of_week <= 5:
    print("It's a workday.")
elif day_of_week == 6 or day_of_week == 7:
    print("It's a weekend.")
else:
    print("Invalid input!")

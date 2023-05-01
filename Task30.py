# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

print()
a1 = int(input("Введите первый элемент прогрессии: "))
print()
d = int(input("Введите разность прогрессии: "))
print()
n = int(input("Введите количество элементов прогрессии: "))
print()

arr = [a1 + (i-1)*d for i in range(1, n+1)]

print(f"Массив элементов арифметической прогрессии: {arr}")
print()
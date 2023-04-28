# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a ^ b, (a & b) << 1)

print()
a = int(input("Введите число А: "))
print()
b = int(input("Введите число B: "))
print()

print(f"{a} + {b} = {sum(a,b)}")
print()
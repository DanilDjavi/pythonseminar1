# Задание №4 Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

print()
s = int(input("Введите количество сделанных журавликов: "))
k = s // 3 * 2 
p = k // 4
s = k // 4
print()
print("Петя сделал", p, "журавликов")
print()
print("Катя сделала", k, "журавликов")
print()
print("Сережа сделал", s, "журавликов")
print()
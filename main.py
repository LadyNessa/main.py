# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#
# set_1 = set()
# set_2 = set()
#
# n = int(input("Введите количество чисел в первом множестве:"))
# m = int(input("Введите количество чисел во втором множестве:"))
#
# print("Введите числа первого множества:")
# count = 0
# while count < n:
#         set_1.add(input())
#         count += 1
#
# print("Введите числа второго множества:")
# count = 0
# while count < m:
#         set_2.add(input())
#         count += 1
#
# new_list = list(set_1.union(set_2))
# new_list.sort()
# print("Числа в порядке возрастания:", new_list)

# Задача 24. Напишите программу для нахождения максимального числа ягод

# bushes = []
# n = int(input("Введите количество кустов:"))
# print("Введите количество ягод на кустах:")
#
# for _ in range(n):
#         number = int(input())
#         bushes.append(number)
# print(bushes)
#
# berries = []
# for i in range(len(bushes)-1):
#         berries.append(bushes[i-1] + bushes[i] + bushes[i+1])
# berries.append(bushes[-2] + bushes[-1] + bushes[0])
# print(max(berries))

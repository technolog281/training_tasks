# Задание
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# Решение

list_1 = [1, 2, 4, 16, 64, 153, 235, 236]
list_2 = []
list_3 = []
for _ in list_1:
    if _ % 2 == 0:
        list_2.append(_ / 4)
    else:
        list_2.append(_ * 2)
for i in list_2:
    if i >= 1:
        list_3.append(int(i))
    else:
        list_3.append(i)
print(list_3)
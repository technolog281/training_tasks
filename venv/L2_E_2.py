# Задание
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# Решение
list_1 = {1, '5', 53.35, 'МЕГА', '1', '2', '3'}
list_2 = {1, 53.3, 36, 353, '2', '3'}
print(list_1.difference(list_2))
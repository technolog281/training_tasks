list = []
list_3 = {}

print('Введите произвольный список чисел:\n')
print('Для продолжения ввода нажмите Enter, для выхода - Q:\n')


while True:
    n = input()
    n = n.lower()
    if n == 'q':
        break
    else:
        list.append(n)

list_2 = set(list)

print(list_2)
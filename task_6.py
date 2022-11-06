# Напишите функцию, которая в качестве аргумента будет принимать список размером не менее 10 элементов.
# Список должен включать строки и числа.
# Функция должна вывести:
# 1. Список в перевернутом виде
# 2. Список в порядке убывания
# 3. Список в порядке возрастания
# 4. Срез списка от 2 до 7 элемента
# 5. Список с удаленным 5 элементом
# 6. Список без дубликатов
# 7. Список без чисел
"""
Сделала разные принты для каждого действия, потому что принт не сохраняет результат,
а некоторые задания тут являются взаимоисключающими. Делать для каждых двух строчек отдельную функцию,
в данном случае, смысла не вижу.
"""

list1 = [10, 'icecream', 4, 5, 3, 8, 7, 'milk', 4, 'mom', 7, 'sun']


def sort(listN):
    list2 = []
    for i in listN[::-1]:  # через list.reverse() не сработало, так что делаю так
        list2.append(i)
    print(f'Список в перевернутом виде: {list2}')

    listINT = []
    listSTR = []
    for i in listN:
        if type(i) == int:
            listINT.append(i)
        else:
            listSTR.append(i)
    listINT.sort(reverse=True)
    listSTR.sort(key=len, reverse=True)
    listINT.extend(listSTR)
    print(f'Список в порядке убывания: {listINT}')

    listINT = []
    listSTR = []
    for i in listN:
        if type(i) == int:
            listINT.append(i)
        else:
            listSTR.append(i)
    listINT.sort()
    listSTR.sort(key=len)
    listINT.extend(listSTR)
    print(f'Список в порядке возрастания: {listINT}')

    print(f'Срез списка от 2 до 7 элемента: {listN[1:8]}')

    list5 = listN    # переопределила что бы не изменять изначальный список
    del list5[4]
    print(f'Список с удаленным 5 элементом: {list5}')

    list6 = list(set(listN))  # что бы не изменять изначальный список, set содержит только уникальные значения
    print(f'Список без дубликатов: {list6}')

    list7 = []  # что бы не изменять изначальный список
    for i in listN:
        if type(i) == str:
            list7.append(i)
    print(f'Список без чисел: {list7}')


sort(list1)

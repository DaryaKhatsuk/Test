import functools
import operator

# Списки в языке Python могут содержать в себе вложенные списки. В то же время вложенные списки могут также
# состоять из списков, тем самым увеличивая глубину общей иерархии.
# В результате списки могут обретать структуру, похожую на следующую: [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]].
# Списки со множеством уровней вложенности могут пригодиться при описании сложных отношений между элементами, но
# при этом такая структура значительно усложняет выполнение операций над элементами. Процесс выравнивания (flattening)
# списка заключается в избавлении от вложенной структуры и простом перечислении входящих в него элементов.
# Допустим, для приведенного выше примера выровненный список будет выглядеть так:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Для выполнения операции выравнивания списка data можно последовать следующему алгоритму:
# 1. Если список data пуст, тогда возвращаем пустой список.
# 2. Если первый элемент списка data также является списком, тогда выравниваем первый элемент списка data и присваиваем
# результат переменной l1 Выравниваем все элементы первого элемента списка data, за исключением первого, и присваиваем
# результат переменной l2 Возвращаем результат конкатенации списков l1 и l2
# 3. Если первый элемент списка data не является списком, тогда Присваиваем переменной l1 список, состоящий из первого
# элемента списка data Выравниваем все элементы первого элемента списка data, за исключением первого, и присваиваем
# результат переменной l2 Возвращаем результат конкатенации списков l1 и l2
# Напишите функцию, реализующую рекурсивный алгоритм выравнивания списка, описанный выше. Функция должна принимать
# на вход список и возвращать выровненную версию списка. В основной программе продемонстрируйте работу функции
# на примере приведенного выше списка, а также нескольких других.
data = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
data2 = [2, [[[5], 8], 3], 2, [], 6, 4]
list1 = []
list2 = []


def funct(listN, l1):
    for i in listN:
        if i == []:
            continue
        elif type(i) == int:
            l1.append(i)
        elif type(i) == list:
            for j in i:
                if type(j) == int:
                    l1.append(j)
                else:
                    funct(j, l1)

    return l1


print(funct(data, list1))
print(funct(data2, list2))

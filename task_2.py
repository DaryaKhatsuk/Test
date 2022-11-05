# Напишите функцию, определяющую вид фигуры по количеству переданных в качестве аргумента сторон. Функция
# должна вернуть строку, представляющую собой вид фигуры
# Программа должна корректно обрабатывать
# и выводить названия для фигур с количеством сторон от трех до десяти включительно.
# Если введенное пользователем значение находится за границами этого диапазона, уведомите его об этом.

def sides(number):
    x = 'agon'
    if number == 3:
        return 'Triangle'
    elif number == 4:
        return 'Square, parallelogram and rhombus'
    elif number == 5:
        return f'Pent{x}'
    elif number == 6:
        return f'Hex{x}'
    elif number == 7:
        return f'Pentagondodecahedron'
    elif number == 8:
        return f'Regular oct{x}'
    elif number == 9:
        return f'Nine-square'
    elif number == 10:
        return f'Dec{x}'
    else:
        return 'Wrong number entered'


print(sides(int(input('Number of sides (>= 3 and <= 10): '))))

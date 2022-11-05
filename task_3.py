import datetime
# Напишите функцию, принимающую на вход дату и выводящую на экран дату, следующую за ней.
# Например: если пользователь введет дату, соответствующую 18 ноября 2019 года, на экран должен быть выведен
# следующий день, то есть 19 ноября 2019 года. Если входная дата будет представлять 30 ноября, то на выходе
# мы должны получить 1 декабря.
# И наконец, если ввести последний день года – 31 декабря 2019-го, пользователь должен увидеть на экране
# дату 1 января 2020-го. Дату пользователь должен вводить в три этапа: год, месяц и день.
# Убедитесь, что ваша программа корректно обрабатывает високосные годы.

months = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12
}


def function(day, month, year):
    if 1 <= day <= 31 and 1 <= len(str(year)) <= 4:
        m = month.lower()
        if m in months:
            m = months.get(m)
        else:
            return "Month is cannot"
        date = datetime.date(year, m, day)
        next_date = date + datetime.timedelta(days=1)
        return f"{next_date.day}.{next_date.month}.{next_date.year}"
    else:
        return 'Data entered incorrectly'


print(function(int(input('Day ')), input('Month '), int(input('Year '))))


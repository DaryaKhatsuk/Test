# Напишите функцию, которая в качестве аргументов будет принимать рост и вес.
# Функция должна возвращать индекс массы тела.
# В зависимости от полученного BMI, интерпретируйте полученный индекс.
# Прим: 25 >= BMI < 30 >>> Вы имеете избыточный вес

def bmi(growth, weight):
    growth = float(f'{growth[0]}.{growth[1:]}')
    BMI = weight/growth**2
    print(f'Your {BMI}')
    if BMI < 18.5:
        return 'BMI < 18.5: Below normal weight'
    elif 18.5 <= BMI < 25:
        return '18.5 <= BMI < 25: Normal weight'
    elif 25 <= BMI < 30:
        return '25 <= BMI < 30: Overweight'
    elif 30 <= BMI < 35:
        return '30 <= BMI < 35: Grade I obesity'
    elif 35 <= BMI < 40:
        return '35 <= BMI < 40: Grade II obesity'
    else:
        return 'BMI >= 40: Grade III obesity'


print(bmi(input('Growth (cm): '), int(input('Weight (kg): '))))

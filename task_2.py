"""
2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000: Вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9
= 28 – делится нацело на 7. Внимание: использовать только арифметические операции! К каждому элементу списка добавить
17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Внимание: новый список
не создавать!!!
"""

list_cubes = []
for i in range(1, 1001, 2):
    list_cubes.append(i ** 3)

for i in [0, 17]:
    summ = 0
    for num in list_cubes:
        num += i
        list_digits = []
        for j in range(0, 15):
            list_digits.append(num // (10 ** j) % 10)
        summ_digits = 0
        for j in list_digits:
            summ_digits += j
        if (summ_digits % 7) == 0:
            summ += num
    if i:
        text = '(увеличенных на ' + str(i) + ')'
    else:
        text = ''
    print('Сумма чисел из списка', text, ', сумма цифр которых делится на 7: ', summ, sep='')

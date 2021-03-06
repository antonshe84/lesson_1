"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
"""


for i in range(10):
    duration = int(input("Введите промежуток времени (в секундах): "))
    # year = round(duration // (3600 * 24 * 30.44 * 12))
    # month = round(duration % (3600 * 24 * 30.44 * 12) // (3600 * 24 * 30.44))
    # day = round(duration % (3600 * 24 * 30.44) // (3600 * 24))
    day = duration // (3600 * 24)
    hour = duration % (3600 * 24) // 3600
    min = duration % 3600 // 60
    sec = duration % 60

    # print(year, 'лет', month, 'мес', day, 'дней', hour, 'часов', min, 'минут',  sec, 'секунд')

    # Первый вариант вывода (0 значения выводятся):
    # print(day, 'дней', hour, 'часов', min, 'минут', sec, 'секунд')

    # Второй вариант вывода (0 значения пропаускаются):
    if day:
        print(day, 'дней', end=' ')
    if hour:
        print(hour, 'часов', end=' ')
    if min:
        print(min, 'минут', end=' ')
    if sec:
        print(sec, 'секунд', end=' ')
    print('')

"""

3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.

"""

for number in range(1, 21):
    if number == 1:
        print(number, 'процент')
    elif 2 <= number <= 4:
        print(number, 'процента')
    elif 5 <= number <= 20:
        print(number, 'процентов')

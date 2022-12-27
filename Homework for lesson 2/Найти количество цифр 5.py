# Пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.

found_figure = 0
count = 0
while count <= 9:
    x = int(input())
    if x == 5:
        found_figure += 1
    count += 1

print(found_figure)

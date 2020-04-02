number = int(input('Введите натуральное число: '))
max_num = 0
while number > 0:
    var = number % 10
    if var > max_num:
        max_num = var
    number = number // 10

print(max_num)

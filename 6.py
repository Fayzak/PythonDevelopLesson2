number = int(input('Введите натуральное число: '))
a = 0
while number > 0:
    var = number % 10
    var += a
    number = number // 10
    a = var

print(var)
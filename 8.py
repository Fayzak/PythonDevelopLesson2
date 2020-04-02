number = int(input('Введите натуральное число: '))
while number > 0:
    if number % 10 == 5:
        print('Yes')
        break
    number = number // 10
else:
    print('No')

number = int(input('Введите натуральное число: '))
count = 0
while number > 0:
    if number % 10 == 5:
        count += 1
    number = number // 10

print(count)
number = int(input('Введите натуральное число: '))

'''
while number > 0:
    print(number % 10)
    number = number // 10
'''

while number > 0:
    print(number // (10 ** (len(str(number)) - 1)))
    number = number % (10 ** (len(str(number)) - 1))


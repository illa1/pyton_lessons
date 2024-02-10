import random

# n = random.randint(1, 3)

print('\u2591' * 40)
print('\u2591' * 11 , 'число від 1 до 3' , '\u2591'* 11)
print('\u2591' * 40)

x = 0

for i in range(1, 5):
    print(f'Raund: {i} :', end=' ')
    random_number = random.randint(1, 3)
    number = int(input('Input number: '))
    if random_number == number:
        print('\x1b[1;32m' 'You guessed' '\x1b[0;37m')
        x = x + 1
    else:
        print(f'\x1b[1;31m' 'Wrong [{number} <> {random_number}]' '\x1b[0;37m')

print('\u2591' * 11)
print('\u2591' * 4 , x , '\u2591' * 4)
print('\u2591' * 11)



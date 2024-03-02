import random

# y = {'x': 222, 'y': 111, 'z': 12}
#
# for key, item in y.items():
#     print(key, ' = ', item)

guess = random.randint(1 , 10)
while True:
    number = int(input('input number:'))
    if guess == number:
        print('Win')
        break
    elif guess > number:
        print('більше')
    elif guess < number:
        print('менше')




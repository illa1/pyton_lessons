import random

# list_1 = [2, 22, 3, 4, 'yellow', 88]

# length = len(list_1)
# print('len= %d' % length)
# for i in range(length):
#     print(list_1[i])

# for i in list_1:
#     print(i)


# new_list = []
# for i in range(10):
#     new_list.append(random.randint(0, 10))
#
# sum = 0
# n = 0
#
# for i in new_list:
#     if i % 2 == 0 and i != 0:
#         n += 1
#         sum += i
#
#
#
# print(new_list)
# print(n,'sum = %d' % sum)


# histogram = []
# for i in range(5):
#     histogram.append(random.randint(0, 10))
#
# for i in histogram:
#     red = ''
#     if i > 5:
#         red = '\x1b[0;31m'
#
#     print(red, '\u2588'*i, i, '\x1b[0;37m')


# numbers = []
# for i in range(10):
#     numbers.append(random.randint(1, 5))
#
# unique = []
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
#
# print(numbers)
# print(unique)


# numbers = [random.randint(0,10) for i in range(10)]
# numbers = [i*i for i in range(10)]
# print(numbers)
#
# file = open('num.txt', 'w')
# for n in numbers:
#     file.write('%s\n' % n)
#
# file.close()

number_from_file = []
file = open('num.txt', 'r')
for n in file.readlines():
    number_from_file.append(int(n))

print(number_from_file)

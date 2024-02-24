# number = int(input('Введіть число: '))
#
# while number > 1:
#     number //= 2
#     print(number)

# num = 859020
# count = 0
#
# while num != 0:
#     num //= 10
#     count += 1
#
# print(count)

# list1 = [2, 4, 6]
# tuplex = (2, 4, 6)
#
# list1[0] = 999
# print(list1)
# tuplex[0] = 999
#
# print(tuplex)

# tuplex = ()
# for i in range(100):
#     tuplex += (i,)
#
# print(tuplex)

dic = {
      'name': 'Ivan',
      'age': 14,
      'sex': 'Male'
      }
for item in dic:
    print(item)

for key, item in dic.items():
    print(key, '=', item)


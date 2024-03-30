# a = 1
# b = 2
#
# def dodamka(a, b):
#     return a + b

def test(a):
    if a > 0:
        return 'більше нуля'
    else:
        return 'менше нуля'


def test1(a, b=1):
    result = 'більше нуля'
    if a < 0:
        result = 'менше нуля'
    if b > 0:
        result += '   b більше нуля'
    return result


print('===>', test1(-1,))
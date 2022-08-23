# import string
# import random
# import sys
#
#
#
# sys.setrecursionlimit(1000000)
# print(sys.getrecursionlimit())
#
# def gen(length):
#
#     letters = string.ascii_lowercase
#     random_string = ' '.join(random.choice(letters) for i in range(length))
#
#     lst = []
#     for i in random_string:
#         if i != ' ':
#             lst.append(i)
#     dct = {}
#     for i in lst:
#         dct[i] = dct.get(i, 0) + 1
#
#     print(dct)
#
# gen(1000000)




with open('some.txt', 'r') as file:

    lst = []
    for i in file:
        for j in i:
            if j.isalpha():
                j = j.lower()
                j = j.strip()
                lst.append(j)
def func(arg):
    dct = {}
    for i in lst:
        dct[i] = dct.get(i, 0) + 1
    return dct
print(func(lst))







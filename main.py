#less1
#1
# print('Hello, Python!')

#2
# a = '234123'
# print (type (a))
# a = int(a)
# print (type (a))
# b = a
# print(id(b))
# c = id(b) - b
# print(c)
# # не впевнений що зрозумів завдання для зміної "c"

#3
# a = input('name: ')
# b = input('surname: ')
# c = input('age: ')
# f = 'Привіт, %s %s!!! Твій вік %s років!'
# print(f % (a, b, c))
# print(f'"Hi, {a} {b} !!!" "Your age is {c}" yo!')

#less2
#1

# lst = [1, 2, 3, 4, 5, 6]
# a = 'a - append'
# b = 'b - insert'
# c = 'c - remove'
# d = 'd - index'
# print(lst)
# print(a)
# print(b)
# print(c)
# print(d)
# e = input('your variant: ')
#
# if e == 'a' or e == 'b' or e == 'c' or e == 'd':
#     print('great choice. go ahead')
# elif e != 'a' or 'b' or 'c' or 'd':
#     print('error, make other choice')
#
# if e == 'a':
#     a1 = 'в якому форматі ви бажаєте ввести новий елемент списку?'
#     print(a1)
#     a2 = '1 - формат int'
#     a3 = '2 - формат str'
#     print(a2)
#     print(a3)
#     a4 = int(input('виберіть формат: '))
#
#     if a4 == 1:
#         a5 = int(input('введіть елемент: '))
#         if a5 not in lst:
#             lst.append(a5)
#             print(lst)
#         else:
#             print('такий елемент вже існує')
#
#
#
#     if a4 == 2:
#         a6 = str(input('введіть елемент: '))
#         if a6 not in lst:
#             lst.append(a6)
#             print(lst)
#         else:
#             print('введіть інший елемент списку')
#
#
#
# elif e == 'b':
#     g = int(input('index of lst: '))
#     h = 'введіть новий елемент: '
#     h1 = 'в якому форматі ви бажаєте ввести новий елемент списку?'
#     print(h1)
#     h2 = '1 - формат int'
#     h3 = '2 - формат str'
#
#     print(h2)
#     print(h3)
#
#     h4 = int(input('введіть формат: '))
#     if h4 == 1:
#         h5 = int(input('введіть новий елемент: '))
#         if h5 not in lst:
#             lst.insert(g, h5)
#             print(lst)
#         else:
#             print('введіть інший елемент списку')
#
#
#     if h4 == 2:
#         h6 = str(input('введіть новий елемент: '))
#         if h6 not in lst:
#             lst.insert(g, h6)
#             print(lst)
#         else:
#             print('введіть інший елемент списку')
#
#
#
# elif e == 'c':
#     k = int(input('номер в списку: '))
#     lst.remove(k)
#     print(lst)
#
# elif e == 'd':
#     l = int(input('номер зі списку: '))
#     print(lst.index(l))




# LESS 3

# lst = [1, 'hello', 4, 3, 6, 'python', 7, 2, 10, 6, 5, 'd', 'a', 's']
#
# a = 'a - user'
# b = 'b - admin'
# print(a)
# print(b)
# c = input('enter a or b: ')
# if c == 'a':
#     print(lst)
#
# elif c == 'b':
#     b = input('enter login and password: ').split()
#     if b[0] == 'admin' and b[1] == '1111':
#         print(lst)
#
#         lst_act = ['remove', 'append', 'insert', 'index', 'copy', 'extend', 'clear', 'count', 'pop', 'reverse', 'sort']
#         m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11 = lst_act
#         print(f'm1 = {m1}\nm2 = {m2}\nm3 = {m3}\nm4 = {m4}\nm5 = {m5}\nm6 = {m6}\nm7 = {m7}\nm8 = {m8}\nm9 = {m9}\nm10 = {m10}\nm11 = {m11}')
#
#         d = input('виберіть метод списку: ')
#         while d:
#             if d == 'm1' or d == 'm2' or d == 'm3' or d == 'm4' or d == 'm5' or d == 'm6' or d == 'm7' or d == 'm8' or d == 'm9' or d == 'm10' or d == 'm11':
#                 break
#             elif d != 'm1' or d != 'm2' or d != 'm3' or d != 'm4' or d != 'm5' or d != 'm6' or d != 'm7' or d != 'm8' or d != 'm9' or d != 'm10' or d != 'm11':
#                 d = input('виберіть метод списку: ')
#                 continue
#
#
#         #remove
#         while d == 'm1':
#             if d == 'm1':
#                 print('в якому форматі ви бажаєте ввести елемент списку, який будемо видаляти?')
#                 d2 = '1 - формат int'
#                 d3 = '2 - формат str'
#                 print(d2)
#                 print(d3)
#                 d4 = int(input('виберіть формат: '))
#
#                 if d4 == 1:
#                     d5 = int(input('введіть елемент зі списку: '))
#                     while d5:
#                         if d5 not in lst:
#                             print('такого елемента немає в списку')
#                             d5 = int(input('введіть елемент зі списку: '))
#                             continue
#                         elif d5 in lst:
#                             lst.remove(d5)
#                             print(lst)
#                             break
#
#                 if d4 == 2:
#                     d5 = str(input('введіть елемент зі списку: '))
#                     while d5:
#                         if d5 not in lst:
#                             print('такого елемента немає в списку')
#                             d5 = str(input('введіть елемент зі списку: '))
#                             continue
#                         elif d5 in lst:
#                             lst.remove(d5)
#                             print(lst)
#                             break
#                 m387 = input('бажаєте продовжити роботу з методами списку? yes/no   ')
#                 m397 = 'yes'
#                 m407 = 'no'
#                 if m387 == m397:
#                     continue
#                 elif m387 == m407:
#                     break
#
#
#
#
#
#
#         #append
#         while d == 'm2':
#             if d == 'm2':
#                 print('в якому форматі ви бажаєте ввести елемент списку, який буде додано до списку?')
#                 m21 = '1 - int'
#                 m22 = '2 - str'
#                 print(m21)
#                 print(m22)
#                 m23 = int(input('виберіть формат: '))
#
#                 if m23 == 1:
#                     m24 = int(input('введіть елемент: '))
#                     while m24 in lst:
#                         print('такий елемент вже присутній в списку')
#                         m25 = input('додати його до списку? yes/no:  ')
#                         m26 = 'yes'
#                         m27 = 'no'
#                         if m25 == m26:
#                             lst.append(m24)
#                             print(lst)
#                         elif m25 == m27:
#                             break
#                     else:
#                         lst.append(m24)
#                         print(lst)
#
#                 if m23 == 2:
#                     m28 = str(input('введіть елемент: '))
#                     while m28 in lst:
#                         print('такий елемент вже присутній в списку')
#                         m29 = input('додати його до списку? yes/no:  ')
#                         m30 = 'yes'
#                         m31 = 'no'
#                         if m29 == m30:
#                             lst.append(m28)
#                             print(lst)
#                             break
#                         elif m29 == m31:
#                             print('the end')
#                             break
#
#                     else:
#                         lst.append(m28)
#                         print(lst)
#
#                 m384 = input('бажаєте продовжити роботу з методами списку? yes/no   ')
#                 m394 = 'yes'
#                 m404 = 'no'
#                 if m384 == m394:
#                     continue
#                 elif m384 == m404:
#                     break
#
#
#
#
#         #insert
#         while d == 'm3':
#             if d == 'm3':
#
#                 ind = int(input('індекс списку:  '))
#
#                 print('який формат нового елементу, який ви бажаєте вставити в список?')
#                 m31 = '1 - int'
#                 m32 = '2 - str'
#                 print(m31)
#                 print(m32)
#                 m33 = int(input('виберіть формат: '))
#                 if m33 == 1:
#                     m34 = int(input('введіть новий елемент: '))
#                     while m34 in lst:
#                         print('такий елемент присутній в списку')
#                         m35 = input('бажаєте додати його? yes/no  ')
#                         m36 = 'yes'
#                         m37 = 'no'
#                         if m35 == m36:
#                             lst.insert(ind, m34)
#                             print(lst)
#                             break
#                         elif m35 == m37:
#                             print('the end')
#                             break
#                     else:
#                         lst.insert(ind, m34)
#                         print(lst)
#
#                 if m33 == 2:
#                     m341 = str(input('введіть новий елемент: '))
#                     while m341 in lst:
#                         print('такий елемент присутній в списку')
#                         m351 = input('бажаєте додати його? yes/no  ')
#                         m361 = 'yes'
#                         m371 = 'no'
#                         if m351 == m361:
#                             lst.insert(ind, m341)
#                             print(lst)
#                             break
#                         elif m351 == m371:
#                             print('the end')
#                             break
#                     else:
#                         lst.insert(ind, m341)
#                         print(lst)
#
#                 m38 = input('бажаєте продовжити роботу з методами списку? yes/no   ')
#                 m39 = 'yes'
#                 m40 = 'no'
#                 if m38 == m39:
#                     continue
#                 elif m38 == m40:
#                     break
#
#         #index
#         while d == 'm4':
#             if d == 'm4':
#                 print('який формат елемента зі списку, індекс якого ви бажаєте дізнатися?')
#                 m41 = '1 - int'
#                 m42 = '2 - str'
#                 print(m41)
#                 print(m42)
#                 m43 = int(input('виберіть формат: '))
#                 if m43 == 1:
#                     m44 = int(input('введіть об\'єкт списку, щоб дізнатися його індекс:  '))
#                     print(lst.index(m44))
#                 elif m43 == 2:
#                     m45 = str(input('введіть об\'єкт списку, щоб дізнатися його індекс:  '))
#                     print(lst.index(m45))
#                 m46 = input('бажаєте продовжити роботу з методами списку? yes/no   ')
#                 m47 = 'yes'
#                 m48 = 'no'
#                 if m46 == m47:
#                     continue
#                 elif m46 == m48:
#                     break
#
#
#         #copy
#         if d == 'm5':
#             lst_new = lst.copy()
#             print(lst)
#             print(lst_new)
#
#
#         #extend
#
#         while d == 'm6':
#             if d == 'm6':
#
#                 print('в якому форматі ви бажаєте додати список?')
#                 m61 = '1 - int'
#                 m62 = '2 - str'
#                 print(m61)
#                 print(m62)
#                 m63 = int(input('оберить формат:  '))
#                 if m63 == 1:
#                     m67 = int(input('скільки елементів буде в новому списку?:  '))
#                     lst_int = []
#                     for i in range(0, m67):
#                         m69 = int(input('введіть числа власного списку: '))
#                         lst_int.append(m69)
#                         print(lst_int)
#                     lst.extend(lst_int)
#                     print(lst)
#                 if m63 == 2:
#                     m67 = int(input('скільки елементів буде в новому списку?:  '))
#                     lst_str = []
#                     for i in range(0, m67):
#                         m68 = str(input('введіть стрічки власного списку: '))
#                         lst_str.append(m68)
#                         print(lst_str)
#                     lst.extend(lst_str)
#                     print(lst)
#                 m661 = input('бажаєте продовжити роботу з методами списку? yes/no   ')
#                 m662 = 'yes'
#                 m663 = 'no'
#                 if m661 == m662:
#                     continue
#                 elif m661 == m663:
#                     break
#
#
#         #clear
#         if d == 'm7':
#             lst.clear()
#             print(lst)
#
#         #count
#         while d == 'm8':
#             if d == 'm8':
#                 print('в якому форматі елемент, кількість якого в списку ви бажаєте визначити?')
#                 m81 = '1 - int'
#                 m82 = '2 - str'
#                 print(m81)
#                 print(m82)
#                 m83 = int(input('виберіть формат: '))
#                 if m83 == 1:
#                     m84 = int(input('введіть елемент int зі списку: '))
#                     print(lst.count(m84))
#                 if m83 == 2:
#                     m85 = str(input('введіть елемент str зі списку: '))
#                     print(lst.count(m85))
#                 m86 = input('бажаєте продовжити роботу з методами списку? yes/no   ')
#                 m87 = 'yes'
#                 m88 = 'no'
#                 if m86 == m87:
#                     continue
#                 elif m86 == m88:
#                     break
#
#
#         #pop
#         while d == 'm9':
#             if d == 'm9':
#                 print('бажаєте видалити елемент списку з кінця чи за індексом?')
#                 m91 = '1 - з кінця'
#                 m92 = '2 - за індексом'
#                 print(m91)
#                 print(m92)
#                 m93 = int(input('зробіть вибір: '))
#                 if m93 == 1:
#                     print(lst.pop())
#                     print(lst)
#                 if m93 == 2:
#                     m94 = int(input('введіть індекс елементу:   '))
#                     print(lst.pop(m94))
#                     print(lst)
#                 m95 = input('бажаєте продовжити роботу з методами списку? yes/no   ')
#                 m96 = 'yes'
#                 m97 = 'no'
#                 if m95 == m96:
#                     continue
#                 elif m95 == m97:
#                     break
#
#
#         #reverse
#
#         while d == 'm10':
#             if d == 'm10':
#                 lst.reverse()
#                 print(lst)
#             m100 = input('бажаєте продовжити роботу з методами списку? yes/no   ')
#             m101 = 'yes'
#             m102 = 'no'
#             if m100 == m101:
#                 continue
#             elif m100 == m102:
#                 break
#
#
#
#
#
#
#         #sort
#         if d == 'm11':
#             print('основний список')
#             print(lst)
#             print('список з цифр')
#             lst_int = [i for i in lst if type(i) == int]
#             print(lst_int)
#             print('список зі стрічок')
#             lst_str = [i for i in lst if type(i) == str]
#             print(lst_str)
#             print('відсортований список з цифр')
#             lst_int.sort()
#             print(lst_int)
#             print('обєднанний новий список')
#             lst_final = lst_int + lst_str
#             print(lst_final)






#4 LESSON

# dct = {'person': {'in_dct': [1, 2, 3],
#        'after_list': {4, '5'},
#        'after_set': ('hello',)}}
#
#
# result_dct = {}
# for key, value in dct.items():
#     result_dct[key] = ""
#     result_dct[tuple(list(value))] = ""
#     for elem in value:
#         result_dct[elem] = ""
#
# print(result_dct)
# print(result_dct.keys())





# LESSON 5


#1 part

# def func(arg_1 = list[int], arg_2= [55, 66, 77]):
#
#     dct_1 = {}
#
#     dct_1 = {i: j for i, j in zip(arg_1, arg_2)}
#
#     return dct_1
#
# dct = func([1, 2, 3], ['efv', 'efvdfv', 'aefv'])
#
# print(dct)


# 2 part

# def func(arg_1, arg_2):
#
#     for elem in arg_1[:]:
#         if type(elem) == set:
#             arg_1.remove(elem)
#
#     dct_1 = {}
#     for i in arg_1:
#         dct_1 = {i: arg_2 for i in arg_1}
#     return dct_1
#
# dct = func([1, {'ksdnjv', 133423423}, 2, {'csd', 'sxsdsfv', 555, 231}, 3], [23, 452, 4643])
# print(dct)





# LESSON 6

#1 частина

# lst = [1, 2, 3, '4', '5', '6']
#
# lst_new = list(map(lambda arg: int(arg) if isinstance(arg, str) else str(arg), lst))
#
# print(lst_new)


#2 частина

# def func(arg):
#     if type(arg) == int:
#         return str(arg)
#     elif type(arg) == str:
#         return int(arg)
#
#
# lst = [1, 2, 3, '4', '5', '6']
# lst_new_2 = list(map(func, lst))
# print(lst_new_2)

#3 частина

# def func(*args):
#     lst_1 = []
#     set_1 = {}
#
#     for arg in args:
#         if len(lst_1) <= 9 and arg not in lst_1 and type(arg) != list and type(arg) != set:
#             lst_1.append(arg)
#
#
#     set_1 = set(lst_1)
#     return set_1
#
# set_2 = func(1, 8888, [1, 2], 1, {6, 4}, 1, (6, 4), 2, 'fcscs', 'qdcdcwdc', 888, 777, 'lsjdvnisjdnvsij', 99)
# # set_2 = func(1, 8888, [1, 2], 'fcscs', 'qdcdcwdc', 888, 99)
# print(set_2)







# LESSON 7


# def decorator(*s):
#
#     def main_func(func):
#         lst_1 = []
#         lst_2 = []
#         dct = {}
#         dct_2 = {}
#
#         for i in s:
#             if type(i) == int:
#                 lst_1.append(i)
#                 dct[type(i)] = lst_1
#         # print(dct)
#
#         for i in s:
#             if type(i) == str:
#                 lst_2.append(i)
#                 dct_2[type(i)] = lst_2
#         # print(dct_2)
#
#         dct.update(dct_2)
#
#         def wrapper(*args, ** kwargs):
#
#             return func(dct, *args, **kwargs)
#
#         return wrapper
#
#     return main_func
#
#
# @decorator(1111, 3333333, 'jfhckjsdbckjsdbc', 1, 2, 'st', 'sretg', 'ds', 4, 'wljfbvwd', 4554)
# def func(*args, **kwargs):
#     return args
#
#
# n = func(9999999999999)
# print(n)

#SECOND VARIANT

# def decorator(*s):
#
#     def main_func(func):
#
#         dct = {}
#
#         lst_int = [i for i in s if type(i) == int]
#         lst_str = [i for i in s if type(i) == str]
#         dct[type(lst_int[0])] = lst_int
#         dct[type(lst_str[0])] = lst_str
#
#
#         def wrapper(*args, **kwargs):
#
#             return func(dct, *args, **kwargs)
#
#         return wrapper
#
#     return main_func
#
#
# @decorator(1111, 22, 3333333, 'jfhckjsdbckjsdbc', 'afdvafdv')
# def func(*args, **kwargs):
#     return args
#
# n = func()
# print(n)




# LESSON 8
# 8.1 ну впевнений що правильно зрозумів завдання тому два варіанти

# def func(*args):
#     dct = {arg: arg + 1 for arg in args}
#     yield (dct)
# a = func(1, 88, 2, 4, 55)
#
# print(next(a))

# або 8.1 другий варіант

# def func(*args):
#     dct_1 = {}
#     for arg in args:
#         dct = {arg: arg + 1}
#         dct_1.update(dct)
#     yield (dct_1)
# a = func(1, 88, 2, 4, 55)
#
# print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))

# 8.2
#1 варіант (без NEXT за межами генератора)
# def func(r):
#     lst = []
#     for i in range(r):
#         if len(lst) >= 0 and len(lst) <= 2 and i % 2 == 1:
#             lst.append(i)
#     return lst
# a = func(20)
# print(a)


#2 варіант (з ОДНИМ NEXT за межами генератора)
# def func(r):
#     lst = []
#     for i in range(r):
#         if 0 <= len(lst) <= 2 and i % 2 == 1:
#             lst.append(i)
#     yield lst
# a = func(20)
# print(next(a))





# LESSON 9
#9.1

# def func(*args, **kwargs):
#
#     for key, value in kwargs.items():
#         text = open('homeWork_9_1.txt', 'a')
#         text.write(f'{key} = {value}\n')
#         text.close()
#
# n = func(kjn = 4, sfv = 234, iughkjb = 3434)


#9.2

# def gen(*args, **kwargs):
#     dct = {}
#     with open('homeWork_9_1.txt') as f:
#         for line in f:
#             (key, value) = line.split('=')
#             dct[key] = int(value)
#
#     print(dct)
#     for elem in dct.items():
#         yield elem
#
# for elem in gen('homeWork_9_1.txt'):
#     print(elem)


# LESSON 10

# with open('some.txt', 'r') as file:
#
#     lst = []
#     for i in file:
#         for j in i:
#             if j.isalpha():
#                 j = j.lower()
#                 j = j.strip()
#                 lst.append(j)
# def func(arg):
#     dct = {}
#     for i in lst:
#         dct[i] = dct.get(i, 0) + 1
#     return dct
# print(func(lst))


# LESSON 11

# class Main:
#     dct = {12: 249, 'skd': 'sj', 'ks': 242, 933: 'las'}
#     tup = (1, 2, 5, 1, 2, 2, 'jd', 'ka')
#
#     def __init__(self):
#
#         access = input('user or admin:  ')
#         if access == 'user':
#             print(self.dct)
#             print(self.tup)
#         elif access == 'admin':
#             # log_pass = input('enter login and password: ').split()
#             # if log_pass[0] == 'admin' and log_pass[1] == '1111':
#                 self.method()
#
#
#     def method(self):
#         print(f'1. dict_items\n2. dict_keys\n3. dict_pop\n4. dict_values\n5. dict_copy\n6. dict_clear\n7. dict_update\n'
#               f'8. dict_fromkeys\n9. dict_get\n10. dict_popitem\n11. dict_setdefault\n12. tuple_index\n13. tuple_count\n14. tuple_add_elem')
#         method = int(input('choose method:  '))
#         if method == 1:
#             self.dict_items()
#         elif method == 2:
#             self.dict_keys()
#         elif method == 3:
#             self.dict_pop()
#         elif method == 4:
#             self.dict_values()
#         elif method == 5:
#             self.dict_copy()
#         elif method == 6:
#             self.dict_clear()
#         elif method == 7:
#             self.dict_update()
#         elif method == 8:
#             self.dict_fromkeys()
#         elif method == 9:
#             self.dict_get()
#         elif method == 10:
#             self.dict_popitem()
#         elif method == 11:
#             self.dict_setdefault()
#         elif method == 12:
#             self.tuple_index()
#         elif method == 13:
#             self.tuple_count()
#         elif method == 14:
#             self.tuple_add_elem()
#
#     def cont_ex(self):
#         i = int(input('continue(1) or exit(2): '))
#         if i == 1:
#             self.method()
#         elif i == 2:
#             exit()
#
#
#     def type_arg(self):
#         self.type_arg = input('enter type arg int, str, list, tuple, dict, set: ')
#         if self.type_arg == 'int':
#             self.arg = int(input('enter arg: '))
#         elif self.type_arg == 'str':
#             self.arg = input('enter arg: ')
#         elif self.type_arg == 'list':
#             self.arg = list(input('enter arg:').split())
#         elif self.type_arg == 'tuple':
#             self.arg = tuple(input('enter arg: ').split())
#         elif self.type_arg == 'dict':
#             self.a = int(input('type key int(1) or str(2): '))
#             if self.a == 1:
#                 self.key = int(input('enter key: '))
#             elif self.a == 2:
#                 self.key = input('enter key: ')
#             self.b = int(input('type value int(1) or str(2): '))
#             if self.b == 1:
#                 self.value = int(input('enter value: '))
#             elif self.b == 2:
#                 self.value = input('enter value: ')
#
#             self.arg = {}
#             self.arg[self.key] = self.value
#         elif self.type_arg == 'set':
#             self.arg = set(input('enter set: ').split())
#
#
#     def dict_items(self):
#         print(Main.dct)
#         for i in Main.dct.items():
#             print(i)
#         self.cont_ex()
#
#     def dict_keys(self):
#         print(Main.dct)
#         for i in Main.dct:
#             print(i)
#         self.cont_ex()
#
#     def dict_pop(self):
#         print(Main.dct)
#         self.type_arg()
#         e = Main.dct.pop(self.arg)
#         print(Main.dct)
#         self.cont_ex()
#
#     def dict_values(self):
#         print(Main.dct)
#         for i in Main.dct.values():
#             print(i)
#         self.cont_ex()
#
#     def dict_copy(self):
#         print(Main.dct)
#         e = input('enter new dct: ')
#         s = Main.dct.copy()
#         print(f'{e} = {Main.dct.copy()}')
#         self.cont_ex()
#
#     def dict_clear(self):
#         print(Main.dct)
#         Main.dct.clear()
#         print(Main.dct)
#         self.cont_ex()
#
#     def dict_update(self):
#         print(Main.dct)
#         self.a = int(input('type key int(1) or str(2): '))
#         if self.a == 1:
#             self.key = int(input('enter key: '))
#         elif self.a == 2:
#             self.key = input('enter key: ')
#         self.b = int(input('type value int(1) or str(2): '))
#         if self.b == 1:
#             self.value = int(input('enter value: '))
#         elif self.b == 2:
#             self.value = input('enter value: ')
#
#         self.arg = {}
#         self.arg[self.key] = self.value
#         if self.key not in Main.dct.keys():
#             Main.dct.update(self.arg)
#             print(Main.dct)
#         else:
#             print('this key already in dct')
#             self.c = int(input('wanna change key(1) or rewrite value(2)'))
#             if self.c == 1:
#                 self.dict_update()
#             else:
#                 Main.dct.update(self.arg)
#                 print(Main.dct)
#         self.cont_ex()
#
#
#     def dict_fromkeys(self):
#         print(Main.dct)
#         self.key = list(input('enter keys: ').split())
#         print(self.key)
#         e = Main.dct.fromkeys(self.key)
#         print(e)
#         self.cont_ex()
#
#     def dict_get(self):
#         print(Main.dct)
#         self.type_arg()
#         e = Main.dct.get(self.arg)
#         print(f'value {e}')
#         self.cont_ex()
#
#     def dict_popitem(self):
#         print(Main.dct)
#         print(Main.dct.popitem())
#         self.cont_ex()
#
#     def dict_setdefault(self):
#         print(Main.dct)
#         self.a = int(input('wanna: 1.return value of key; 2.add new key; 3.add new item: '))
#         if self.a == 1:
#             self.aa = int(input('type key int(1) or str(2): '))
#             if self.aa == 1:
#                 self.b = int(input('enter key: '))
#             elif self.aa == 2:
#                 self.b = input('enter key: ')
#             print(Main.dct.setdefault(self.b))
#         elif self.a == 2:
#             self.aa = int(input('type key int(1) or str(2): '))
#             if self.aa == 1:
#                 self.b = int(input('enter key: '))
#             elif self.aa == 2:
#                 self.b = input('enter key: ')
#             Main.dct.setdefault(self.b)
#             print(Main.dct)
#         elif self.a == 3:
#             self.aa = int(input('type key int(1) or str(2): '))
#             if self.aa == 1:
#                 self.b = int(input('enter key: '))
#             elif self.aa == 2:
#                 self.b = input('enter key: ')
#             self.c = int(input('type value int(1) or str(2): '))
#             if self.c == 1:
#                 self.bb = int(input('enter value: '))
#             elif self.c == 2:
#                 self.bb = input('enter value: ')
#             Main.dct.setdefault(self.b, self.bb)
#             print(Main.dct)
#         self.cont_ex()
#
#
#     def tuple_index(self):
#         print(Main.tup)
#         self.a = int(input('type element of tuple int(1) or str(2): '))
#         if self.a == 1:
#             self.b = int(input('enter element: '))
#         elif self.a == 2:
#             self.b = input('enter element: ')
#         print(Main.tup.index(self.b))
#         self.cont_ex()
#
#     def tuple_count(self):
#         print(Main.tup)
#         self.a = int(input('type element of tuple int(1) or str(2): '))
#         if self.a == 1:
#             self.b = int(input('enter element: '))
#         elif self.a == 2:
#             self.b = input('enter element: ')
#         e = Main.tup.count(self.b)
#         print(e)
#         self.cont_ex()
#
#     def tuple_add_elem(self):
#         print(Main.tup)
#         self.type_arg()
#         # self.a = int(input('type add element to tuple int(1) or str(2): '))
#         # if self.a == 1:
#         #     self.b = int(input('enter element: '))
#         # elif self.a == 2:
#         #     self.b = input('enter element: ')
#         e = list(Main.tup)
#         e.append(self.arg)
#         print(tuple(e))
#         self.cont_ex()
#
#
# a = Main()

#LESSON 12

# from datetime import datetime
#
# class Main:
#     name = 'Tom'
#
#     def __init__(self, height, weight):
#         self._height = height
#         self.__weight = weight
#
#
#     def _func_for_height(self):
#         with open('text_12.txt', 'a') as self.file:
#             self.file.write(f'{"return height"}\n{str(self._height)}\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n ')
#
#
#     def func_for_weight(self):
#         with open('text_12.txt', 'a') as self.file:
#             self.__func_for_weight_inc()
#             self.file.write(f'{"return weight"}\n{str(self.__weight)}\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n ')
#
#     def __func_for_weight_inc(self):
#         return self.__weight
#
#     @property
#     def method_weight(self):
#         with open('text_12.txt', 'a') as self.file:
#             print(self.__weight)
#             self.file.write(f'{"return weight"}\n{str(self.__weight)}\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n ')
#
#     @method_weight.setter
#     def method_weight(self, arg):
#         with open('text_12.txt', 'a') as self.file:
#             if isinstance(arg, (int, float)) and arg > 0:
#                 self.__weight = arg
#                 self.file.write(f'{"set weight"}\n{str(self.__weight)}\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n ')
#
#
#     @method_weight.deleter
#     def method_weight(self):
#         del self.__weight
#
#
#
#
#     # def text_12(self):
#     #     with open('text_12.txt', 'a') as self.file:
#     #         self.file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#
#
# a = Main(190, 100)

# LESSON 13

# class A:
#     class A:
#
#         def __init__(self, a, b):
#             self.a = a
#             self.b = b
#
#         def ch_atr_fa_cl(self, aa, bb):
#             self.a = aa
#             self.b = bb
#             print(self.a)
#             print(self.b)
#
#         def create_sets(self, **kwargs):
#             return {i for i in kwargs.keys()}
#
#     class B(A):
#         def __init__(self, c, d, e, a, b):
#             super().__init__(a, b)
#             self.c = c
#             self.d = d
#             self.e = e
#
#         def change_atr_father_class(self, *args):
#             super().ch_atr_fa_cl(*args)
#
#         def create_sets(self, **kwargs):
#             return super().create_sets(**kwargs), set(
#                 map(lambda i: tuple(i) if isinstance(i, (set, dict, list)) else i, kwargs.values()))
#
#     a = B(1, 2, 3, 4, 5)
#
#     var_1, var_2 = a.create_sets(tom=1223, bob=111111, mark=[22222222, 1], john={1, 2, 3}, nick=23232323,
#                                  colt={1: 3, 2: 4}, rod=(9, 8, 7))
#     print(var_1)
#     print(var_2)



# 14 LESSON

# class A:
#     def __init__(self, a):
#         self.a = a
#
#     def func_1(self):
#         return self.a
#
#
# class B:
#     def __init__(self, b, c):
#         self.b = b
#         self.c = c
#
#     def func_1(self):
#         return self.b, self.c
#
#     def func_2(self):
#         pass
#
#
# class C:
#     def __init__(self, d, e, f):
#         self.d = d
#         self.e = e
#         self.f = f
#
#     def func_1(self):
#         return self.d, self.e, self.f
#
#     def func_2(self):
#         pass
#
#
# class D:
#     def __init__(self, j, h, k, q):
#         self.j = j
#         self.h = h
#         self.k = k
#         self.q = q
#
#
# obj_a = A(1)
# obj_b = B(2, 3)
# obj_c = C(4, 5, 6)
# obj_d = D(7, 8, 9, 10)
#
#
# list_of_classes = [A, B, C, D]
#
# print((lambda func_1, func_2, list_of_classes:
#        ({_: _.__dict__[func_1] for _ in list_of_classes if func_1 in _.__dict__},
#         {_: _.__dict__[func_2] for _ in list_of_classes if func_2 in _.__dict__}))
#       ('func_1', 'func_2', [A, B, C, D]))
#
# # def func_gen():
# #     res = [i for i in list_of_classes if 'func_1' in i.__dict__]
# #
# #     lst_function = []
# #     for i in list_of_classes:
# #         for k, v in i.__dict__.items():
# #             if "func_1" in str(k):
# #                 lst_function.append(v)
# #
# #     dct = {i: j for i, j in zip(res, lst_function)}
# #
# #     res_2 = [i for i in list_of_classes if 'func_2' in i.__dict__]
# #
# #     lst_function_2 = []
# #     for i in list_of_classes:
# #         for k, v in i.__dict__.items():
# #             if "func_2" in str(k):
# #                 lst_function_2.append(v)
# #
# #     dct_1 = {k: m for k, m in zip(res_2, lst_function_2)}
# #
# #     return dct, dct_1
# #
# # sss = func_gen()
# # print(sss)




#15 LESSON




































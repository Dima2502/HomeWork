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

# print((lambda func_1, func_2, list_of_classes:
#        ({_: _.__dict__[func_1] for _ in list_of_classes if func_1 in _.__dict__},
#         {_: _.__dict__[func_2] for _ in list_of_classes if func_2 in _.__dict__}))
#       ('func_1', 'func_2', [A, B, C, D]))

# def func_gen():
#     res = [i for i in list_of_classes if 'func_1' in i.__dict__]
#
#     lst_function = []
#     for i in list_of_classes:
#         for k, v in i.__dict__.items():
#             if "func_1" in str(k):
#                 lst_function.append(v)
#
#     dct = {i: j for i, j in zip(res, lst_function)}
#
#     res_2 = [i for i in list_of_classes if 'func_2' in i.__dict__]
#
#     lst_function_2 = []
#     for i in list_of_classes:
#         for k, v in i.__dict__.items():
#             if "func_2" in str(k):
#                 lst_function_2.append(v)
#
#     dct_1 = {k: m for k, m in zip(res_2, lst_function_2)}
#
#     return dct, dct_1
#
# sss = func_gen()
# print(sss)


# def count_sheep(n):
#     return ''.join(f"{i} sheep..." for i in range(1, n + 1))
# m = count_sheep(20)
# print(m)


# def comp_fex_string_int(s):
#     n = int(s, 16)
#     return n
# m = comp_fex_string_int('deadbeef')
# print(m)


# def count_positives_sum_negatives(arr):
#
#     pos = sum(1 for x in arr if x > 0)
#     neg = sum(x for x in arr if x < 0)
#     return [pos, neg] if len(arr) else []
#
# n = count_positives_sum_negatives([1, 2, 6, 7, -6, -4, 9, -3, 0, 0])
# print(n)

# def count_positives_sum_negatives(arr):
#     return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0)] if arr else []

# def rev(a):
#         print(a[::-1])
# rev('anastasiia')

# def grow(arr):
#
#     n = 1
#     for el in arr:
#         n *= el
#     return n
#
# print(grow([10, 20, 30, 40]))


# class A:
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def str_check(*args):
#         for elem in args:
#             if elem.isalpha() and type(elem) == str:
#                 return elem
#             else:
#                 raise TypeError
#
#
# a = A('bob')
# a = A(A.str_check('djkcnskjcm9776', 'ksfjhbv986', 'jsdbvi8775'))
# print(a.name)


# class B:
#
#     dct = {('bmw', 'toyota'): ['audi', 13], 'merc': ['vw', 15]}
#     lst_obj = []
#
#     def __init__(self, lst_attr=None):
#         self.lst_attr = lst_attr
#
#     @classmethod
#     def method(cls):
#         for key, value in cls.dct.items():
#             if isinstance(key, str):
#                 cls.lst_obj.append(key)
#                 for i in value:
#                     if isinstance(i, str):
#                         cls.lst_obj.append(i)
#                 return cls.lst_obj
#
# obj = B()
# print(obj.method())

# class PositiveNumber:
#     def __get__(self, instance, owner):
#         return getattr(instance, self.s_name)
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError
#         setattr(instance, self.s_name, value)
#
#     def __set_name__(self, owner, name):
#         self.s_name = '_' + name
#
#
# class Order:
#
#     amount = PositiveNumber()
#     cost = PositiveNumber()
#
#     def __init__(self, amount, cost):
#         # self.name = 'Bob'
#         # self.shop = '#21'
#         # self.product = 'Milk'
#         self.amount = amount
#         self.cost = cost
#
#     def total(self):
#         return self.amount * self.cost
#
# order = Order(40, 2)
#
# print(order.total())
#
#
# print(order.__dict__)


# class Integer:
#     def __get__(self, instance, owner):
#         return getattr(instance, self.var_name)
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError
#         setattr(instance, self.var_name, value)
#     def __set_name__(self, owner, name):
#         self.var_name = '_' + name


# class PosInt:
#     def __set_name__(self, owner, name):
#         self.i_name = '_' + name
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError
#         setattr(instance, self.i_name, value)
#     def __get__(self, instance, owner):
#         return getattr(instance, self.i_name)
#
#
# class Coord:
#     x = PosInt()
#     y = PosInt()
#     z = PosInt()
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def sqaue(self):
#         return self.x * self.y * self.z
#
# cube = Coord(4, 5, 2)
# cube.x = 20
# cube.y = 2
# cube.z = 1
# print(cube.sqaue())




# ПАТЕРНОЕ "МОНОСОСТОЯНІЕ"
# class ThreadData:
#     __shared_attrs = {
#         'name': 'thread_1',
#         'data': {},
#         'id': 1
#     }
#     def __init__(self):
#         self.__dict__ = self.__shared_attrs
#
# th1 = ThreadData()
# th2 = ThreadData()
# th3 = ThreadData()
#
# th3.data = {1: 3, 4: 6}
# th1.name = 'lkjsjkncijniwnciwjcniwjcskdj'
# th2.id = 3
# th1.new_attr = 'new attrrrrr'
# print(th1.__dict__)
# print(th2.__dict__)
# print(th3.__dict__)



#PROPERTY

# from string import ascii_letters
#
# class Person:
#     S_RUS = ''
#     S_RUS_UPPER = S_RUS.upper()
#     def __init__(self, fio, old, ps, weight):
#
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_ps(ps)
#         # self.verify_weight(weight)
#
#         self.__fio = fio.split()
#         self.old = old
#         self.ps = ps
#         self.weight = weight
#
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if type(fio) != str:
#             raise TypeError('ФИО должно быть строкой')
#
#         f = fio.split()
#         if len(fio) != 3:
#             raise TypeError('ФИО должно быть из 3 слов')
#
#         letters = ascii_letters + cls.S_RUS +cls.S_RUS_UPPER
#         for s in f:
#             if len(s) < 1:
#                 raise TypeError('В ФИО должен быть хотя бы один символ')
#             if len(s.strip(letters)) != 0:
#                 raise TypeError('ФИО можно использовать только буквенные символы и дефис')
#     @classmethod
#     def verify_old(cls, old):
#         if type(old) != int or 20 < old > 120:
#             raise TypeError('возраст должен быть целим числом от 20 дод 120 лет')
#
#     @classmethod
#     def verify_weight(cls, w):
#         if type(w) != float or w < 40:
#             raise TypeError('вec должен быть вещественным числом от 40 кг')
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if type(ps) != str:
#             raise TypeError('должна быть строкой')
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError('должна быть из двух частей')
#
#         for i in s:
#             if not i.isdigit():
#                 raise TypeError('должны быть только цифры')
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def ps(self):
#         return self.__ps
#
#     @ps.setter
#     def ps(self, ps):
#         self.verify_ps(ps)
#         self.__ps = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
#
# p = Person('Bob', 50, '3433 121212', 40.4)
# p.old = 40
# print(p.__dict__)

# def chane_sum(number):
#     result = number
#
#     def wrapper(number2=None):
#         nonlocal result
#         if number2 is None:
#             return result
#         result += number2
#         return wrapper
#     return wrapper
#
# print(chane_sum(9)(3)(1)())

# class PosNumber:
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('only positive number')
#         setattr(instance, self.name, value)
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#
# class Goods:
#
#     amount = PosNumber()
#     price = PosNumber()
#
#     def __init__(self, good, amount, price):
#         self.good = good
#         self.amount = amount
#         self.price = price
#
# p = Goods('milk', 12, 100)
# print(p.__dict__)
# p.price = 20
# p.price = 30
# print(p.__dict__)


# class B:
#     dct = {('bmw', 'toyota'): ['audi', 13], 'merc': ['vw', 15], 'a': [1, 'pyton']}
#
#     def __init__(self, *args):
#         self.args = args
#
#     @classmethod
#     def method(cls):
#         dct_1 = {}
#         lst_1 = []
#         lst_2 = []
#         for key in cls.dct.keys():
#             if isinstance(key, str):
#                 lst_1.append(key)
#                 for i in cls.dct.values():
#                     if isinstance(i, str):
#                         lst_2.append(i)
#                         dct_1 = {key: i for key, i in zip(lst_1, lst_2)}
#                         return dct_1
#
#
# obj = B()
# t = obj.method()
# print(t)



class B:
    dct = {('bmw', 'toyota'): ['audi', 13], 'merc': ['vw', 15], 'a': [1, 'pyton'], 'opel': ['motor', 34], '23': ['32', 111]}

    def __init__(self, *args):
        self.args = args

    @classmethod
    def method(cls):
        dct_1 = {}
        lst_1 = []
        lst_2 = []
        for key, value in cls.dct.items():
            if isinstance(key, str):
                lst_1.append(key)


                for i in value:
                    if isinstance(i, str):
                        lst_2.append(i)
                        dct_1 = {key: i for key, i in zip(lst_1, lst_2)}
        return cls(dct_1)


obj = B.method()
print(obj.__dict__)

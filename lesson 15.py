# #15.1 LESSON
# class A:
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def str_check(*args):
#         for elem in args:
#             if isinstance(elem, str) and elem.isalpha():
#                 return elem
#             continue
#         raise TypeError
#
#
# a = A('bob')
#
# b = A(A.str_check(1, 'test1', 'John', 'Mark'))
# print(b.name)


#15.2 LESSON

class B:
    dct = {('bmw', 'toyota'): ['audi', 13], 'merc': ['vw', 15], 'a': [1, 'pyton'], 'opel': [34, 'motor']}

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







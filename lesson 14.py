class A:
    def __init__(self, a):
        self.a = a

    def func_1(self):
        return self.a


class B:
    def __init__(self, b, c):
        self.b = b
        self.c = c

    def func_1(self):
        return self.b, self.c

    def func_2(self):
        pass


class C:
    def __init__(self, d, e, f):
        self.d = d
        self.e = e
        self.f = f

    def func_1(self):
        return self.d, self.e, self.f

    def func_2(self):
        pass


class D:
    def __init__(self, j, h, k, q):
        self.j = j
        self.h = h
        self.k = k
        self.q = q


obj_a = A(1)
obj_b = B(2, 3)
obj_c = C(4, 5, 6)
obj_d = D(7, 8, 9, 10)


list_of_classes = [A, B, C, D]


def func_gen():
    res = list(i for i in list_of_classes if 'func_1' in i.__dict__)

    lst_function = []
    for i in list_of_classes:
        for k, v in i.__dict__.items():
            if "func_1" in str(k):
                lst_function.append(v)

    dct = {i: j for i, j in zip(res, lst_function)}

    res_2 = [i for i in list_of_classes if 'func_2' in i.__dict__]

    lst_function_2 = []
    for i in list_of_classes:
        for k, v in i.__dict__.items():
            if "func_2" in str(k):
                lst_function_2.append(v)

    dct_1 = {k: m for k, m in zip(res_2, lst_function_2)}

    return dct, dct_1


sss = func_gen()
print(sss)


# print((lambda func_1, func_2, list_of_classes:
#        ({_: _.__dict__[func_1] for _ in list_of_classes if func_1 in _.__dict__},
#         {_: _.__dict__[func_2] for _ in list_of_classes if func_2 in _.__dict__}))
#       ('method', 'for_dct', [A, B, C, D]))
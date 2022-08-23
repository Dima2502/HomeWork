class A:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ch_atr_fa_cl(self, aa, bb):
        self.a = aa
        self.b = bb
        print(self.a)
        print(self.b)

    def create_sets(self, **kwargs):
        return {i for i in kwargs.keys()}


class B(A):
    def __init__(self, c, d, e, a, b):
        super().__init__(a, b)
        self.c = c
        self.d = d
        self.e = e

    def change_atr_father_class(self, *args):
        super().ch_atr_fa_cl(*args)

    def create_sets(self, **kwargs):
        return super().create_sets(**kwargs), set(map(lambda i: tuple(i) if isinstance(i, (set, dict, list)) else i, kwargs.values()))


a = B(1, 2, 3, 4, 5)

var_1, var_2 = a.create_sets(tom= 1223, bob= 111111, mark= [22222222, 1], john= {1, 2, 3}, nick= 23232323, colt= {1: 3, 2: 4}, rod= (9, 8, 7))
print(var_1)
print(var_2)



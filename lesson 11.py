# LESSON 11

class Main:
    dct = {12: 249, 'skd': 'sj', 'ks': 242, 933: 'las'}
    tup = (1, 2, 5, 1, 2, 2, 'jd', 'ka')

    def __init__(self):

        access = input('user or admin:  ')
        if access == 'user':
            print(self.dct)
            print(self.tup)
        elif access == 'admin':
            # log_pass = input('enter login and password: ').split()
            # if log_pass[0] == 'admin' and log_pass[1] == '1111':
                self.method()


    def method(self):
        print(f'1. dict_items\n2. dict_keys\n3. dict_pop\n4. dict_values\n5. dict_copy\n6. dict_clear\n7. dict_update\n'
              f'8. dict_fromkeys\n9. dict_get\n10. dict_popitem\n11. dict_setdefault\n12. tuple_index\n13. tuple_count\n14. tuple_add_elem')
        method = int(input('choose method:  '))
        if method == 1:
            self.dict_items()
        elif method == 2:
            self.dict_keys()
        elif method == 3:
            self.dict_pop()
        elif method == 4:
            self.dict_values()
        elif method == 5:
            self.dict_copy()
        elif method == 6:
            self.dict_clear()
        elif method == 7:
            self.dict_update()
        elif method == 8:
            self.dict_fromkeys()
        elif method == 9:
            self.dict_get()
        elif method == 10:
            self.dict_popitem()
        elif method == 11:
            self.dict_setdefault()
        elif method == 12:
            self.tuple_index()
        elif method == 13:
            self.tuple_count()
        elif method == 14:
            self.tuple_add_elem()

    def cont_ex(self):
        i = int(input('continue(1) or exit(2): '))
        if i == 1:
            self.method()
        elif i == 2:
            exit()


    def type_arg(self):
        self.type_arg = input('enter type arg int, str, list, tuple, dict, set: ')
        if self.type_arg == 'int':
            self.arg = int(input('enter arg: '))
        elif self.type_arg == 'str':
            self.arg = input('enter arg: ')
        elif self.type_arg == 'list':
            self.arg = list(input('enter arg:').split())
        elif self.type_arg == 'tuple':
            self.arg = tuple(input('enter arg: ').split())
        elif self.type_arg == 'dict':
            self.a = int(input('type key int(1) or str(2): '))
            if self.a == 1:
                self.key = int(input('enter key: '))
            elif self.a == 2:
                self.key = input('enter key: ')
            self.b = int(input('type value int(1) or str(2): '))
            if self.b == 1:
                self.value = int(input('enter value: '))
            elif self.b == 2:
                self.value = input('enter value: ')

            self.arg = {}
            self.arg[self.key] = self.value
        elif self.type_arg == 'set':
            self.arg = set(input('enter set: ').split())


    def dict_items(self):
        print(Main.dct)
        for i in Main.dct.items():
            print(i)
        self.cont_ex()

    def dict_keys(self):
        print(Main.dct)
        for i in Main.dct:
            print(i)
        self.cont_ex()

    def dict_pop(self):
        print(Main.dct)
        self.type_arg()
        e = Main.dct.pop(self.arg)
        print(Main.dct)
        self.cont_ex()

    def dict_values(self):
        print(Main.dct)
        for i in Main.dct.values():
            print(i)
        self.cont_ex()

    def dict_copy(self):
        print(Main.dct)
        e = input('enter new dct: ')
        s = Main.dct.copy()
        print(f'{e} = {Main.dct.copy()}')
        self.cont_ex()

    def dict_clear(self):
        print(Main.dct)
        Main.dct.clear()
        print(Main.dct)
        self.cont_ex()

    def dict_update(self):
        print(Main.dct)
        self.a = int(input('type key int(1) or str(2): '))
        if self.a == 1:
            self.key = int(input('enter key: '))
        elif self.a == 2:
            self.key = input('enter key: ')
        self.b = int(input('type value int(1) or str(2): '))
        if self.b == 1:
            self.value = int(input('enter value: '))
        elif self.b == 2:
            self.value = input('enter value: ')

        self.arg = {}
        self.arg[self.key] = self.value
        if self.key not in Main.dct.keys():
            Main.dct.update(self.arg)
            print(Main.dct)
        else:
            print('this key already in dct')
            self.c = int(input('wanna change key(1) or rewrite value(2)'))
            if self.c == 1:
                self.dict_update()
            else:
                Main.dct.update(self.arg)
                print(Main.dct)
        self.cont_ex()


    def dict_fromkeys(self):
        print(Main.dct)
        self.key = list(input('enter keys: ').split())
        print(self.key)
        self.e = Main.dct.fromkeys(self.key)
        print(self.e)
        self.aaa = int(input('wanna add value: yes(1) or no(2): '))
        if self.aaa == 1:
            self.b = int(input('type value int(1) or str(2): '))
            if self.b == 1:
                self.value = int(input('enter value: '))
            elif self.b == 2:
                self.value = input('enter value: ')
            n = self.e.fromkeys(self.key, self.value)
            print(n)
        else:
            exit()
        self.cont_ex()

    def dict_get(self):
        print(Main.dct)
        self.type_arg()
        e = Main.dct.get(self.arg)
        print(f'value {e}')
        self.cont_ex()

    def dict_popitem(self):
        print(Main.dct)
        print(Main.dct.popitem())
        self.cont_ex()

    def dict_setdefault(self):
        print(Main.dct)
        self.a = int(input('wanna: 1.return value of key; 2.add new key; 3.add new item: '))
        if self.a == 1:
            self.aa = int(input('type key int(1) or str(2): '))
            if self.aa == 1:
                self.b = int(input('enter key: '))
            elif self.aa == 2:
                self.b = input('enter key: ')
            print(Main.dct.setdefault(self.b))
        elif self.a == 2:
            self.aa = int(input('type key int(1) or str(2): '))
            if self.aa == 1:
                self.b = int(input('enter key: '))
            elif self.aa == 2:
                self.b = input('enter key: ')
            Main.dct.setdefault(self.b)
            print(Main.dct)
        elif self.a == 3:
            self.aa = int(input('type key int(1) or str(2): '))
            if self.aa == 1:
                self.b = int(input('enter key: '))
            elif self.aa == 2:
                self.b = input('enter key: ')
            self.c = int(input('type value int(1) or str(2): '))
            if self.c == 1:
                self.bb = int(input('enter value: '))
            elif self.c == 2:
                self.bb = input('enter value: ')
            Main.dct.setdefault(self.b, self.bb)
            print(Main.dct)
        self.cont_ex()


    def tuple_index(self):
        print(Main.tup)
        self.a = int(input('type element of tuple int(1) or str(2): '))
        if self.a == 1:
            self.b = int(input('enter element: '))
        elif self.a == 2:
            self.b = input('enter element: ')
        print(Main.tup.index(self.b))
        self.cont_ex()

    def tuple_count(self):
        print(Main.tup)
        self.a = int(input('type element of tuple int(1) or str(2): '))
        if self.a == 1:
            self.b = int(input('enter element: '))
        elif self.a == 2:
            self.b = input('enter element: ')
        e = Main.tup.count(self.b)
        print(e)
        self.cont_ex()

    def tuple_add_elem(self):
        print(Main.tup)
        self.type_arg()
        # self.a = int(input('type add element to tuple int(1) or str(2): '))
        # if self.a == 1:
        #     self.b = int(input('enter element: '))
        # elif self.a == 2:
        #     self.b = input('enter element: ')
        e = list(Main.tup)
        e.append(self.arg)
        print(tuple(e))
        self.cont_ex()


a = Main()
print(a.dict_keys())



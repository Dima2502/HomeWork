from datetime import datetime

class Main:
    name = 'Tom'

    def __init__(self, height, weight):
        self._height = height
        self.__weight = weight


    def _func_for_height(self):
        with open('text_12.txt', 'a') as self.file:
            self.file.write(f'{"return height"}\n{str(self._height)}\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n ')


    def func_for_weight(self):
        with open('text_12.txt', 'a') as self.file:
            self.__func_for_weight_inc()
            self.file.write(f'{"return weight"}\n{str(self.__weight)}\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n ')

    def __func_for_weight_inc(self):
        return self.__weight

    @property
    def method_weight(self):
        with open('text_12.txt', 'a') as self.file:
            print(self.__weight)
            self.file.write(f'{"return weight"}\n{str(self.__weight)}\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n ')

    @method_weight.setter
    def method_weight(self, arg):
        with open('text_12.txt', 'a') as self.file:
            if isinstance(arg, (int, float)) and arg > 0:
                self.__weight = arg
                self.file.write(f'{"set weight"}\n{str(self.__weight)}\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n ')


    @method_weight.deleter
    def method_weight(self):
        del self.__weight




    # def text_12(self):
    #     with open('text_12.txt', 'a') as self.file:
    #         self.file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


a = Main(190, 100)









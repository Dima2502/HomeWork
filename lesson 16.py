from datetime import datetime

import requests
from bs4 import BeautifulSoup as Bs


class Enter:
    """при створені об'єкту передається пін та баланс"""
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    @property
    def pin(self):
        return self.__pin

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance


class Operation(Enter):
    """"зарахування та зняття коштів з рахунку"""
    def __init__(self, pin, balance):
        super().__init__(pin, balance)

    def deposit(self):
        with open('text_16.txt', 'a') as self.file:
            amount = float(input('enter amount deposit: '))
            self.balance += amount

            self.file.write(f'{datetime.now().strftime("%H:%M:%S %Y-%m-%d")} : {"deposit"}\n')
            print('Balance updated:', self.balance)

    def withdraw(self):
        with open('text_16.txt', 'a') as self.file:
            amount = float(input('enter amount withdraw: '))
            if amount > self.balance:
                raise ValueError('balance less amount withdraw, your balance is', self.balance)
            else:
                self.balance -= amount
                print('Balance updated: ', round(self.balance, 2))
                self.file.write(f'{datetime.now().strftime("%H:%M:%S %Y-%m-%d")} : {"withdraw"}\n')


class SetUSDAccount:
    def __set_name__(self, owner, name):
        self.i_name = '_' + name

    def __set__(self, instance, value):
        setattr(instance, self.i_name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.i_name)


class Exchange(Operation):
    """дізнатися курс долара, купити долар, продати долар"""
    usd_account = SetUSDAccount()

    def __init__(self, pin, balance):
        super().__init__(pin, balance)
        self.main()

    def course_currency(self):
        with open('text_16.txt', 'a') as self.file:
            url = 'https://kurs.com.ua/'
            response = requests.get(url)
            html = Bs(response.content, 'html.parser')
            for i in html.select('#main_table'):
                self.buy = float(i.select('.course')[0].text[0:5])
                self.sell = float(i.select('.course')[1].text[0:5])
                print(f'buy = {self.buy}, sell = {self.sell}')
            self.file.write(f'{datetime.now().strftime("%H:%M:%S %Y-%m-%d")} : {"view course currency"}\n')

    def exchange_buy(self):
        url = 'https://kurs.com.ua/'
        response = requests.get(url)
        html = Bs(response.content, 'html.parser')
        for i in html.select('#main_table'):
            self.sell = float(i.select('.course')[1].text[0:5])
        with open('text_16.txt', 'a') as self.file:
            amount = float(input('enter amount for buy USD: '))
            if amount > self.balance:
                raise ValueError('amount has to <= balance')
            else:
                with open('text_16_USD.txt', 'a') as self.file_USD:
                    self.usd_account = round(amount / self.sell, 2)
                    self.balance = round(self.balance - amount, 2)
                    self.file_USD.write(f'Balance USD: {self.usd_account} : {datetime.now().strftime("%H:%M:%S %Y-%m-%d")}\n')
                    print('Balance updated: ', self.balance)
                    print(f'Balance USD: {self.usd_account}')
            self.file.write(f'{datetime.now().strftime("%H:%M:%S %Y-%m-%d")} : {"currency buy"}\n')

    def exchange_sell(self):
        url = 'https://kurs.com.ua/'
        response = requests.get(url)
        html = Bs(response.content, 'html.parser')
        for i in html.select('#main_table'):
            self.buy = float(i.select('.course')[0].text[0:5])
        with open('text_16.txt', 'a') as self.file:
            amount = float(input('enter USD for sell: '))
            if amount > self.usd_account:
                raise ValueError('amount has to <= usd account')
            else:
                with open('text_16_USD.txt', 'a') as self.file_USD:
                    self.balance += (self.buy * amount)
                    self.usd_account = round(self.usd_account - amount, 2)
                    self.file_USD.write(f'Balance USD: {self.usd_account} : {datetime.now().strftime("%H:%M:%S %Y-%m-%d")}\n')
                    print('Balance updated: ', round(self.balance, 2))
                    print(f'Balance USD update: {self.usd_account}')
            self.file.write(f'{datetime.now().strftime("%H:%M:%S %Y-%m-%d")} : {"currency sell"}\n')

    def main(self):
        while True:
            number_operation = int(input('Choose operation:\n1: deposit\n2: withdraw\n3: currency course\n4: currency buy\n5: currency sell\n6: exit\n'))
            if number_operation == 1:
                self.deposit()
            elif number_operation == 2:
                self.withdraw()
            elif number_operation == 3:
                self.course_currency()
            elif number_operation == 4:
                self.exchange_buy()
            elif number_operation == 5:
                self.exchange_sell()
            elif number_operation == 6:
                print('Thanks for visit')
                break


a = Exchange(111, 1000)





















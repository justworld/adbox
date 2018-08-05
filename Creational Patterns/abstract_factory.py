# coding: utf-8
"""
抽象工厂模式
"""


class Phone:
    def show(self):
        raise Exception('The method is not implemented')


class Computer:
    def show(self):
        raise Exception('The method is not implemented')


class Company:
    def __init__(self):
        self.phone = Phone()
        self.computer = Computer()

    def show(self):
        self.phone.show()
        self.computer.show()


class ApplePhone(Phone):
    def show(self):
        print 'Apple phone'


class AppleComputer(Computer):
    def show(self):
        print 'Apple pc'


class AppleCompany(Company):
    def __init__(self):
        self.phone = ApplePhone()
        self.computer = AppleComputer()


class MicrosoftPhone(Phone):
    def show(self):
        print 'Microsoft phone'


class MicrosoftComputer(Computer):
    def show(self):
        print 'Microsoft pc'


class MicrosoftleCompany(Company):
    def __init__(self):
        self.phone = MicrosoftPhone()
        self.computer = MicrosoftComputer()


def get_company(name):
    if name == 'Apple':
        return AppleCompany()
    if name == 'Microsoft':
        return MicrosoftleCompany()
    return Company()


if __name__ == '__main__':
    get_company('Apple').show()

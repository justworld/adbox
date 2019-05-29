# coding: utf-8
"""
代理模式
"""


class Subject(object):
    def request(self):
        raise NotImplementedError()


class RealSubject(Subject):
    def request(self):
        print "真实请求"


class Proxy(Subject):
    def __init__(self):
        self.real_subject = RealSubject()

    def request(self):
        self.real_subject.request()


if __name__ == '__main__':
    Proxy().request()

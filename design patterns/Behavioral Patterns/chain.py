# coding: utf-8
"""
责任链模式
"""


class PlainObject:
    def __init__(self):
        self.list = []

    def show(self):
        print ','.join(self.list)


class BaseMiddleware(object):
    def __init__(self, next=None):
        self.next = next

    def handler(self, request):
        if self.next:
            self.next.handler(request)


class MiddlewareOne(BaseMiddleware):
    def handler(self, request):
        request.list.append('handler one')
        super(MiddlewareOne, self).handler(request)


class MiddlewareTwo(BaseMiddleware):
    def handler(self, request):
        request.list.append('handler two')
        super(MiddlewareTwo, self).handler(request)


def create_middleware_chain(middlewares):
    if not middlewares:
        return None

    length = len(middlewares)
    if length == 0:
        return None

    for i in range(length-1):
        middlewares[i].next = middlewares[i+1]

    return middlewares[0]


if __name__ == '__main__':
    chain = create_middleware_chain([MiddlewareOne(), MiddlewareTwo()])
    plain = PlainObject()
    if chain:
        chain.handler(plain)
    plain.show()

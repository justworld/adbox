# coding: utf-8

def wraper(fun):
    def inner():
        print 'this is decorator'
        result = fun()
        print 'end now'
        return result
    return inner

def hello():
    print 'hello'
    return 'world'

if __name__ == '__main__':
    f = wraper(hello)
    print f()
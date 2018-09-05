# coding: utf-8
"""
观察者模式，参考消息队列中间件
"""


class Topic(object):
    def __init__(self):
        self.obs = []

    def attach(self, ob):
        self.obs.append(ob)

    def detach(self, ob):
        self.obs.remove(ob)

    def notify(self):
        for ob in self.obs:
            ob.update()


class Observer(object):
    def __init__(self, topic):
        self.topic = topic

    def update(self):
        raise NotImplementedError()


class Observer1(Observer):
    def update(self):
        print 'change!'


if __name__ == '__main__':
    topic = Topic()
    topic.attach(Observer1(topic))
    topic.notify()

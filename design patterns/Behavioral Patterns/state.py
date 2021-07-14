"""
状态模式
"""


class State(object):
    def show(self):
        print(self.name)


class StateOne(State):
    def __init__(self, host):
        self.name = "One"


class StateTwo(State):
    def __init__(self, host):
        self.name = "Two"


class Host(object):
    def __init__(self):
        self.state_list = [StateOne(self), StateTwo(self)]
        self.state = 0
        self.state_num = len(self.state_list)

    def toggle(self):
        state = self.state + 1
        self.state = state % self.state_num

    def show(self):
        self.state_list[self.state].show()


if __name__ == '__main__':
    host = Host()
    actions = [host.show] + [host.toggle]
    actions = actions * 4
    for action in actions:
        action()

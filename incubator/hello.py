class Hello(object):

    def __init__(self, name):
        self.name = name

    def say(self):
        return 'Hello %s' % self.name

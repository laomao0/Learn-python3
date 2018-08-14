class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('parent')

    def bar(self, message):
        print("{} from parent".format(message))


class FooChild(FooParent):
    def __init__(self):
        super(FooChild, self).__init__()
        print("child")

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar function')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')

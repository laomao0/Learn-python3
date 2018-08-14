class Parent(object):

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def altered(self):
        print("CHILD, Before Parent altered()")
        super(Child, self).altered()
        print("CHILD, After parent altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()
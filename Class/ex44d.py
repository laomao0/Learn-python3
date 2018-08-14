class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def override(self):
        print("Child override")

    def altered(self):
        print("Child, before parent altered()")
        super(Child, self).altered()  # use super to get the parent function
        print("Child, after parent altered()")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()  # the inheritance class implict the original class's function

dad.override()
son.override()  # the inheritance class can override original class function

dad.altered()
son.altered()   # use super function to get the original class function

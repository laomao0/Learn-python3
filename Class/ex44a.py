# Actions on the child imply an action on the parent
# 在隐式继承中 implicit inheritance中
# 父类的隐式继承 会默认传给子类
# 所以即使child中没有定义implict函数，子类函数在调用的时候会自动调用父类的implict函数
# 注意这里的 implict不是关键词，只是一个函数的名称


class Parent(object):

    def implict():
        print("Parent Implict( )")


class Child(Parent):
    pass


# 在这里我们研究下python类语法中的三种方法，实例方法，静态方法，类方法
class Foo(object):
    """ 类的三种方法语法形式"""

    # 实例方法只能被实例对象调用
    def instance_method(self):
        print("是类{}的实例方法，只能被实例对象调用".format(Foo))

    # 静态方法 可以被类或类的实例对象调用
    @staticmethod
    def static_methon():
        print("静态方法")

    # 静态方法 可以被类或类的实例对象调用
    @classmethod
    def class_method(cls):
        print("类方法")


class people(object):
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("{} speak: I am {} age old, weight {} ".format(self.name, self.age, self.__weight))


dad = Parent()
son = Child()

dad.implict()
son.implict()

foo = Foo()
foo.instance_method()
foo.static_methon()
foo.class_method()
print('-----------')
Foo.static_methon()
Foo.class_method()

p = people('runoob', 10, 30)
p.speak()
print(p.age)
print(p.name)  # p.__weight是不能访问的







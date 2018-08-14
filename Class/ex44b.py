# override explicitly
# 重写
# 关于有些方法是隐式调用的问题原因在于有时候你想让子类有不同的表现。这时你想重写子类中的方法且有效的覆盖父类中的方法。要做到这一点，你只需要在子类中定义一个同名的方法就行


class Parent(object):

    def override(self):
        print("PARENT override()")


class Child(Parent):

    def override(self):
        print("CHILD override()")


dad = Parent()
son = Child()

dad.override()  # 调用同名的函数
son.override()

from decimal import Decimal as D
from decimal import getcontext
from fractions import  Fraction as F

print("I will now count my chickens:")

print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater ot equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

# python 中的变量不需要声明。 每个变量在使用前都必须赋值，变量赋值之后改变量才会被创建。
# 在python中，变量就是变量，它没有类型，我们所说的"类型"是指变量所指的内存中对象的类型。
print(50*2)
print(1/500)
print(4*3-1)
print(3.14*2*200)
print(1.0/20)

# The following expression are more complicated calculations.
# Ignore them if you haven't learned anything about each type.

# decimal 十进制消暑
# Python提供了decimal模块用于十进制数学计算，它具有以下特点：
# 1. 提供十进制数据类型，并且存储为十进制数序列
# 2. 有界精度：用于存储数字的位数是固定的，可以通过decimal.getcontext().prec = x来设定
# 3. 浮点：十进制小数点的位置不固定（但位数是固定的）

getcontext()  #
getcontext().prec = 6
print(D(9876)+D(54321.012345678987654321))

# fractions 分数
# [sign] numerator ['/' denominator]
print(F(1, 3))
print(F(4, 6))
print(3 * F(1, 3))

# complex 复数
print(3-4j)
print(3-4J)
print(complex(3, -4))
print(3 + 1J * 3j)





# Python()函数接受一个标准输入数据，返回为string类型

print("How old are you?", end=' ')
age = input()
# age = int(input())

print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy")
print("So, you're {} old, {} tall and {} heavy".format(age, height, weight))

print("So, you're %s old, %s tall and %s heavy" % (age, height, weight))

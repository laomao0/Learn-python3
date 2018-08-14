# close 关闭文件
# read  读取文件内容
# readline 读取一行文件
# truncate 清空文件
# write('stuff') 向文件写
# seek(0) 讲读写地址移动带文件起始处

# from sys import argv

# script, filename = argv

filename = 'new_file.txt'

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w+')  # 以读写的方式打开这个文件，如果该文件已存在则打开文件，即原有内容会被删除。如果文件不存在，则创建新的文件

# w+会自动清空原有的内容，所以truncate是不必要的
print("Truncating the file. Goodbye!")
target.truncate()  # Empties the file. Watch out if you care about the file


print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

total_line = [line1, line2, line3]  # 讲三个str组合成List ,List是[], tuple是() tuple是不可变的list，一旦被创立就不能改变

print("I'm going to write there to the file.")

target.write(line1)  # 向文件写入line1
target.write("\n")  # 向文件写入换行符，即从下一行开始写
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


# 可以使用一个 .write函数，写入函数
target.write("{0}\n{1}\n{2}\n".format(line1, line2, line3))

# 可以使用循环 写入文件
print("We can also use list to write")

for i in total_line:
    target.write(str(i) + '\n')


target.seek(0)
content = target.read()
print("Last time, what we write into the txt is ")
print(content)

print("And finally, we close it.")
target.close()



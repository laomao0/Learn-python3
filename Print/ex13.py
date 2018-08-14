from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# If they give your script inputs on the command line, then you use argv
# If you want them to input using the keyboard while the script is running, then use input().

# 在Terminal中输入  python3.6 ex13.py first 2nd 3rd 运行

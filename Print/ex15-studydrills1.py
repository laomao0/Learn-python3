# import argv variables from sys submodule
from sys import argv

# get the argv variables
script, filename = argv

# open a file
txt = open(filename)

# print the file name
print(f"Here's your file {filename}")
# print all the contents of the file
print(txt.read())

# close the file
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# close
# read
# readline
# truncate
# write('stuff')
# seek(0)

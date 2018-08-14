from sys import argv

script, first_name, second_name = argv

my_name = input("What's your name? ")
my_age = input("How old are you? ")
my_height = input("How tall are you? ")

# python 在（） {} []中不需要添加换行符 \
print("The script name is {0}, and the first_name is {1}, the second_name is {2}, and "
      "your name is {3}, you are {4} ages old and your height is {5}.".format(script, first_name, second_name,
                                                                              my_name, my_age, my_height))

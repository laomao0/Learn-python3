types_of_people = 10

# 使用f" { x }" 与 "  {0}".format(x) 最终形成的string是一样的
x = f"There are {types_of_people} types of people."
x1 = "There are {0} types of people.".format(types_of_people)

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")  # need to print out single-quotes

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))  # use {} to indicate the f style

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

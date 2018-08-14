my_name = 'Zed A. Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}")

# Print的格式化输出，与C语言的printf类似
print("Let's talk about %s" % my_name)
print("He's %d inches tall." % my_height)
print("He\'s %d pounds heavy" % my_weight)
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee" % my_teeth)

# 利用str.format() 来输出
print("Let's talk about {0}".format(my_name))
print("He's {0} inches tall".format(my_height))
print("He's {0} pounds heavy".format(my_weight))
print("He's got {0} eyes and {1} hair".format(my_eyes, my_hair))

# try more format characters
my_greeting = "Hello,\t"  # \t是string里面的制表符
my_first_name = 'wang'
my_last_name = 'shen'
my_age = 24
print("%r my name is %s %s, and I'm %d years old." % (my_greeting, my_first_name, my_last_name, my_age))

inches_per_centimeters = 2.54
pounds_per_kilo = 0.4535

print("He's %f centimeters tall" % (inches_per_centimeters * my_height))
print("He's %f kilos heavy" % (pounds_per_kilo * my_weight))


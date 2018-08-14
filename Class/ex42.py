# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


# Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has a name
        self.name = name


# cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has a name
        self.name = name


# person is-a object
class Person(object):

    def __init__(self, name):
        # person has-a name
        self.name = name  # 这些类的对象是公有的，所以在类外直接可以通过累的对象访问

        # person has-a pet of some kind
        self.pet = None


# Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        # run the __init__ method of a parent class reliably
        super(Employee, self).__init__(name)  # 回到父类，并给父类对象的成员变量赋值 parent class
        # employee has a salary
        self.salary = salary


# Fish is a object
class Fish(object):
    pass


# Salmon is-a fish
class Salmon(Fish):
    pass


# Halibut is-a fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a cat
santan = Cat("Santan")

# mary is-a person
mary = Person("Mary")

# mary's pet is satan
mary.pet = santan

# frank is a employee, his salary is 120000
frank = Employee("Frank", 120000)

# frank's pet is rover
frank.pet = rover

# flipper is-a fish
flipper = Fish()


# crouse is a Salmon
crouse = Salmon()

# harry is-a halibut
harry = Halibut()

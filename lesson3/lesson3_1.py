# MULTIPLE INHERITANCE - МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ

class Person:
    name = 'Will'
    age = 30


class Homosapiens:
    generation = 2000
    new_era = True


class Human(Person, Homosapiens):
    pass


h1 = Human()
print(h1.name, h1.new_era)


class Mother:
    beauty = "precious"
    kindness = True

    def __init__(self):
        print("Happy")


class Father:
    height = 180
    money = 100000

    def __init__(self, last_name):
        self.last_name = last_name

    def say_hello(self):
        print("Hello")

class Uncle(Father):
    pass


class Child(Father, Mother):
    pass
# class Grandchild(Child):
#     pass
#
#
# class GrandGrandChild(Grandchild):
#     pass

c1 = Child("Blackoff")
c1.say_hello()
c1 = Child("Willov")
print(c1.last_name, c1.kindness)

##########################################################
# MAGIC METHOD - МАГИЧЕСКИЕ МЕТОДЫ
val = 50
str_val = str(val)
# print(type(val))

class Parent:
    def __init__(self, last_name):
        self.last_name = last_name
        self.age = 2000

    def get_info(self):
        return f"This object: {self.last_name} - {self.age}"

    def __str__(self):
        return f"This STR of: {self.last_name} - {self.age}"

p1 = Parent("Jolbunov")


a = 20
b = 30
c = a + b


class Area:
    def __init__(self, x, y):
        self.width = x
        self.height = y

    def __str__(self):
        return f"Area is {self.width * self.height}"

    def __add__(self, other):
        tmp_width = self.width + other.width
        tmp_height = self.height + other.height
        new_area = Area(tmp_width, tmp_height)
        return new_area

a1 = Area(20, 30)
a2 = Area(10, 10)
a3 = a1 + a2

# print(a3)

class A:
    def __init__(self, word):
        print(f"Hello {word}! I'm First!")

class B(A):
    def __init__(self):
        print("Hello! I'm second!")
        super().__init__("janga!") # A("janga")


class C(B):
    def __init__(self):
        print("Я ПРОСТО ТРЕТИЙ!")
        super().__init__()


c1 = C()
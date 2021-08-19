# Inheritance - Наследование
# Incapsulation - Инкапсуляция
# Polymorphism - Полиморфизм

status = True

class Robot:  # Parent
    '''this robot is made in China''' # docstring
    head = 20 # public - общий - доступный
    _body = 80 # protected - защищенный
    __legs = 40 # private - изолированный - приватный - частный - скрытый

    def __init__(self, cpu_name):
        self.cpu = cpu_name

    def say_hello(self):
        print("Hello humans")
        print("LEGS:", self.__legs)

    def change_cpu(self, new_cpu):
        self.cpu = new_cpu

# print(Robot.__doc__)

class Terminator(Robot): # Child
    def find_sarah_connor(self):
        print("Terminator: Are you Sarah Connor ?")
        ans = input()
        if ans == 'yes':
            print("You are terminated")
        else:
            print("Go away!")

    def check_status(self, status):
        if status == True:
            print("Okey!")


r1 = Robot("Ryzen")
r2 = Robot("Intel i5")
r3 = Robot("Apple")

# print(r3.head)
#
# t1 = Terminator("Kirin8000")
#
# t1.say_hello()
# r1.say_hello()
# # t1.find_sarah_connor()
# t1.check_status(status)
# r1.__legs = 15
#
# # print(r1.cpu, r2.cpu, r3.cpu)
# # print(r1._body, r2._body, r3._body)
# # print(r1.__legs)
# # r3.say_hello()
# # print(Robot.__doc__)



class Person:
    def __init__(self, name, birth):
        self.__name = name
        self.birth = birth

    def say_name(self):
        print(f"My name is {self.__name}")

    def change_name(self, new_name):
        self.__name = new_name


class Human(Person):
    def __init__(self, name): # конструктор
        self.__name = name

    def say_name(self): # Polymorphism of Python
        print(f"I'm Human - {self.__name} ")

# p1 = Person("Jack", 1999)
# h1 = Human("Den")
#
# p1.say_name()
# h1.say_name()


class Bank:
    __total_money = 1000 #private

    # def __init__(self):
    #     self.total_money = 1000

    @classmethod
    def give_money(cls, amount):
        cls.__total_money -= amount

    @classmethod
    def take_money(cls, amount):
        cls.__total_money += amount

    @classmethod # доступ к аттрибутам класса
    def get_total_money(cls):
        return cls.__total_money

    @staticmethod # simple function
    def print_cache():
        print("Your cache is gone")

b1 = Bank() # sozdanie filiala
b2 = Bank()

b1.give_money(500)
b2.give_money(200)
b1.take_money(600)
b2.take_money(400)
Bank.print_cache()
#
# print(b2.get_total_money())

class Mfo(Bank):

    @staticmethod
    def control_money():
        print("Bank money is controlled")


def make_sum(a, *args, **kwargs):
    # args - tuple
    # kwargs - dictionary
    tmp = 0
    for i in args:
        tmp += i

    kw_res = 0
    for val in kwargs.values():
        kw_res += val
    print("RESULT RES:", kw_res)
    return tmp + a

print(make_sum(5, 20,5,4,8,2, age=25, weight=45))



























current_year = 2021

class Person:
    '''Human class'''
    __total_persons = 0


    def __init__(self, birth_year, name,  **kwargs): #конструктор
        if birth_year >= current_year:
            raise Exception("Bigger than current year!")
        # raise TypeError("Bigger than current year!"
        self.__birth_year = birth_year
        self.__name = name
        self.__language = kwargs.get("Language")
        self.increase_total_persons()
        Person.__total_persons += 1 # total persons


    @classmethod
    def get_total_persons(cls):  # общее число созданных Человеков
        return cls.__total_persons

    @classmethod
    def increase_total_persons(cls):
        cls.__total_persons += 1

    def is_adult(self):
        if current_year - self.__birth_year >= 18:
            return True
        else:
            return False

    def get_age(self):
        print(current_year - self.__birth_year)

    def talk(self):
        print("Hello World")
class Teacher(Person):
    def talk(self):
        print("Greetings, I'm your teacher")

p1 = Person(1995,"Jack", language = 'Italian')
p2 = Person(2002, "Dilya")
print(Person.get_total_persons())
print(p1.is_adult())
print(p1.get_age())
t1 = Teacher(2010,"Ivan")
t1.talk()
print(Person.get_total_persons())

#
#     #self.__total_persons += 1
#         if self.birth_year >= self.__current_year:
#             raise TypeError("Bigger than current year!")
#
#     def is_adult(self):
#         if self.__current_year - self.birth_year >= 18:
#             print(True)
#         else:
#             print(False)
#
#     def get_age(self):
#         print(self.__current_year - self.birth_year)  # Person's age
#
#     def talk(self):
#         print("Hello World")
#
#
# class Teacher(Person):
#
#     def new_talk(self, ntalk):  # Переопределние метода talk
#         self.talk = ntalk
#         print("Greetings, I'm your teacher")
#
#     def tech(self):
#         print("Lesson started by Teacher")
#
#
# person1 = Person('Myname', 2004)
# person2 = Person('Aiym', 1999)
# person3 = Person('Alice', 1990)
#
# print(person2.name)
# print(person2.is_adult())
# print(person2.get_age())
#
#
#
# teacher1 = Teacher('Airas', 2001)
# teacher2 = Teacher('Daniiar', 2000)
# teacher3 = Teacher('Abai', 1998)
#
# print(teacher1.name)
# print(teacher1.is_adult())
# print(teacher1.get_age())
#Standup
#Что сделала:
# ДЗ №2
# Проблемы:
# были с get_total_perrsons
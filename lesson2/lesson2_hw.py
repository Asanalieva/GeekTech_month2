current_year = 2021
class Person:
    '''Human class'''
    __total_persons = 0
    __birth_year = 2002 #maybe input?
    __name = "Alice"
    __language = "spanish"



    def __init__(self,name,birth_year,**kwargs):
        self.name = name
        self.birth_year = birth_year

        self.__language = kwargs

        self.__total_persons +=1
        if self.__birth_year >= current_year:
            raise ValueError("Bigger than current year!")


    def is_adult(self):
        if self.__birth_year - current_year == 18: #<
            print(True)
        else:
            print(False)

    def get_age(self):
        print(current_year - self.__birth_year ) #Person's age

    @classmethod
    def get_total_persons(cls):#общее число созданных Человеков
        pass

    def talk(self):
        print("Hello World")

class Teacher(Person):

    def new_talk(self,ntalk):#Переопределние метода talk
        self.talk = ntalk
        print("Greetings, I'm your teacher")
    def tech(self):
        print("Lesson started by Teacher")

person1 = Person('Myname',2001)
person2 = Person('Aiym',2000)
person3 = Person('Alice',1990)

teacher1 = Teacher('Airas',2001)
teacher2 = Teacher('Daniiar',2000)
teacher3 = Teacher('Abai',1998)

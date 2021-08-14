class House:
    width = 300
    height = 150
    price = 2000
    rooms = 5
    doors = 3


    def __init__(self,address):
        self.address = address


my_house = House("Djal 29   ") #создание обЪекта
house2 = House("Ahunbaeva 22 ")

print(my_house.address,my_house.rooms,my_house.width)
print(house2.address,house2.rooms,house2.width)
class user:
    '''this class descibes the behavior of users'''
    website = "gmail"
    domain = "kg"
    #object's attribute
    def __init__(self,name,last_name,login,password): #
        self.name = name                             #
        self.last_name = last_name
        self.login = login
        self.password = password

    def say_hello(self): #method
        print("Hello",self.name)

    def get_login(self): #method
        print("Your login is",self.login)

    def change_login(self,new_login):
        self.login = new_login

    def change_password(self,new_pass):
        if len(new_pass) < 4:
            raise  Exception("Should be over 4")
        self.password = new_pass
    @classmethod
    def change_website(cls,new_website):
        cls.website = new_website

u1 = user("Jack","Aikaliev","aika_ja",123)
u2 = user("Dilbara","Asanalieva",'dilya_12',122112)
u3 = user("Kim","Kardashian",'kimm',"IloveLA")

print(u1.name,u2.name,u3.name,u1.website)
u1.get_login()
u1.change_login('new_login_is_here')
u1.get_login()
u1.change_website('mail')
print(u1.website)

#
# u1.say_hello()
# u2.say_hello()
# u3.say_hello()


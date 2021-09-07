import os, random
import re


class Library:
    __secret_key = os.environ.get("SECRET_LIB_KEY")
    __book_list = ["451° по Фаренгейту", "Цветы для Элджернона", "Портрет Дориана Грея", "Маленький принц"]

    @classmethod
    def get_books(cls):
        if cls.__secret_key is not None:
            return cls.__book_list
        else:
            raise Exception("Forbidden action")

    @classmethod
    def change_key(cls, new_key):
        cls.__secret_key = new_key

    @classmethod
    def get_secret_key(cls):
        return cls.__secret_key

    @classmethod
    def give_book(cls, book_name):
        if cls.__secret_key is not None and book_name in cls.__book_list:
            cls.__book_list.remove(book_name)
            return cls.__book_list
        else:
            print(f"Can't give this book {book_name} to you")

    def check_student_key(self):
        pub_key = os.environ.get('STUDENT_PUB_KEY')
        pattern = "\d{2}\w+-\w\d\w\d-\d{3}\w\d\w"  # "42bc-a9f2-672a7d"
        #ww = re.findall(pattern,pub_key)
        if pub_key == pattern:
            print("Public key Success")
            return True
        else:
            print("Wrong Public Key")
            return False


# print("File loaded")

# Library.change_key("new password")
# print(Library.get_secret_key())
# print(Library.get_books())
# num = random.randint(0, 3)
# book_name = Library.get_books()[num]
#
# Library.give_book(book_name)
# print(Library.get_books())
print(Library.check_student_key(1))

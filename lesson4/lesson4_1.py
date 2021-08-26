#########
# MODULS

import random, os

candidates = ["Amantur", "Atai", "Dilbara", "Maruf", "Temirlan"]
z = random.choice(candidates)
# print(z)
# print(candidates[random.randint(0,4)])
greencard = ["Aktan", "Atai", "Belek", "Temirlan", "Sultanmurat"]
random.shuffle(greencard)
# print(greencard.pop()) #get last item in the list

this_dictionary = os.getcwd()  # get current working place
# print("PATH", this_dictionary)
# print(os.getlogin()) #my pc login
# print(os.listdir()) #my current file
# print(os.name) #operation system nt==Windows

# create folder

new_folder = "august"
path = os.path.join(this_dictionary, new_folder)
# this_dictionary > new_folder
# C:\Users\user\PycharmProjects\python09_month2\lesson4\august
# print(path)

import datetime, time

started = datetime.datetime.now()

# for i in  range(20):
#     calcs = i + 100 + 2000 * 3 / 4 // 2 * 3
#     time.sleep(0.2)
finish = datetime.datetime.now()
# print(started)
# print(finish)

dt = datetime.datetime(2020, 1, 13, 14, 20, 30)  # year.month.day hour.min.seconds
# print(dt.weekday()) # day of written month in dt
# # Mn Tu Wd Th Fr St Sn
# # 0  1  2  3  4  5  6
# print(dt.date())


from random import choice, shuffle
from random import randint as randomizer

res = choice(candidates)
shuffle(candidates)
rn = randomizer(0, 100)
# print(rn)

from datetime import date, datetime

t1 = date(year=2021, month=7, day=9)
t2 = date(year=2021, month=8, day=23)
diff = t2 - t1
# print(diff) #сколько времени прошло с t2 dо t1

d1 = datetime(year=2021, month=7, day=9, hour=18, minute=24, second=40)
d2 = datetime(year=2021, month=8, day=23, hour=19, minute=24, second=40)
# print(d2 - d1)

import my_module_calc  # imported from another file named my_module_calc.py

area = my_module_calc.calc_area(5, 10)  # using module in my_module_calc and function calc_area()
print(area)

import requests
r = requests.get("https://random-data-api.com/api/omniauth/twitter_get")
print(r.content)

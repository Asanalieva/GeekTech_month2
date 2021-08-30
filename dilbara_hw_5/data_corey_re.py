import re

file = open("C:/Users/user/PycharmProjects/python09_month2/src/data_corey.txt ")  # opened txt file to use data in my code
text = file.read()

phone = r"\d{3}-\d{3}-\d{4}"  # Regular Expressions pattern
total = re.findall(phone, text)  # total amount of phone numbers in data_corey.txt
print(f"Total amount of phone numbers:{len(total)}")  # 103 lines
seven = r"\d{3}-\d{3}-\d{3}7"
end_7 = re.findall(seven, text)
print(f"Total amount of phone numbers with ending 7 is: {len(end_7)}")  # 15 number

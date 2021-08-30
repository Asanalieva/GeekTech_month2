########## Regular expressions - регулярные выражения
import re  # Regular expressions

msg = "Hello World from World"
print(re.findall("World", msg))  # Searching "World" from msg

text = "Lorem Ipsum 1345 is simply dummy text of the https://youtube.org/ printing and typesetting industry. " \
       "Lorem Ipsum has been the industry's standard dummy well@net.com text ever since the 1500s, when a" \
       "n unknown printer took a galley of type and scrambled it to make a type specimen book. It " \
       "has survived not only five hey@sy.net centuries, but also the leap into electronic typesetting, http://gmail.com/ remaining" \
       " essentially unchanged 234 . It was 1325 popularised in the 1960s with the release of Letraset sheets containing" \
       " Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including " \
       "ersions of Lorem Ipsum dilbara@gmail.com"
#\.(com|net|org) #or com or net or org
standart = '123 - 123'  # 3 digit
# \d{3}-\d{3} фильтр по нашим стандартом 3 до 3 после -
'''
123=233
125-342
243-225 
245-24'''

a = '133-124-3424'  # \d{3}[-.*]\d{3}[-.*]\d{4} for all a b z
b = '134.314.2344'
z = '314*243*2345'
#[a-zA-Z] #all from a to z and with Big words
#[0-3] from 0 to 3
#^a строка которая начинается с буквы а

# Mr Smith  #M(r|s)\s[a-zA-Z]+  #to find it #M(r|s|rs)\.?\s[a-zA-Z]+
# Mrs. Smith            \s white space (пробел)
# Mr Lol


#http://mail.ru/         #https?://[a-z0-9]+\.\w+/  #to find all these site*
#http://gmail.com/
#https://youtube.org/

# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x.span())
pattern = r'https?://[a-z0-9]+\.\w+/' #raw string и есть
x = re.findall(pattern, text)
print(f"found {len(x)} items") # len of sites in text
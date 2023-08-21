# no. 1
# import re
# text = "John is a student of Cyclobold and his matric number is m123d but he often says he is \"the scholar of our time\""
# uppercase = re.compile(r'[A-Z]')
# digit = re.compile(r'[0-9]')
# space = re.compile(r' ')
# uppercase_exists = re.findall(uppercase, text)
# digit_exists = re.findall(digit, text)
# space_exist = re.findall(space, text)
# if uppercase_exists:
#     print("Uppercase found: ", uppercase_exists)
# if digit_exists:
#     print("Number found: ", digit_exists)
# if space_exist:
#     print("space found: ", space_exist)

#no. 2
# import re
# def match_pattern(input_string):
#     pattern = r'\d+_'
#     if re.search(pattern, input_string):
#         return True
#     else:
#         return False
    
# input_string = input('Input a string: ')
# if match_pattern(input_string):
#     print('Match')
# else:
#     print('match not found')

#no. 3
# import re
# def match_pattern(word):
#     pattern = r'\w\d$'
#     if re.search(pattern, word):
#         return True
#     else:
#         return False
# word = input('Type a word: ')
# if match_pattern(word):
#     print('match')
# else:
#     print('no match')

#no. 4
# import re
# text = 'I am John, the name of my tech academy is Cyclobold'
# space = re.findall(r'\s', text)
# if space:
#     print("space found: ", space)
# new_text = re.sub(r'John,\s+the', r'John, and the', text) 
# print(new_text)

#no. 5
# import re
# program = r'^(a|e)'
# text = input('Enter a text: ')

# if re.match(program, text):
#     print('match')
# else:
#     print('not match')

#no 7
import requests
import re
from bs4 import BeautifulSoup
r = requests.get("https://cyclobold.com/")
# if r.status_code == 200:
#     soup = BeautifulSoup(r.text, 'html.parser')
#     paragraphs = soup.find_all('p')
#     program = r'\bmovies\b'
#     movies_found = False
#     for paragraph in paragraphs:
#         text = paragraph.get_text()
#         if re.search(program, text, re.IGNORECASE):
#             print(f"found 'movies' in paragraph: {text}")
#             movies_found = True
#     if not movies_found:
#         raise ValueError("the word 'movies' was not found")
# else:
#     print(f"failed to get webpage. Status code: {r.status_code}")


# if r.status_code == 200:
#     soup = BeautifulSoup(r.text, 'html.parser')
#     paragraphs = soup.find_all('p')
#     program = r'\bforms\b'
#     forms_found = False
#     for paragraph in paragraphs:
#         text = paragraph.get_text()
#         if re.search(program, text, re.IGNORECASE):
#             print(f"found 'forms' in paragraph: {text}")
#             forms_found = True
#     if not forms_found:
#         raise ValueError("the word 'forms' was not found")
# else:
#     print(f"failed to get webpage. Status code: {r.status_code}")


# if r.status_code == 200:
#     soup = BeautifulSoup(r.text, 'html.parser')
#     paragraphs = soup.find_all('p')
#     program = r'\d+'
#     digits_found = False
#     for paragraph in paragraphs:
#         text = paragraph.get_text()
#         digits = re.findall(program, text)
#         if digits:
#             # print(f"found digits in paragraph: {text}")
#             print(f"digits found: {', '.join(digits)}")
#             digits_found = True
#     if not digits_found:
#         raise ValueError("no digits found")
# else:
#     print(f"failed to get webpage. Status code: {r.status_code}")


#no 8
soup = BeautifulSoup(r.content, "html.parser")
data = soup.prettify()
paragraphs = soup.find_all("p")
for paragraph in paragraphs:
    print(paragraph)
content = soup.find(class_ = 'modal-content')
print(content.text)
para = open('para.pdf', 'w')
para.write(content.text)
para.close()
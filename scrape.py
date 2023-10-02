# import requests
# from bs4 import BeautifulSoup
# r = requests.get("https://www.netflix.com/ng/")
# soup = BeautifulSoup(r.content, 'html.parser')
# data = soup.prettify()
# divs = soup.find_all('div')
# for div in divs:
#    print(div.text)
#do a .src
# images = soup.find_all('img')
# for image in images:\
#    print(image)

# import requests
# from bs4 import BeautifulSoup
# r = requests.get("https://cyclobold.com/")
# soup = BeautifulSoup(r.content, "html.parser")
# data = soup.prettify()
# divs = soup.find("div")
# print(divs)
# images = soup.find_all("img")
# for image in images:
#     # print(image)
#     print(image)
# content = soup.find(class_ = 'modal-content')
# print(content.text)
# head = open('head.pdf', 'w')
# head.write(content.text)
# head.close()
# content = soup.find(class_ = 'lazy img-fluid')
# print(content.text)
# image = open('image.pdf', 'w')
# image.write(content.text)
# image.close()

import requests
from bs4 import BeautifulSoup

import mysql.connector

db_con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "management_db"
)
cursor = db_con.cursor()
r = requests.get("https://cyclobold.com/")
data = BeautifulSoup(r.content, "html.parser")
soup = data.prettify()
ps = data.find_all('p')
text = ""
num = 8 
for p in ps:
    text = p.text

if cursor:
    mysql_insert_query = f"""
                INSERT INTO `content` VALUES (%s, %s);
"""
    record = (num, text)
    cursor.execute(mysql_insert_query, record)
    db_con.commit()
    print(text)
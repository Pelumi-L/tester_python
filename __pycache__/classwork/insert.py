import mysql.connector
import requests
import json
api_content = requests.get("http://universities.hipolabs.com/search?country=United+States")
contents = api_content.json()
if(contents):
    country = " "
    domain = " "
    alpha = " "
    state = " "
    web = " "
    name =" "
    for content in contents:
        country = content["country"]    
        domain = content["domains"]
        alpha = content["alpha_two_code"]
        state = content["state-province"]
        web = content["web_pages"]
        name = content["name"]
insert = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'university_db',
)
cursor = insert.cursor()
if(cursor):
    for cont in contents:
        insert_query = f"""INSERT INTO `api_content` VALUES(%s, %s, %s, %s, %s, %s);"""
        data = (cont["country"], "".join(cont["domains"]), cont["alpha_two_code"], cont["state-province"], "".join(cont["web_pages"]), cont["name"])    
        cursor.execute(insert_query, data)
        insert.commit()
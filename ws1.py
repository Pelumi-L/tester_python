import requests
from bs4 import BeautifulSoup
response = requests.get("https://cyclobold.com/")
soup = BeautifulSoup(response.content, 'html.parser')
data = soup.prettify
# divs = soup.find_all('div')
# for div in divs:
#     print(div.text)
images = soup.find_all('img')
for image in images:
    print(image)
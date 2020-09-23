from bs4 import BeautifulSoup
import requests
# url = "https://www.tutorialspoint.com/index.htm"
# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")
# print(soup.title)
#
#
# for link in soup.find_all('a'):
#     print(link.get('href'))

#-------------------------------------------
url = "https://www.theverge.com/2020/9/13/21435507/nvidia-acquiring-arm-40-billion-chips-ai-deal"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup, "\n")

print("\n", soup.h1.text, "\n")

for a in soup.find_all('p'):
    print(a)


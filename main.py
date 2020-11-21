# ------------------------------------------------------------------------------------------------------------------
# NOTE: This only works under the assumption that the accessed web page does not change its layout and class naming
# ------------------------------------------------------------------------------------------------------------------

# Need to be installed with pip

# Dependencies
import requests
from bs4 import BeautifulSoup


import time
import json
# ------------------------------------------------------------------------------------------------------------------

# Go to imdb 150 top Anime movie list page
url = "https://www.imdb.com/list/ls026128329/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")


# Parts of the webpages where we're getting out data out pf
tags = soup.findAll("h3", class_="lister-item-header")
spans = soup.findAll("span", class_="runtime")
spans2 = soup.findAll("span", class_="lister-item-index unbold text-primary")
boxes = soup.findAll("div", class_="lister-item mode-detail")


outList = []

# Helper functions
def extractDescriptions():
    list = []

    # the movie descriptions
    for i in boxes:
        list.append(i.findAll("p")[1].text.strip())

    return list
def extractRank():
    list = []

    # the movie ranks
    for i in spans2:
        list.append(int(i.text.split('.')[0]))

    return list
def extractRuntimes():
    list = []

    # the movie runtimes
    for i in spans:
        list.append(int(i.text.split(" ")[0]))

    return list
def extractNames():
    list = []

    # the movie names
    for a in tags:
        list.append(a.find_all('a')[0].text)

    return list



# Extracting the needed info
descriptionsList = extractDescriptions()
rankList = extractRank()
runtimesList = extractRuntimes()
namesList = extractNames()




if (len(descriptionsList) == len(runtimesList) == len(namesList) == len(rankList)):
    for i in range(len(descriptionsList)):
        outList.append(
            {
                "rank": rankList[i],
                "name": namesList[i],
                "runtime": runtimesList[i],
                "description": descriptionsList[1]
            }
        )




# save to a json file
with open("Anime-Movie-list.json", 'w') as fileObject:
    json.dump(outList, fileObject)


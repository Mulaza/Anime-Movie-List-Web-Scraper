# ------------------------------------------------------------------------------------------------------------------
# NOTE: This only works under the assumption that the accessed web page does not change its layout and class naming
# ------------------------------------------------------------------------------------------------------------------

# Need to be installed with pip
from bs4 import BeautifulSoup
import requests

# ------------------------------------------------------------------------------------------------------------------

# Go to imdb 150 top Anime movie list page
url = "https://www.imdb.com/list/ls026128329/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

# look fot only the 'h3' tage with the class of 'lister-item-header'
tags = soup.findAll("h3", class_="lister-item-header")


# create an empty string to hold the movie names
listString = ""


# loop through the h3 tags to get a list of a tags and het the text within them
for a in tags:

    # append every movie name to the end of a list
    listString = listString + "{} \n".format(a.find_all('a')[0].text)


# create a file to add and hold all of the movie names
with open("Anime-Movie-list.txt", 'a') as fileObject:
    fileObject.write(listString)


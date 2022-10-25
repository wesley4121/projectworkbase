import re
import requests
from bs4 import BeautifulSoup

def returnLocation(uri):   
    htmlfile=requests.get(uri)
    soup=BeautifulSoup(htmlfile.text,"lxml")
    location=soup.find("div",class_="jsx-3666296992 map").iframe["src"]
    longitudeLatitude=re.search(r"2[2-5]+.+1[1-2]+.+\d",location).group(0)
    newLongitudeLatitude=longitudeLatitude.split(",")
    return newLongitudeLatitude


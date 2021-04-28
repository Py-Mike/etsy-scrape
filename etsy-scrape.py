#etsy-scrape.py
#Written By: Py-Mike
#Date: 4/28/2021
#Description: A script that takes the JSON output from the Etsy api, parses it for the url containing the Full Size Images
#             then downloads them to a specified path.

import json                         #for parsing the JSON file
import requests                     #to handle the pull request
import os                           #to format the file name
from urllib.parse import urlparse   #to parse the url

#User Variables
apikey = '<etsy api key>'
shopname = ' <Name of Shop to backup>'
outputdirectory = '<c:\\test\\>' #Allows users to set a Directory for the Output

#Instead of Opening a local file I want to be able to Post the request to the api and just use the results

for offset in range(0,600,100): #Iterates 5 times
    #Loads the api url and imports the data in JSON format
    apiurl = "https://openapi.etsy.com/v2/shops/" + shopname + "/listings/active?method=GET&api_key=" + apikey + "&fields=title,url&limit=100&offset=" + str(offset) + "&includes=MainImage"
    response = requests.get(apiurl, allow_redirects=True)
    response.raise_for_status()
    listings = response.json()

    #Loops through the dictionary and extracts the image URL
    #then takes the URL and downloads it to a specified folder
    for i in listings['results']:
        #Extracts the image URL
        j = i.get('MainImage')
        url = j.get('url_fullxfull')
        print(url)

        #Extracts and modifies the file name from the url for windows filesystem
        a = urlparse(url)
        path = outputdirectory + os.path.basename(a.path)

        #downloads the image
        r = requests.get(url, allow_redirects=True)

        #writes it to the specified path
        file = open(path, 'wb')
        file.write(r.content)
        file.close()
        print("")
        
        
    
    

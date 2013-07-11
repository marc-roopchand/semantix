from bs4 import BeautifulSoup
import quopri
import json
import os, errno
import settings

def parseData():
    INPUT_FILE = os.path.join(settings.APP_DATA_HTML, 'california_pizza_kitchen.txt')
    soups = [] 

    with open(INPUT_FILE) as inputFile:
        for line in inputFile:
            # Load the line and the value 'body'.
            body = json.loads(line)['body']
            # Use the quopri module to decode the qp encoded value of each page.
            decodedQP = quopri.decodestring(body)
            soups.append(BeautifulSoup(decodedQP))
    
    return soups


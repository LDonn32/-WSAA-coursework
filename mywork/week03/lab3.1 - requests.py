# lab3.1 - requests.py
# Author: Laura Donnelly

'''
# Task 1 - make a request to google and print the response text

import requests

url = "https://google.com"
response = requests.get(url)

print(response.text)

'''



import requests
url = "https://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(url)
# print(response.json())

def readbooks():
    response = requests.get(url)
    return response.json()
if __name__ == "__main__":
    print(readbooks())

def readbooksbyid(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createbook(book):
    response = requests.post(url, json=book)
    return response.json()

def updatebook(id, book):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

def deletebook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()
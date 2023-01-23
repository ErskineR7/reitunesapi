import pymongo
import requests

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['topsongs']

mycol = mydb["uk2"]
mycol.drop()
mycol = mydb["uk2"]

url = "https://rss.applemarketingtools.com/api/v2/gb/music/most-played/50/albums.json"

response = requests.get(url)
data = response.json()

i=0


while i < 50:
    genre = data['feed']['results'][i]['id']
    mydict = { "id": genre }
    x = mycol.insert_one(mydict)
    i+=1

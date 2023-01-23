import pymongo
import requests

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['topsongs']

mycol = mydb["us"]
mycol.drop()
mycol = mydb["us"]

url = "https://rss.applemarketingtools.com/api/v2/us/music/most-played/50/albums.json"

response = requests.get(url)
data = response.json()

i=0


while i < 50:
    genre = data['feed']['results'][i]['genre']['name']
    mydict = { "genre": genre }
    x = mycol.insert_one(mydict)
    i+=1

#for artist_dict in data['feed']['entry']
    #artist_name = artist_dict['im:artist']['label']
    #album_name = artist_dict['im:collection']['im:name']['label']
    #song_name = artist_dict['title']['label']
    #genre = artist_dict['category']['attributes']['term']
#freemsqlhosting.net

#mycursor = mydb.cursor()

#   sql = "INSERT INTO US100 (artist, album, song, genre) VALUES (%s, %s, %s, %s"
#   val = (artist_name, album_name, song_name, genre)
#   mycursor.execute(sql, val)

#   mydb.commit()

#

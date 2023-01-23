import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['topsongs']
mycol = mydb["us"]

myquery = { 'genre': "Country" }

mydoc = mycol.find(myquery)

i=0
for x in mydoc:
    print(x)
    i+=1

print(i)

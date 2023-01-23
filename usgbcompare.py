import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['topsongs']
mycol = mydb["us2"]
ukcol = mydb["uk2"]

i=0

for x in mycol.find({},{ "_id": 0, "id": 1}):
    for y in ukcol.find({},{ "_id": 0, "id": 1}):
        if x == y:
            print(i)
            i+=1

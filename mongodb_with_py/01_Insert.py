import os

from dotenv import load_dotenv

load_dotenv()

import pymongo

mongoDbUrl = os.getenv('MONGO_URL')

myclient = pymongo.MongoClient(mongoDbUrl)

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

mydict = {
    "name": "Jaosn Jafari",
    "address": "Highway 371"
}

x = mycol.insert_one(mydict)

print(x.inserted_id)

import os

from dotenv import load_dotenv

load_dotenv()

import pymongo

mongoDbUrl = os.getenv('MONGO_URL')

myclient = pymongo.MongoClient(mongoDbUrl)

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

myquery = { "name": "Jason Jafari" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

for x in mycol.find():
  print(x)
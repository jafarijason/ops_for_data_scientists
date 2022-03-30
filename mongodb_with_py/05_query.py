import os

from dotenv import load_dotenv

load_dotenv()

import pymongo

mongoDbUrl = os.getenv('MONGO_URL')

myclient = pymongo.MongoClient(mongoDbUrl)

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

myquery = { "name": "Jason Jafari" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
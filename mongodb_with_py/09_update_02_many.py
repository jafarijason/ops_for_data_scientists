import os

from dotenv import load_dotenv

load_dotenv()

import pymongo

mongoDbUrl = os.getenv('MONGO_URL')

myclient = pymongo.MongoClient(mongoDbUrl)

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

myquery = { "name": "Jason Jafari" }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")

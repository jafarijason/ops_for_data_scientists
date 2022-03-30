import os

from dotenv import load_dotenv

load_dotenv()

import pymongo

mongoDbUrl = os.getenv('MONGO_URL')

myclient = pymongo.MongoClient(mongoDbUrl)

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

myquery = { "name": "Jason Jafari" }

x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")



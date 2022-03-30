import os

from dotenv import load_dotenv

load_dotenv()

import pymongo

mongoDbUrl = os.getenv('MONGO_URL')

myclient = pymongo.MongoClient(mongoDbUrl)

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)


__author__ = 'eric'
from pymongo import MongoClient

conn = MongoClient('localhost',27017)

db = conn.ymca_sample

collection = db.user_event

for i in range(collection.find().count()):


    print "!!",i
    a = collection.find({'event':'YA0birth'},{'token':1})[i]

    print a
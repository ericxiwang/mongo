__author__ = 'ericwang'

from pymongo import MongoClient


conn = MongoClient('localhost',27017)

name = conn.database_names()

print name


db = conn.ymca_example

print db

db.drop_collection('events')
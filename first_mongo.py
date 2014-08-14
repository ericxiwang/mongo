__author__ = 'ericwang'
import pymongo

import datetime

conn = pymongo.Connection('localhost',27017) #

db = conn.ymca

coll = db.events

data = coll.find()

print data

time1 = 1405026000
a = datetime.datetime.fromtimestamp(time1, None)
#dd = {"event": "YA0charge", "properties": {"num_retries": 1, "ctime": 1405026000, "YA0ver": "2.0.2", "event_id": "1ef34147-1b9f-11e4-999c-685b35d0c60d_1405026000", "YA0token": "8416e32af87f11e284c212313b0ace15", "currency": "CAD", "amount": 1.99, "distinct_id": "MX-1ee25900-1b9f-11e4-939b-685b35d0c60d", "uid": ""}}


db.events.remove({"properties.YA0token":"8416e32af87f11e284c212313b0ace15"})

#db.events.insert(dict(dd))
print a
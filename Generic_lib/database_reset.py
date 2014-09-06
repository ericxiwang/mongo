__author__ = 'eric'

import pymongo

import test_conf

db = test_conf.current_database
db['8416e32af87f11e284c212313b0ace15.active_users.day'].drop()
db['8416e32af87f11e284c212313b0ace15.active_users.month'].drop()
db['8416e32af87f11e284c212313b0ace15.active_users.week'].drop()

db['8416e32af87f11e284c212313b0ace15.active_users.day.tmp'].drop()
db['8416e32af87f11e284c212313b0ace15.active_users.month.tmp'].drop()
db['8416e32af87f11e284c212313b0ace15.active_users.week.tmp'].drop()



db['8416e32af87f11e284c212313b0ace15.new_users.day'].drop()
db['8416e32af87f11e284c212313b0ace15.new_users.month'].drop()
db['8416e32af87f11e284c212313b0ace15.new_users.week'].drop()

db['8416e32af87f11e284c212313b0ace15.new_users.day.tmp'].drop()
db['8416e32af87f11e284c212313b0ace15.new_users.month.tmp'].drop()
db['8416e32af87f11e284c212313b0ace15.new_users.week.tmp'].drop()


#db['8416e32af87f11e284c212313b0ace15.dau.tmp'].drop()

db.events.remove()


db.games.update({'_id':'8416e32af87f11e284c212313b0ace15'},{"$set":{'timezone':'Asia/Hong_Kong'}},upsert=False)
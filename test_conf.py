__author__ = 'eric'
import pymongo

##### server setting #####
DB_server = pymongo.Connection('localhost', 27017)

current_database = DB_server.ymcatest

API_host = "http://localhost:9000/api/"


#### event default value ####
SDK_version = "2.0.2"
token_id = "8416e32af87f11e284c212313b0ace15"

#### duration of testing ####

Date_start = "2014-8-1"
Date_end = "2014-8-31"
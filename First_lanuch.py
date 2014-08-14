__author__ = 'eric'
# ##### Create by Eric Wang ######
# ##### Create date 8/10/2014 ####
###### For "first launch" feature test ######
######  Generate 30 days user data ######

import uuid
import Data_gen
import time
import datetime
import pymongo
import random
import json
conn = pymongo.Connection('localhost', 27017)

#### Data Base init ####

db = conn.ymca

db.events.remove({"properties.YA0token":"8416e32af87f11e284c212313b0ace15"})


def first_launch_gen(date_start, duration, post_enable):


    sum = 0
    for days in range(1, duration):
        ISOFMT = '%Y-%m-%d %H:%M:%S'


        #print "day", days

        date_start_1 = datetime.datetime(*time.strptime(time.strftime(date_start), ISOFMT)[:6])



        current_date = str(date_start_1 + datetime.timedelta(days - 1))

        #print current_date

        for amount_user in range(days):


            current_date_1 = time.strptime(str(current_date), "%Y-%m-%d %H:%M:%S")

            cTime = int(time.mktime(current_date_1))

            country_code = random.choice(['CA', 'US'])


            ################# Generate distinct_id ###################################
            distinct_id = str(country_code + "-" + str(uuid.uuid1()))

            YA0birth = Data_gen.package_generator("YA0birth", "2.0.2", "8416e32af87f11e284c212313b0ace15",
                                                  cTime, distinct_id, country_code)

            date_post(YA0birth, post_enable)

            daily_total = amount_user + 1

        sum = sum + daily_total


    return sum
    conn.close()



##################################	Retention Event end ######################################



def date_post(event, post_enable):
    if post_enable == 1:
        global conn

        db = conn.ymca

        db.events.insert(event)

    else:
        pass


if __name__ == '__main__':
    date_start = "2014-7-22 23:00:00" # local time

    duration = 5

    first_launch_gen(date_start, duration, post_enable=1)




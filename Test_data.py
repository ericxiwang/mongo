__author__ = 'eric'
# ##### Create by Eric Wang ######
# ##### Create date 8/10/2014 ####
# ##### For "first launch" feature test ######
######  Generate 30 days user data ######

import uuid
import Data_gen
import time
import datetime
from datetime import date
import pymongo
import random
import test_conf
import json
db = test_conf.current_database

def Feature_range(date_start, date_end):
    base_time = " 23:00:00"

    date_start_time = int(time.mktime(time.strptime(str(date_start + base_time), "%Y-%m-%d %H:%M:%S")))
    date_end_time = int(time.mktime(time.strptime(str(date_end + base_time), "%Y-%m-%d %H:%M:%S")))

    API_start = date_start
    API_end = date_end

    duration = int((date_end_time - date_start_time) / 86400) + 2

    return date_start_time, date_end_time, API_start, API_end, duration


def Input_data_gen(date_start, duration, post_enable):

    users_daily = []

    sum = 0
    for days in range(1, duration):
        items = {}

        current_date = str(datetime.datetime(*time.strptime(date_start, '%Y-%m-%d %H:%M:%S')[:6]) + datetime.timedelta(days - 1))


        cTime = int(time.mktime(time.strptime(str(current_date), "%Y-%m-%d %H:%M:%S")))

        ####################### First_launches users ########################
        for amount_user in range(1000000*days):

            country_code = random.choice(['CA'])
            distinct_id = str(country_code + "-" + str(uuid.uuid1()))



            ####################    DAU #############################

            DAU_users = Data_gen.package_generator("YA0birth",cTime, distinct_id, country_code)
            date_post(DAU_users, post_enable)


             ################# Generate distinct_id ###################################


            '''YA0birth = Data_gen.package_generator("YA0birth",cTime, distinct_id, country_code)
            date_post(YA0birth, post_enable)



            ##################### Revenue ###################

            Revenue_users = Data_gen.package_generator("YA0charge",cTime, distinct_id, country_code)

            date_post(Revenue_users, post_enable)

            Revenue_users = Data_gen.package_generator("YA0charge",cTime, distinct_id, country_code)

            date_post(Revenue_users, post_enable)'''




            ######################   Session length ###########################


            '''Session_users = Data_gen.package_generator("YA0session",cTime, distinct_id, country_code)
            date_post(Session_users, post_enable)'''





            daily_total = amount_user + 1



            #datetime_TS = time.mktime(str(datetime.datetime.fromtimestamp(cTime).strftime('%Y-%m-%d')))

        #print datetime_TS

        sum = sum + daily_total

        sum_daily = amount_user + 1

        items["user"] = sum_daily
        items["ts"] = int(time.mktime(date.fromtimestamp(cTime).timetuple())) # new TS only remain the date info

        users_daily.append(items)





    return sum, users_daily




##################################	Retention Event end ######################################



def date_post(event, post_enable):
    if post_enable == 1:
        global db

        db.events.insert(event)

    else:
        pass


if __name__ == '__main__':


    a = Input_data_gen(datetime.datetime.fromtimestamp(Feature_range(test_conf.Date_start, test_conf.Date_end)[0]).strftime("%Y-%m-%d %H:%M:%S"),
                   duration=int(Feature_range(test_conf.Date_start, test_conf.Date_end)[4]),
                   post_enable=1)
    print a






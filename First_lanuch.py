__author__ = 'eric'
# ##### Create by Eric Wang ######
###### Create date 8/10/2014 ####
###### For "first launch" feature test ######
######  Generate 30 days user data ######



import uuid
import Data_gen
import time
import datetime
import pymongo
import random
import json


def first_launch_gen(date_start, duration, post_enable):

    for days in range(1,duration):
        ISOFMT = '%Y-%m-%d %H:%M:%S'

        print "day",days

        date_start_1 = datetime.datetime(*time.strptime(time.strftime(date_start), ISOFMT)[:6])


        current_date = str(date_start_1 + datetime.timedelta(days-1))

        print current_date

        for amount_user in range(days):



            print "++++",amount_user

            current_date_1 = time.strptime(str(current_date), "%Y-%m-%d %H:%M:%S")

            cTime = int(time.mktime(current_date_1))


            country_code = random.choice(['CA', 'US'])

            ##################  Country code generate end ##############################



            ################# Generate distinct_id ###################################
            distinct_id = str(country_code + "-" + str(uuid.uuid1()))







            YA0birth = Data_gen.package_generator("YA0birth", "2.0.2", "8416e32af87f11e284c212313b0ace15",
                                              cTime, distinct_id, country_code)

            date_post(YA0birth, post_enable)







            print cTime


def project_profile(date_start, duration, http_post_enable):
    for x in range(0, duration):
        #################### treat date increase daily and transfer into ctime format #################

        ISOFMT = '%Y-%m-%d %H:%M:%S'
        date_start_1 = datetime.datetime(*time.strptime(time.strftime(date_start), ISOFMT)[:6])



        current_date = time.strptime(str(date_start_1), "%Y-%m-%d %H:%M:%S")

        print current_date

        event_gen(current_date, x + 1, http_post_enable)
        current_date = str(date_start_1 + datetime.timedelta(x))

        print x,"--------- one day end --------------"


def event_gen(current_date, x, http_post_enable):
    datetime_input = int(time.mktime(current_date))  # ####### transfer current_date into ctime	#########

    amount_birth = x
    print "!!!",x

    daily_user_list = []  # create a list for reuse distinct_id, clear this daily

    ####################### daily event as follow #####################

    for daily_birth in range(1,amount_birth):
        def random_time(datetime_input):
            date_with_random = datetime.datetime.utcfromtimestamp(datetime_input)

            date_with_random_1 = time.strptime(str(date_with_random), "%Y-%m-%d %H:%M:%S")

            date_random_ctime = int(time.mktime(date_with_random_1))

            return date_random_ctime


        ####################### Country code generate in term of weight in list #########################




        country_code = random.choice(['CA', 'US'])

        ##################  Country code generate end ##############################



        ################# Generate distinct_id ###################################
        distinct_id = str(country_code + "-" + str(uuid.uuid1()))

        daily_user_list.append(distinct_id)  # append all distince_id (in one day) into list



        ########################## YA0birth  as follow ###################

        YA0birth = Data_gen.package_generator("YA0birth", "2.0.2", "4b5b5c2e208811e3b5a722000a97015e",
                                              random_time(datetime_input), distinct_id, country_code)

        http_post(YA0birth, http_post_enable)






##################################	Retention Event end ######################################
conn = pymongo.Connection('localhost', 27017)  #


def date_post(event, post_enable):
    if post_enable == 1:
        global conn

        db = conn.ymca

        db.events.insert(event)

    else:
        pass


if __name__ == '__main__':
    date_start = "2014-7-1 00:00:00"


    duration = 3

    '''project_profile(date_start, duration,
                    http_post_enable= 1)  # if http_post_enable = 0 that means no real package to be sent out'''





    first_launch_gen(date_start,duration,post_enable = 1)

    conn.close()


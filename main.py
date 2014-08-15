__author__ = 'eric'
import First_lanuch
import pymongo

import Fetch_API

##### first launch test cases #####
date_start = "2014-7-22 23:00:00" # local time
duration = 20
conn = pymongo.Connection('localhost', 27017)
def First_lanuch_test():
    global date_start
    global duration




    #First_lanuch.first_launch_gen(date_start, duration, post_enable=1)

    return First_lanuch.first_launch_gen(date_start, duration, post_enable=1)


def First_oupt_API():
    Pacific_return = Fetch_API.URL_gen("first_launches","2014-07-20","2014-08-16","pacific")

    GMT_return = Fetch_API.URL_gen("first_launches","2014-07-20","2014-08-16","GMT")

    return Pacific_return,GMT_return





def Result_judgment(Sum_of_input,Sum_of_ouput_Pacific):



    if Sum_of_input == Sum_of_ouput_Pacific[0]|Sum_of_input == Sum_of_ouput_Pacific[1]:

        print "GMT pass!"

    else:
        print "Test failed!"

        return False









if __name__ == '__main__':


    def bug_reproduce():


        #### Data Base init ####

        db = conn.ymca

        db.events.remove({"properties.YA0token":"8416e32af87f11e284c212313b0ace15"})
        input = First_lanuch_test()

        output = First_oupt_API()

        a = Result_judgment(input,output)

        return a

    while bug_reproduce() != False:


        bug_reproduce()





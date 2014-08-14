__author__ = 'eric'
import First_lanuch
import pymongo

import Fetch_API

##### first launch test cases #####

def First_lanuch_test():
    date_start = "2014-7-22 23:00:00" # local time

    duration = 5

    #First_lanuch.first_launch_gen(date_start, duration, post_enable=1)

    return First_lanuch.first_launch_gen(date_start, duration, post_enable=1)


def First_oupt_API():
    Pacific_return = Fetch_API.URL_gen("first_launches","2014-07-21","2014-07-29","pacific")

    GMT_return = Fetch_API.URL_gen("first_launches","2014-07-21","2014-07-29","GMT")

    return Pacific_return,GMT_return





def Result_judgment(Sum_of_input,Sum_of_ouput_Pacific):



    if Sum_of_input == Sum_of_ouput_Pacific[0]:

        print "GMT pass!"

    else:
        print "GMT failed!"

    if Sum_of_input == Sum_of_ouput_Pacific[1]:

        print "Pacific PASS!"

    else:
        print "pacific failed"







if __name__ == '__main__':


    input = First_lanuch_test()

    output = First_oupt_API()

    Result_judgment(input,output)
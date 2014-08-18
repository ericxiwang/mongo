__author__ = 'eric'
import First_lanuch
import pymongo
import datetime
import Fetch_API

##### first launch test cases #####
date_start = "2014-7-1" # local time

date_end = "2014-7-3"


conn = pymongo.Connection('localhost', 27017)


def First_oupt_API(date_start,date_end):

    Pacific_return = Fetch_API.URL_gen("first_launches",date_start,date_end,"pacific")

    GMT_return = Fetch_API.URL_gen("first_launches",date_start,date_end,"GMT")



    return Pacific_return,GMT_return





def Result_judgment(Sum_of_input,Sum_of_ouput_Pacific):

    print Sum_of_input
    print Sum_of_ouput_Pacific



    if Sum_of_input == Sum_of_ouput_Pacific[0] or Sum_of_input == Sum_of_ouput_Pacific[1]:

        print "GMT pass!"

    else:
        print "Test failed!"

        return False


if __name__ == '__main__':

    date_start = "2014-7-1" # local time

    date_end = "2014-7-3"





    def bug_reproduce(date_start,date_end):



        #### Data Base init ####

        db = conn.ymca

        db.events.remove({"properties.YA0token":"8416e32af87f11e284c212313b0ace15"})

        input_data = First_lanuch.first_launch_gen(datetime.datetime.fromtimestamp(First_lanuch.Feature_range(date_start, date_end)[0]).strftime("%Y-%m-%d %H:%M:%S"),
                                              First_lanuch.Feature_range(date_start, date_end)[4], post_enable=1)

        output_data = First_oupt_API(date_start,date_end)[1]

        len_1 = len(input_data)

        len_2 = len(output_data)




        if len_1 == len_2:
            for pos in range(len_1):

                print "input",input_data[1][pos]
                print "output",output_data[1][pos]

                off_set = int(output_data[1][pos]['ts']) + 25200  # offset + 7 hours
                print off_set

                if input_data[1][pos]['ts'] == off_set and input_data[1][pos]['user'] == output_data[1][pos]['users']:
                    print "PASS"
                else:

                    print






        else:
            pass

        #print input[1]




    #while bug_reproduce() != False:

    bug_reproduce(date_start,date_end)

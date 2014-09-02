__author__ = 'eric'
import sys
import main
import time

date_start = "2010-7-1" # local time

date_end = "2010-7-30"



result = main.bug_reproduce(date_start,date_end,feature_name = "first_launches")

#main.bug_reproduce(date_start,date_end,feature_name = "user_start")


if result[1] == []:  # if nothing in failed result list

    print "========== All Test Pass! =========="

    for list in result[0]:

        print list
    print "========== All Test Pass! =========="
    sys.exit(1)

else:

    #print "Test Failed!!!!!!!"

    for list in result[1]:

        print list
    print "Test Failed!!!!!!!"
    sys.exit(0)




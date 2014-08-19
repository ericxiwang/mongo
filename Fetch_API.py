import urllib2
import json
import time

def URL_gen(feature_name,startDate,endDate,timeZone):

    sum = 0

    #URL = "http://localhost:9000/api/first_launches?collection_name=events&endDate=2014-01-30&startDate=2014-01-02&timezone=pacific&token=8416e32af87f11e284c212313b0ace15&type=day"

    host_name = "http://localhost:9000/api/"

    #test_feature = "first_launches"

    collection_name = "collection_name=" + "events"

    endDate = "endDate=" + str(endDate)

    startDate = "startDate=" + str(startDate)

    timezone = "timezone=" + str(timeZone)

    token = "token=" + "8416e32af87f11e284c212313b0ace15"

    type = "type=day"

    if feature_name == "new_buyer":

        URL = host_name + "buyer_sort" + "?" + collection_name + "&" + endDate + "&" + "first=1" + startDate + "&" + timezone + "&" + token + "&" +type




    else:

        URL = host_name + feature_name + "?" + collection_name + "&" + endDate + "&" + startDate + "&" + timezone + "&" + token + "&" +type

    print URL

    a = urllib2.urlopen(URL).read()

    list = json.loads(a)





    for dict in list:


        TS = dict.get('ts')

        #DT = time.gmtime(TS)
        daily_users = dict.get('users')

        sum = sum + daily_users

    #print "SUM:",sum



    return sum,list
#print json.dumps(a)

def result_check():

    pass



if __name__ == '__main__':

    date_start = "2014-7-21" # local time

    date_end = "2014-7-31"

    URL_gen("first_launches",date_start,date_end,"pacific")

    URL_gen("user_start",date_start,date_end,"GMT")

    URL_gen("new_buyer",date_start,date_end,"GMT")


# ##YMCA server site test script###
# ##Author:Eric Wang	####
# ##Create data:/5/1/2014####
# ##script name:package_gen.py#####

import base64
import sys
import json
import uuid
import datetime
import time
import random


def event_id_gen(random_datetime):  # generate the real event_id element
    UU_ID = str(uuid.uuid1())

    event_id = UU_ID + "_" + str(random_datetime)
    return event_id


def package_generator(event_name, SDK_version, token_id, Current_datetime, distinct_id, country_code):

    GMT_DT = time.gmtime(Current_datetime)
    Pacific_DT = time.localtime(Current_datetime)

    gmt_time = datetime.datetime(*tuple(GMT_DT)[:6])

    pacific_time = datetime.datetime(*tuple(Pacific_DT)[:6])



    event_property = {
        "distinct_id": distinct_id,  #"YA0debug": 1,
        "YA0ver": SDK_version,
        "uid": "",
        "num_retries": 5,  #"amount": 100.0,  #"currency": "CNY",

        "YA0token": token_id,  #"ctime": int(time.time()),
        "ctime": Current_datetime,
        "event_id": event_id_gen(Current_datetime),
        "time": gmt_time,


        "time_pacific": pacific_time,




        "country": country_code


    }

    #main JSON:template_data
    template_data = {
        "event": event_name,
        "properties": event_property,


    }

    if event_name == "YA0session":
        start_1 = Current_datetime
        length_1 = int(random.randint(20, 100))  #session length range (10s to 1000s)
        end_1 = int(start_1 + length_1)
        session_info = {"start": start_1, "length": length_1, "end": end_1}

        event_property.update(session_info)



    elif event_name == "YA0charge":

        amount = random.choice([1.99, 2.99, 3.99])

        USD = amount * 0.7

        event_property.update({"currency": "CAD", "amount": amount, "YA0USD": USD})

    #json_data = json.dumps(template_data)

    json_data = template_data

    json_data

    #transfer_base64 = "data=" + base64.b64encode(json_data)

    #return transfer_base64
    return json_data

# return json_data



if __name__ == '__main__':
    event_name = "YA0birth"
    timeStamp = 1403971200
    distinct_id = "BE-211"

    a = package_generator(event_name, "2.0.2", "8416e32af87f11e284c212313b0ace15", timeStamp, distinct_id, "CA")



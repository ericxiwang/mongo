# ##YMCA server site test script###
# ##Author:Eric Wang	####
# ##Create data:/5/1/2014####
# ##script name:package_gen.py#####


import uuid
import datetime
import time
import test_conf


def event_id_gen(random_datetime):  # generate the real event_id element
    UU_ID = str(uuid.uuid1())

    event_id = UU_ID + "_" + str(random_datetime)
    return event_id


def package_generator(event_name, Current_datetime, distinct_id, country_code):

    GMT_DT = time.gmtime(Current_datetime)
    Pacific_DT = time.localtime(Current_datetime)

    gmt_time = datetime.datetime(*tuple(GMT_DT)[:6])

    #pacific_time = datetime.datetime(*tuple(Pacific_DT)[:6])




    event_property = {
        "distinct_id": distinct_id,  #"YA0debug": 1,
        "YA0ver": test_conf.SDK_version,
        "uid": "",
        "num_retries": 5,  #"amount": 100.0,  #"currency": "CNY",

        "YA0token": test_conf.token_id,  #"ctime": int(time.time()),
        "ctime": Current_datetime,
        "event_id": event_id_gen(Current_datetime),
        "time": gmt_time,


        "time_pacific": gmt_time,




        "country": country_code



    }

    template_data = {
        "event": event_name,
        "properties": event_property,


    }

    if event_name == "YA0session":
        start_1 = Current_datetime
        length_1 = 100
        end_1 = int(start_1 + length_1)
        session_info = {"start": start_1, "length": length_1, "end": end_1}

        event_property.update(session_info)



    elif event_name == "YA0charge":

        amount = 1.00

        USD = amount * 0.7

        event_property.update({"currency": "USD", "amount": amount, "YA0USD": USD})


    json_data = template_data

    return json_data





if __name__ == '__main__':
    event_name = "YA0birth"
    timeStamp = 1404198000
    distinct_id = "BE-211"

    a = package_generator(event_name, timeStamp, distinct_id, "CA")
    print a



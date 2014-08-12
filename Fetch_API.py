import urllib2

import json



a = urllib2.urlopen("http://localhost:9000/api/user_start?collection_name=events&endDate=&event_type=play&startDate=&timezone=pacific&token=8416e32af87f11e284c212313b0ace15&type=day").read()

list = json.loads(a)

print type(list)

for dict in list:
    print type(dict)
    print dict.get('ts')
    print dict.get('users')
    print '==============================='

#print json.dumps(a)
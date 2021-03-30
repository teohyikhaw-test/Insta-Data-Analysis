import json

import http.client

conn = http.client.HTTPSConnection("instagramdimashirokovv1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "8331ae32c8msh013d217412a1464p1dce59jsn6a38b434ff97",
    'x-rapidapi-host': "InstagramdimashirokovV1.p.rapidapi.com"
    }

hashtag="icmshk"
#conn.request("GET", "/user/yikhaw_teoh", headers=headers)
conn.request("GET", "/tag/"+hashtag+"/optional", headers=headers)

res = conn.getresponse()
data = res.read()

json_dictionary = json.loads(data.decode("utf-8"))

#print(data.decode("utf-8"))

with open('testdata.json', 'w') as outfile:
    json.dump(json_dictionary, outfile)

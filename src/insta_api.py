from src.connect_api import *
import json

def insta_data(tag):
    #Enter tag as "/user/username" or "/tag/hashtag/optional"

    conn,headers=connectinstaapi()

    conn.request("GET", tag, headers=headers)
    #conn.request("GET", "/tag/"+hashtag+"/optional", headers=headers)

    res = conn.getresponse()
    data = res.read()
    return (data)

###sample usage
data=insta_data("/user/graduan")
json_dictionary = json.loads(data.decode("utf-8"))

#print(data.decode("utf-8"))

with open('testdata.json', 'w') as outfile:
    json.dump(json_dictionary, outfile)

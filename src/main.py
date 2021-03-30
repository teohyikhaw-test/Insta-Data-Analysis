from src.load_json import *

#client = MongoClient("mongodb+srv://"+username+":"+password+"@fbm1.awjp0.mongodb.net/test1?retryWrites=true&w=majority")

#db = client['hashtag']
#col = db['icmshk']


#x = col.find_one()
#print(x)

download_json("hashtag","icmshk","test1.json")
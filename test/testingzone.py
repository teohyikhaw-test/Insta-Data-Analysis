import json
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from datetime import datetime

#Stop Words
stop_words = stopwords.words('english') #sets language to english
newStopWords = ['.',',','?','!',"'"]
stop_words.extend(newStopWords)

def tokenandstopw(filename):
    #Open file
    with open(filename) as json_file:
        data = json.load(json_file)

    #Extract message data only
    data=data["messages"]
    length=len(data)

    #timestamp = data["timestamp_ms"]
    #dt_object = datetime.fromtimestamp(timestamp/1000)
    #print("dt_object =", dt_object)

    w=[]
    for i in range(length):
        if data[i]['sender_name'] == 'Teoh Yik Haw':
            #avoid KeyError which occurs when some documents don't have column
            try:
                text=word_tokenize(data[i]['content'])
                text=[y for y in text if not y in stop_words]
                w.extend(text)
            except KeyError:
                pass

    w=nltk.FreqDist(w)
    return w

jq1=tokenandstopw("jq_message_1.json")
jq2=tokenandstopw("jq_message_2.json")
#print(b.most_common(100))




"""import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=False)
            print(namedEnt)
            #namedEnt.draw()
    except Exception as e:
        print(str(e))

process_content()"""

#from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
#from nltk.corpus import gutenberg

# sample text
#sample = gutenberg.raw("bible-kjv.txt")

#tok = sent_tokenize(sample)

#for x in range(5):
#    print(tok[x])

import nltk
#nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
x=sia.polarity_scores("I hate people!!!!")
print(x)
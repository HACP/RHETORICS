import DPlib, sys



filename = '/home/hugo/DEEPLEARNING/SENTIMENT_ANALYSIS/data/training/raw_tweets_1452787775.7.json'

DATA = DPlib.getDATA(filename)

for item in DATA:
    print item + ',0'

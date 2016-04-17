import time, os, csv
from tweepy import Stream
from tweepy import OAuthHandler, API
from tweepy.streaming import StreamListener


consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

 
 
start_time = time.time() #grabs the system time

#Listener Class Override
class listener(StreamListener):
 
    def __init__(self, start_time, time_limit=60):
 
        self.time = start_time
        self.limit = time_limit
 
    def on_data(self, data):
 
        while (time.time() - self.time) < self.limit:
 
            try:
 
                saveFile = open('../DATA/raw_tweets_' + str(start_time) + '.json', 'a')
                saveFile.write(data)
                #saveFile.write('\n')
                saveFile.close()

                return True
 
 
            except BaseException, e:
                print 'failed ondata,', str(e)
                time.sleep(5)
                pass
 
        exit()
 
    def on_error(self, status):
 
        print statuses

def getDATA_HASHTAG(keyword_list, time_mins):

    auth = OAuthHandler(consumer_key, consumer_secret) #OAuth object
    auth.set_access_token(access_token_key, access_token_secret)
 
 
    twitterStream = Stream(auth, listener(start_time, time_limit=time_mins*60)) #initialize Stream object with a time out limit
    twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream Object


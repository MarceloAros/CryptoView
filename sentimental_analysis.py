#!/usr/bin/env python
# -*- coding: utf-8 -*-
#https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/

import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob
  
class TwitterClient(object): 
    ''' 
    Generic Twitter Class for sentiment analysis. 
    '''
    def __init__(self): 
        ''' 
        Class constructor or initialization method. 
        '''
        # keys and tokens from the Twitter Dev Console 
        consumer_key = 'kT9feIBWSGjRbVg9NomTRpC1V'
        consumer_secret = 'rkbCMh5I30dm8stH1hJ7EFttQFS3EyLebm1JDI6mnpVLjso68j'
        access_token = '1248927414-BTiLOgHBPnuTQitBdndKVK18wpLNjzJgMSrkaWZ'
        access_token_secret = 'PwRioESOuNwGUGtF76q1o7hmafiXGIhcLK3AF1W9yHRiq'
  
        # attempt authentication 
        try: 
            # create OAuthHandler object 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            # set access token and secret 
            self.auth.set_access_token(access_token, access_token_secret) 
            # create tweepy API object to fetch tweets 
            self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") 
  
    def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
  
    def get_tweet_sentiment(self, tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(self.clean_tweet(tweet)) 
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'
  
    def get_tweets(self, query, count = 10): 
        ''' 
        Main function to fetch tweets and parse them. 
        '''
        # empty list to store parsed tweets 
        tweets = [] 
  
        try: 
            # call twitter api to fetch tweets 
            fetched_tweets = self.api.search(q = query, count = count) 
  
            # parsing tweets one by one 
            for tweet in fetched_tweets: 
                # empty dictionary to store required params of a tweet 
                parsed_tweet = {} 
  
                # saving text of tweet 
                parsed_tweet['text'] = tweet.text 
                # saving sentiment of tweet 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 
  
                # appending parsed tweet to tweets list 
                if tweet.retweet_count > 0: 
                    # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
  
            # return parsed tweets 
            return tweets
  
        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e)) 

    def get_percentages(self):
        api = TwitterClient()
        percentages = []
        # calling function to get tweets 
        tweets = api.get_tweets(query = 'bitcoin', count = 200) 
    
        # picking positive tweets from tweets 
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
        # percentage of positive tweets 
        print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
        percentages.append((100*len(ptweets)/len(tweets)))
        # picking negative tweets from tweets 
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
        # percentage of negative tweets 
        print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
        percentages.append((100*len(ntweets)/len(tweets)))
        print(percentages[0])
        if (percentages[0]>percentages[1]):
            return (percentages[0])
        else:
            return (percentages[1])*(-1)
            
def main(comentario): 
    # creating object of TwitterClient Class 
    api = TwitterClient()
    percentages = []
    # calling function to get tweets 
    tweets = api.get_tweets(query = comentario, count = 200) 
  
    # picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    # percentage of positive tweets 
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    percentages.append((100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    percentages.append((100*len(ntweets)/len(tweets)))
    print(percentages)
    return percentages
    # percentage of neutral tweets 
    # print("Neutral tweets percentage: {} % \ ".format(100*len(tweets - ntweets - ptweets)/len(tweets))) 
    #if (format(100*len(ptweets)/len(tweets)) > format(100*len(ntweets)/len(tweets))):
     #   return (True)
   # else:
    #    return (False)
    # deciding if the news are overall negative or positive

     ##printing first 5 positive tweets 
    #print("\n\nPositive tweets:") 
    #for tweet in ptweets[:10]: 
     #   print(tweet['text'].encode('utf-8')) 
  
    #prinming  first 5 negative tweets 
    #print("\n\nNegative tweets:") 
    #for tweet in ntweets[:10]: 
     #   print(tweet['text'].encode('utf-8')) 
    
if __name__ == "__main__": 
    # calling main function 
    main('#coronavirus') 

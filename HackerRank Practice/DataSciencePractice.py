'''import tweepy
from textblob import TextBlob

consumer_key = 'kiWvtouSTcOn6eURDC6GUcUN6'
consumer_secret = 'Lgi4VGJbDdGlL8Zwoe1vBQtsKk5TZYnUAl2q04azoLMGngepu3'

access_token = '813666730249777152-zlhvVFJJ7l2oatVoENhs504Syr1O4aV'
access_token_secret = 'PfroxqtJDipJWKgEN6u5ihlpUjfApW6FlAdpareCQKIak'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
'''
'''
import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFm

#fetch data and import it
data = fetch_movielens(min_rating = 4.0)

#printtraining and testing data
print(repr(data['train']))
print(repr(data['test']))

#create model
model = LightFm(loss='warp')
#train model
mode.fit(data['train'], epochs = 30, num_threads = 2)

def sample_recommendation(model, data, user_ids):
    
    #number of users and movies in training data
    n_users, n_items = data['train'].shape
    #generate recommendations for each user we input
    for user_id in user_ids:
        
        #movies they already like
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
        
        #movies our model predicts they will like
        scores = model.predict(user_id, np.arrange(n_items))
        #rank them in order of most like to least liked
        top_items = data['item_labels'][np.argsort(-scores)]
        
        #print results
        print("User %s" % user_id)
        print("    Known positives:")
        
        for x in known_positives[:3]:
            print("        %s" % x)
            
        print ("    Recommended:")
        
        for x in top_items[:3]:
            print("        %s" % x)
            
sample_recommendation(model, data, [3, 25, 450])
'''
    
import pip; print(pip.pep425tags.get_supported())
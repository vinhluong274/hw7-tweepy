import unittest
import tweepy
import requests
import json


consumer_key = "9VyHlYhJzMvpkV2ZXMIhYzpHG"
consumer_secret = "sZ3NwVK2fwVWgtEMWe8hNae4hM8jGvd1BbCGMJSelbjGh2MXKh"
access_token = "921119316266962946-zMYVXOq1Zzv2xEG2bnkbubFcIISpO5Q"
access_token_secret = "knb7rflOIfT9UICKnQkigAk8yrb6JSC8f0NiomlpR8sHy"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

results = api.search(q="university of michigan")
print(type(results), "is the type of the results variable")

## OK, it's a dictionary. What are its keys?
print(results.keys())

## That 'statuses' key looks interesting.
print(type(results["statuses"]), "is the type of results['statuses']")
## OK, that's a list! Hmm. What's the type of the first element in it?
print(type(results["statuses"][0]), "is the type of the first element in the results")
## OK, that's a dictionary. What are its keys? I have a suspicion they'll be the same as the Tweet dictionary I saw before...
## I'm gonna assign that one tweet to a variable to make it easier.
umich_tweet = results["statuses"][0]
## Now, what are its keys?
print("\nThe keys of the tweet dictionary:")
print(umich_tweet.keys())

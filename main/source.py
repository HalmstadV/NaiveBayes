import tweepy

consumer_key ="Py6lNvkqZlwNkqUFFWMdjqfsB"
consumer_secret = "1g8JdGA9JPn7SECI3qhakMkuj9uX9pqLi02A5C2FivFJllIi8g"

access_token = "2331679425-A68ldHhc9Hk0ipOhJxnbA1vu3cnSDa2UTPK4GIJ"
access_token_secret = "njDNnvLiS9KxqGzQ9KtZt7tJSAhQegiJG7SnbzFo6FFku"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)

for user in tweepy.Cursor(api.followers, screen_name="twitter").items():
    print (user.screen_name)




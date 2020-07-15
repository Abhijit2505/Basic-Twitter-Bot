import tweepy
import time

CONSUMER_KEY = 'secret-key'
COMSUMER_SECRET = 'secret-key'
ACCESS_KEY = 'secret-key'
ACCESS_SECRET = 'secret-key'
auth = tweepy.OAuthHandler(CONSUMER_KEY,COMSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
search = '#technology'
numTweet = 500

for tweet in tweepy.Cursor(api.search,search).items(numTweet):
    try:
        print('Tweet Liked')
        tweet.favorite()
        print('Retweet done')
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

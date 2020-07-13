!pip install tweepy
import tweepy
import time

CONSUMER_KEY = '2bafyvAn0YKWMjs0Wbtd3wBBr'
COMSUMER_SECRET = 'sm3oWoYJgVe8Q9y5fGSaKgvvpnK5KuJ3OHsTpvjgRg0YKgHUnT'
ACCESS_KEY = '811384273911615488-8FzvFZVvzgHgZ76NYsSRGnuwXPZxQOh'
ACCESS_SECRET = '60ObqzXFatJuuglx2XoP8WA3AW4Y2wmsoguTFiHxt4KY8'
auth = tweepy.OAuthHandler(CONSUMER_KEY,COMSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
search = '#nature'
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

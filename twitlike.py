import tweepy
import time

api_key = "9uTIGlfwba8Jx3yDNiDfnqopo"
api_secret = "0nnlbBDcs5w2MNO89HaBXq4Ku8nrvYBjyh11kpU8JK4rZKW0b4"
bearer_token= "AAAAAAAAAAAAAAAAAAAAADC3ugEAAAAA7alm3XbtQXncizbkwsaoI2ciRBs%3DKMTPamp24l4jbpW8Ph6XYEYFAYk9lrbOi3SvkzuCtvXKMdLMqf"
access_token = "1809160550959702016-gydwU30tA78ZDwHIPwZied0z41vTc6"
access_token_secret ="46QgcmdPVE7PdlclquG3zBMqOU9dY1BQnxHJ0NGpouGRV"

client = tweepy.Client(bearer_token , api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key,api_secret,access_token,access_token_secret)
api = tweepy.API(auth)

client.create_tweet(text="Ayoo")

class MyStream(tweepy. StreamingClient):
    def on_tweet (self, tweet) :
        try:
            print(tweet.text)   
            client.like(tweet.id)
        except Exception as error:
            print(error)
            
        time.sleep(1)
        
        
stream = MyStream(bearer_token=bearer_token)

stream.add_rules(tweepy.StreamRule("Developer OR Software Engineer Hiring -is:retweet"))

stream.filter()
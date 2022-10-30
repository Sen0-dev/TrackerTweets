import tweepy
import config
import time


client= tweepy.Client(bearer_token= config.bearer_token)

class Tracker_Tweet():
        def __init__(self, id_user = "", username_user = "", key_word = "", hashTag = ""):
                self.id_user = id_user
                self.username_user = username_user
                

        def get_all_Tweets(self):
                return client.get_users_tweets( id = self.id_user)

        
        def print_last_Tweet(self):
                for tweets in self.get_all_Tweets().data:
                        return tweets.text

        
        def check_new_Tweet(self):
                old_tweet= self.print_last_Tweet()

                while old_tweet == self.print_last_Tweet():
                        time.sleep(4)
                        #print(f"CURRENT TWEET: {old_tweet}")
                        self.print_last_Tweet()
                
                print(self.print_last_Tweet())
                self.check_new_Tweet()


tracker_Tweets = Tracker_Tweet("") # Id of the Twitter account to track

tracker_Tweets.check_new_Tweet()

"""
# obtain id by username
def get_user_id(username):
    return client.get_user(username = username)

print(get_user_id("Ssayle_"))
"""
import tweepy
import config
import time


client= tweepy.Client(bearer_token= config.bearer_token)

class Tracker_Tweet():
        def __init__(self, id):
                self.id= id
                

        def get_idd(self):
                self.borderlands_tweets= client.get_users_tweets( id=self.id)

        
        def print_last_Tweet(self):
                self.get_idd()
                for tweets in self.borderlands_tweets.data:
                        all_tweet= tweets.text
                        return all_tweet

        
        def check_new_Tweet(self):
                old_tweet= self.print_last_Tweet()

                while old_tweet == self.print_last_Tweet():
                        time.sleep(4)
                        #print(f"CURRENT TWEET: {old_tweet}")
                        self.print_last_Tweet()
                
                print(self.print_last_Tweet())
                self.check_new_shiftCode()


tracker_Shift_code= Tracker_Tweet("3830990053") # Id of the Twitter account to track
tracker_Shift_code.check_new_Tweet()
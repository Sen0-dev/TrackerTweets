import tweepy
import real_config
import time


client= tweepy.Client(bearer_token= real_config.bearer_token)

class Tracker_Shift_code():
        def __init__(self, id):
                self.id= id
                

        def get_idd(self):
                self.borderlands_tweets= client.get_users_tweets( id=self.id)

        
        def print_last_shiftCode(self):
                self.get_idd()
                for tweets in self.borderlands_tweets.data:
                        all_tweet= tweets.text
                        return all_tweet
                        
        
        def check_new_shiftCode(self):
                old_tweet= self.print_last_shiftCode()
                while old_tweet == self.print_last_shiftCode():
                        time.sleep(4)
                        #print(f"ACTUAL TWEET: {old_tweet}")
                        self.print_last_shiftCode()
                
                print(self.print_last_shiftCode())
                self.check_new_shiftCode()


tracker_Shift_code= Tracker_Shift_code("3830990053")
tracker_Shift_code.check_new_shiftCode()
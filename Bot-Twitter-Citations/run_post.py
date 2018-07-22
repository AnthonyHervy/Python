#-*- coding: utf-8 -*-
import tweepy
import re
import time
from secret import *
from conf import *
from fonctions import *

# OAuth identification

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

print("Execution du script run_post.py")
def main():
    while True:
        text = citation_hasard(fichier_citations)
        if tweet_with_picture is True:
            output_filename = "output/{}.png".format(int(time.time()))
            print(write_image(text, output_filename, background_img=select_background_image()))
            api.update_with_media(output_filename)
        else:
            api.update_status(status=text)
        print(time.strftime('%H%M%S'), ": tweet posté, prochain tweet dans ", (time_between_tweets/60), "minutes")
        time.sleep(time_between_tweets)

if __name__ == "__main__":
    main()
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

### Stream Twitter

class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        print(status.user.screen_name)
        if re.search(regex_reply, status.text) is not None:
            text = citation_hasard(fichier_citations)
            if reply_with_picture is True:
                output_filename = "output/{}.png".format(int(time.time()))
                print(write_image(text, output_filename, background_img=select_background_image()))
                api.update_with_media(output_filename, status=text_reply, in_reply_to_status_id = status.id)
            else:
	            api.update_status(status=text)

    def on_error(self, status_code):
        return True # Don't kill the stream

    def on_timeout(self):
        return True # Don't kill the stream
		
sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=[bot_name])



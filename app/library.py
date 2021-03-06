# Utility methods.

import tweepy
import sys


class TweepyAPIs (object):
  """Base class for all needed tweepy APIs"""

  def __init__ (self):
    # Put your twitter credentials here.
    consumer_key = ""
    consumer_secret = ""
    access_key = ""
    access_secret = ""
  
    if not (consumer_key and consumer_secret and access_key and access_secret):
      print "Please enter all of your credentials."
      sys.exit()
  
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    self._api = tweepy.API(auth, parser=tweepy.parsers.ModelParser())

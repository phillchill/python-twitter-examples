#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-friendship
#  - outputs details of the relationship between two users.
#-----------------------------------------------------------------------

from twitter import *

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

#-----------------------------------------------------------------------
# the usernames whose relationship we want to examine
#-----------------------------------------------------------------------
source = config["username"]
target = "ideoforms"

#-----------------------------------------------------------------------
# perform the API query
# twitter API docs: https://dev.twitter.com/docs/api/1/get/friendships/show
#-----------------------------------------------------------------------
result = twitter.friendships.show(source_screen_name = source,
                                  target_screen_name = target)

#-----------------------------------------------------------------------
# extract the relevant properties
#-----------------------------------------------------------------------
following = result["relationship"]["target"]["following"]
follows   = result["relationship"]["target"]["followed_by"]

print "%s following %s: %s" % (source, target, follows)
print "%s following %s: %s" % (target, source, following)


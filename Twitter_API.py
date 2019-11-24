'''
 Gather data from twitter using twitter API

 In order to be able to use Twitter API you will need to visit http://dev.twitter.com/ and apply for access.
 Your application will be revised and you might be asked for more information about your use case within an email.
 After you are granted an access for Twitter API, you may visit http://dev.twitter.com/apps/new and create a new app.
'''

import twitter
from urllib.parse import unquote
import json
import pandas as pd

# Go to https://developer.twitter.com/en/apps to get values for these credentials
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

# Create a Twitter OAuth object
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initialize the API
twitter_api = twitter.Twitter(auth=auth)

# Set the query or hashtag you want to search for
query = '#DataScience' 
count = 100

search_results = twitter_api.search.tweets(q=query, count=count) 
statuses = search_results['statuses']

# Define a dataframe to save tweets in
tweets = pd.DataFrame(columns=['user', 'text', 'time'])

# Show one sample search result by slicing the list...
for i in range(0,len(statuses)):
    print(json.dumps(statuses[0], indent=1))
    
    # Add tweets to the dataframe
    tweets.loc[len(tweets)] = [statuses[i]["user"]["screen_name"], statuses[i]["text"], statuses[i]["created_at"]]
    
# Write the data in csv format
tweets.to_csv("tweets_api.csv", index=False)
from twitter import *
from tkinter import *
import json
import pprint
# t is assign to the keys needed to use twitter
t = Twitter(
    auth=OAuth('805338356326563841-qrbTYHwhSyUY5HFiJ4IzTn4fostBgFz','qGDgTnRhce89hLrDdaQKa8Voeigu85kPA22VzAAgYgbuf',
               'ZlmrsEGVpvCU21Jk9YRQxA45p','9wxvAq4MpV4eRCcsqhpfmGMpMQOKrSqxN2NZ36VuQ1LikvGOKB'))

#t.statuses.update(
 #status="Using @Robski5777 sweet Python Twitter Tools.")


#showTweets,  on line 1 pulls the user screen name and line 2 pulls the text message they sent.
def showTweets(x, num):

    for i in range(0, num):
        line1 = (x[i]['user']['screen_name'])
        line2 = (x[i]['text'])
        line1 + "\n" + line2 + "\n\n"

        return x

# getTweets show the org timeline by using the user name and returning x
def getTweets():
    x = t.statuses.home_timeline(screen_name="RobertWilliamsJr")
    return x


def tweet():
    
    global entryWidget
    
    if entryWidget.get().strip() == "":
        print("Empty")
    else:
        t.statuses.update(status=entryWidget.get().strip())
        entryWidget.delete(0,END)
        print("working")

    return numberOfTweets

#searchTwitter creats a query and pulls tweet.
def searchTwitter(query):
    tweets_list = []
    #search for tweet data
    tweet_Data = t.search.tweets(q=query,
                             count=3,
                             lang="en")
    for tweet in tweet_Data['statuses']:
        tweet_dump = json.dumps(tweet, indent=4)

        tweet_json =json.loads(tweet_dump)


        if 'text' in tweet_json:
            tweet_user = tweet_json['user']['name']
            tweet_text =tweet_json['text']

            tweets_list.append({'User' : tweet_user, 'Text' : tweet_text})
    return \
        {
            'Tweet': tweets_list
        }


# Put in token, token_key, con_secret, con_secret_key


numberOfTweets = 10
#testing phase
if __name__== "__main__":
    test = input("Enter Key Word: ")
    tweet_search = searchTwitter(test)
    pprint.pprint(tweet_search, indent= 4)



# showTweets(getTweets(), numberOfTweets)


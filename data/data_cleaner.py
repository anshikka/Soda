import re

def removeLinks(tweet):
    tweet = re.sub(r'http\S+', '', tweet)
    return tweet

def getListOfRetweets(db):
    cursor = db.cursor()
    retweetNumListQuery = "SELECT retweets from twitter_with_retweets"
    cursor.execute(retweetNumListQuery)
    result = cursor.fetchall()
    return [list(rt)[0] for rt in result]

def getListOfLikes(db):
    cursor = db.cursor()
    likeNumListQuery = "SELECT likes from twitter_with_retweets"
    cursor.execute(likeNumListQuery)
    result = cursor.fetchall()
    return [list(like)[0] for like in result]

def getListOfTweetsWithoutRetweets(db):
    cursor = db.cursor()
    tweetsListQuery = "SELECT text from twitter_with_retweets"
    cursor.execute(tweetsListQuery)
    result = cursor.fetchall()
    return [list(tweet)[0] for tweet in result]


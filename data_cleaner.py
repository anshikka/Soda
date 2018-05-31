import re

def removeLinks(tweet):
    tweet = re.sub(r'http\S+', '', tweet)
    return tweet

def getListOfRetweets(db):
    cursor = db.cursor()
    retweetNumListQuery = "SELECT retweets from twitter_without_retweets"
    cursor.execute(retweetNumListQuery)
    result = cursor.fetchall()
    return [list(rt)[0] for rt in result]

def getListOfLikes(db):
    cursor = db.cursor()
    likeNumListQuery = "SELECT likes from twitter_without_retweets"
    cursor.execute(likeNumListQuery)
    result = cursor.fetchall()
    return [list(like)[0] for like in result]

import re

def empty_database(db):
    cursor = db.cursor()
    empty_query_1 = "TRUNCATE TABLE twitter_with_retweets"
    empty_query_2 = "TRUNCATE TABLE twitter_without_retweets"
    cursor.execute(empty_query_1)
    cursor.execute(empty_query_2)

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

def getListOfTweetsWithoutRetweets(db):
    cursor = db.cursor()
    tweetsListQuery = "SELECT text from twitter_without_retweets"
    cursor.execute(tweetsListQuery)
    result = cursor.fetchall()
    return [list(tweet)[0] for tweet in result]

def getTopFiveTweets(db):
    cursor = db.cursor()
    topNTweetsQuery = "SELECT text from twitter_without_retweets ORDER BY likes desc LIMIT 5"
    topNLikesQuery = "SELECT likes from twitter_without_retweets ORDER BY likes desc LIMIT 5"
    topNRetweetsQuery = "SELECT retweets from twitter_without_retweets ORDER BY likes desc LIMIT 5"
    cursor.execute(topNTweetsQuery)
    tweet_result = cursor.fetchall()
    cursor.execute(topNLikesQuery)
    likes_result = cursor.fetchall()
    cursor.execute(topNRetweetsQuery)
    retweets_result = cursor.fetchall()
    return [[list (tweet)[0] for tweet in tweet_result], [list (like)[0] for like in likes_result], [list (retweet)[0] for retweet in retweets_result]]
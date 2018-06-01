import json
from dateutil import parser

def empty_database(db):
    cursor = db.cursor()
    empty_query_1 = "TRUNCATE TABLE twitter_with_retweets"
    empty_query_2 = "TRUNCATE TABLE twitter_without_retweets"
    cursor.execute(empty_query_1)
    cursor.execute(empty_query_2)

def get_tweets_with_retweets_from_user(api, username):
    current_api = api
    tweets = current_api.user_timeline(username, count = 100, include_rts = True)
    return tweets

def get_tweets_without_retweets_from_user(api, username):
    current_api = api
    tweets = current_api.user_timeline(username, count = 100, include_rts = False)
    return tweets

def put_into_database(db, api, username):
    #create new database csv file
    current_api = api
    cursor = db.cursor()
    insert_query_retweets = "INSERT INTO twitter_with_retweets (tweet_id, screen_name, created_at, text, likes, retweets) VALUES (%s, %s, %s, %s, %s, %s)"
    insert_query_no_retweets = "INSERT INTO twitter_without_retweets (tweet_id, screen_name, created_at, text, likes, retweets) VALUES (%s, %s, %s, %s, %s, %s)"

    #get tweets from user
    tweets_with_retweets = get_tweets_with_retweets_from_user(current_api, username)
    tweets_without_retweets = get_tweets_without_retweets_from_user(current_api, username)

    #write to mysql database with all tweets
    for tweet in tweets_with_retweets:
        tweet = json.loads(json.dumps(tweet._json))
        id = tweet['id']
        text = tweet['text']
        screen_name = tweet['user']['screen_name']
        created_at = parser.parse(tweet['created_at'])
        likes = tweet['favorite_count']
        retweets = tweet['retweet_count']
        cursor.execute(insert_query_retweets, (id, screen_name, created_at, text, likes, retweets))

    for tweet in tweets_without_retweets:
        tweet = json.loads(json.dumps(tweet._json))
        id = tweet['id']
        text = tweet['text']
        screen_name = tweet['user']['screen_name']
        created_at = parser.parse(tweet['created_at'])
        likes = tweet['favorite_count']
        retweets = tweet['retweet_count']
        cursor.execute(insert_query_no_retweets, (id, screen_name, created_at, text, likes, retweets))







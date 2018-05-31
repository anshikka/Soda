import tweepy as tp
import MySQLdb as sql

def setUpAuth(consumer_key, consumer_secret, access_token, access_token_secret):
    #set up OAuth system on Twitter
    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    #get access to api
    api = tp.API(auth)
    return api

def connectToSQLdb(host, user, paswd, db):
    db = sql.connect(host, user, paswd, db, charset = 'utf8mb4')
    db.autocommit(True)
    return db

import authenticate_credentials as auth
import data_retriever as dr
import data_cleaner as dc

#input keys for twitter
CONSUMER_KEY = 'INSERT_CONSUMER_KEY_HERE'
CONSUMER_SECRET = 'INSERT_CONSUMER_SECRET_HERE'
ACCESS_TOKEN = 'INSERT_ACCESS_TOKEN_HERE'
ACCESS_TOKEN_SECRET = 'INSERT_ACCESS_TOKEN_SECRET_HERE'


#input keys for mysql
HOST = "INSERT_HOST_HERE"
USER = "INSERT_USERNAME_HERE"
PASSWORD = "INSERT_PASSWORD_HERE"
DATABASE = "INSERT_NAME_OF_DATABASE_HERE"
PORT = "INSERT_PORT_HERE"


#input username to retreive tweets
username = 'INSERT_TWITTER_USERNAME_HERE'

#initialize OAuth and Retrieve Tweets
api = auth.setUpAuth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET) #authenticats api


#initialize mysql server
db = auth.connectToSQLdb(HOST, USER, PASSWORD, DATABASE)

dr.put_into_database(db, api, username)

def getDatabase():
    return db

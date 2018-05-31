import authenticate_credentials as auth
import data_retriever as dr
import data_cleaner as dc

#input keys for twitter
CONSUMER_KEY = 'jTM2LQX1F1EYlOMqZNOyF4oe1'
CONSUMER_SECRET = 'v95EqkBpu5fKtk2ih0DPKayJDXQKaVvBBL0d5Ihi0UtSXKDCBW'
ACCESS_TOKEN = '733418148-1eH19c1jQoUo8vfX2r2soFReB0fcAkTMC0iVsWVQ'
ACCESS_TOKEN_SECRET = '0tXEJeXXSSPf0oa4dV1dZ97IjWoWdb85yKyn4Pd1dZhde'


#input keys for mysql
HOST = "localhost"
USER = "root"
PASSWORD = "Mukti@54321"
DATABASE = "twitter_queries"
PORT = 3306


#input username to retreive tweets
username = 'anshikka'

#initialize OAuth and Retrieve Tweets
api = auth.setUpAuth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET) #authenticats api


#initialize mysql server
db = auth.connectToSQLdb(HOST, USER, PASSWORD, DATABASE)

dr.put_into_database(db, api, username)

def getDatabase():
    return db

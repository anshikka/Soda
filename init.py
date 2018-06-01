from authentication import twitter
from authentication import database
from authentication import keys
from data import data_retriever as dr
import dash
from analysis import sentiment_analysis as sa
from data import data_cleaner as dc
import dash_html_components as html
from visualization import graphs_processor as gp
from visualization import color_picker as cp


#TWITTER
#input keys for twitter
CONSUMER_KEY = keys.twitter_keys('CONSUMER_KEY')
CONSUMER_SECRET = keys.twitter_keys('CONSUMER_SECRET')
ACCESS_TOKEN = keys.twitter_keys('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = keys.twitter_keys('ACCESS_TOKEN_SECRET')
#initialize OAuth and Retrieve Tweets
api = twitter.setUpAuth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET) #authenticats api


#SQL
#input keys for mysql
HOST = keys.sql_keys('HOST')
USER = keys.sql_keys('USER')
PASSWORD = keys.sql_keys('PASSWORD')
DATABASE = keys.sql_keys('DATABASE')
PORT = keys.sql_keys('PORT')
#initialize mysql server
db = database.connectToSQLdb(HOST, USER, PASSWORD, DATABASE)


#input username to retreive tweets
username = input('Enter a twitter handle/username to analyze: ')


#REFRESH DATABASE
print("Refreshing and parsing data... \n \n \n")
dr.empty_database(db)
dr.put_into_database(db, api, username)


#MAIN DASHBOARD
app = dash.Dash()
app.layout = html.Div(style = {'backgroundColor' : cp.getColor('background')}, children=[
    html.H1(children='Twitter Data Analysis', style = {'font-family' : 'Roboto', 'textAlign' : 'center', 'color': cp.getColor('twitter_blue')}),
    gp.processComparisonGraph(db),
    gp.processSentimentGraph(sa.getSentimentScore(dc.getListOfTweetsWithoutRetweets(db)))
])

if __name__ == '__main__':
    app.run_server(debug=False)



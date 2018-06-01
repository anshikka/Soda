from textblob import TextBlob as tb

def getSentimentScore(tweets):
    length = len(tweets)
    totalSentiment = 0
    for tweet in tweets:
        tweetToAnalyze = tb(tweet)
        totalSentiment+=tweetToAnalyze.sentiment.polarity
    return (totalSentiment/length) * 100

def getSentimentPolarity(score):
    if(score < 0):
        return -1
    elif (score > 0):
        return 1
    else:
        return 0


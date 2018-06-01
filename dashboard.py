import dash
import init
from analysis import sentiment_analysis as sa
from data import data_cleaner as dc
import dash_html_components as html
from visualization import graphs_processor as gp
from visualization import color_picker as cp





app = dash.Dash()
app.layout = html.Div(style = {'backgroundColor' : cp.getColor('background')}, children=[
    html.H1(children='Twitter Data Analysis', style = {'font-family' : 'Roboto', 'textAlign' : 'center', 'color': cp.getColor('twitter_blue')}),
    gp.processComparisonGraph(main_database),
    gp.processSentimentGraph(sa.getSentimentScore(dc.getListOfTweetsWithoutRetweets(main_database)))
])

if __name__ == '__main__':
    app.run_server(debug=True)
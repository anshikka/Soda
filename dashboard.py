import dash
import dash_core_components as dcc
import dash_html_components as html
import init
import data_cleaner as dc

main_database = init.getDatabase()

colors = {'twitter_blue' : '#7FDBFF',
          'background' : '#111111'
}

app = dash.Dash()
app.layout = html.Div(style = {'backgroundColor' : colors['background']}, children=[
    html.H1(children='Twitter Data Analysis', style = {'font-family' : 'Roboto', 'textAlign' : 'center', 'color': colors['twitter_blue']}),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x': dc.getListOfLikes(main_database), 'y': dc.getListOfRetweets(main_database), 'type': 'bar', 'name': 'Likes vs. Retweets'}
            ],
            'layout': {
                'title': 'Likes vs. Retweets',
                'color' : 'blue',
                'xaxis' : {'title' :'Likes', 'color': colors['twitter_blue']},
                'yaxis' : {'title' : 'Retweets', 'color': colors['twitter_blue']}
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
import csv
import pandas as pd
import plotly.plotly as py
import sys

from collections import defaultdict
from pandas import DataFrame, Series
from plotly.graph_objs import *

city = sys.argv[1].lower()
path_to_csv_file = sys.argv[2]

df_csv = pd.read_csv(path_to_csv_file)

# Merge LinkedIn columns because there were two of them for some reason
# Comment if not required
df_csv['LinkedIn'].fillna(df_csv['LinkedIn.1'], inplace=True)
del df_csv['LinkedIn.1']
del df_csv['Unnamed: 14']

github = df_csv['GitHub']
resume = df_csv['Resume']
linkedin = df_csv['LinkedIn']
twitter = df_csv['Twitter handle']

x_axis = ['GitHub', 'Resume', 'LinkedIn', 'Twitter']

yes_bar = Bar(x=x_axis, y=[github.notnull().sum(), resume.notnull().sum(), linkedin.notnull().sum(), twitter.notnull().sum()], name='Yes')
no_bar = Bar(x=x_axis, y=[github.isnull().sum(), resume.isnull().sum(), linkedin.isnull().sum(), twitter.isnull().sum()], name='No')

data = Data([yes_bar, no_bar])
layout = Layout(
    barmode = 'group',
    title='WearHacks {0} Social Info'.format(city.capitalize()),
    xaxis=XAxis(
        title='Social Info',
        titlefont=Font(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=YAxis(
        title='Social Info Count',
        titlefont=Font(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
figure = Figure(data=data, layout=layout)
plot_url = py.plot(figure, filename='WearHacks/wearhacks_{0}_social_info'.format(city))

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

preference = df_csv["What's your preference?"]
preference.fillna('', inplace=True)
preference_dict = defaultdict(int)
for index, values in preference.items():
    if not values:
        preference_dict['NaN'] += 1
    else:
        for value in values.split('||'):
            if value:
                preference_dict[value] += 1
# Clean up
preference_key = ('Design', 'Hardware', 'Software', 'Biz Dev', 'NaN' )
for key in list(preference_dict.keys()):
    if key not in preference_key:
        del preference_dict[key]

preference_value = []
preference_count = []
for value, count in sorted(preference_dict.items()):
    preference_value.append(value)
    preference_count.append(count)

bar = Bar(x=preference_value, y=preference_count)
data = Data([bar])
layout = Layout(
    title='WearHacks {0} Project Role Preference '.format(city.capitalize()),
    xaxis=XAxis(
        title='Preference',
        titlefont=Font(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=YAxis(
        title='Preference Count' ,
        titlefont=Font(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
figure = Figure(data=data, layout=layout)
plot_url = py.plot(figure, filename='WearHacks/wearhacks_{0}_preference_role_distribution'.format(city))


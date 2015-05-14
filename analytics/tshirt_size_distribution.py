import csv
import plotly.plotly as py
import sys

from collections import defaultdict
from plotly.graph_objs import *

city = sys.argv[1].lower()
path_to_csv_file = sys.argv[2]
column_number = int(sys.argv[3])

with open(path_to_csv_file) as csv_file:
    csv_data = csv.reader(csv_file)
    next(csv_data, None)
    tshirt_distribution = defaultdict(int)
    for data in csv_data:
        tshirt_distribution[data[column_number]] += 1

tshirt_size = []
tshirt_size_quantity = []
for size, quantity in sorted(tshirt_distribution.items()):
    tshirt_size.append(size)
    tshirt_size_quantity.append(quantity)

bar = Bar(x=tshirt_size, y=tshirt_size_quantity)
data = Data([bar])
layout = Layout(
    title='WearHacks {0} T-shirt Distribution'.format(city.capitalize()),
    xaxis=XAxis(
        title='T-shirt Size',
        titlefont=Font(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=YAxis(
        title='Number of T-shirts',
        titlefont=Font(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
figure = Figure(data=data, layout=layout)
plot_url = py.plot(figure, filename='WearHacks/wearhacks_{0}_tshirt_distribution'.format(city))

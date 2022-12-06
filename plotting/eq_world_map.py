import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Изучение структурных данных
falename = 'plotting/data/eq_data_30_day_m1.json'
with open(falename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features'] # Создание словаря с чистыми данными

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    # перебор данных и добавление в список, для дальнейшей обработки
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    hover_texts.append(title)
    lons.append(lon)
    lats.append(lat)

# Нанесение данных на карту
# data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text': hover_texts,
    'marker':{
        'size':[3*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename = 'plotting/data/global_earthquakes.html')
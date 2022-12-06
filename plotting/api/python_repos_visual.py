import requests
from plotly.graph_objs import Bar
from plotly import offline

# Создание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Обработка результатов
response_dist = r.json()
repo_dists = response_dist['items']
repo_links, stars, labels = [], [], []

for repo_dist in repo_dists:
    repo_name = repo_dist['name']
    repo_url = repo_dist['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dist['stargazers_count'])

    owner = repo_dist['owner']['login']
    description = repo_dist['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# Построение визуализации
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker':{
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'},
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred python projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='plotting/api/python_repos.html')
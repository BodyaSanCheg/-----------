import requests

# Создание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")

# Сохранение ответа API в переменной
response_dist = r.json()
print(f"Total repositories: {response_dist['total_count']}")

# Анализ информации о репозиториях
repo_dists = response_dist['items']
print(f"Repositories returned: {len(repo_dists)}")

print("\nSelected information about each repository:")
for repo_dist in repo_dists:
    print(f"Name: {repo_dist['name']}")
    print(f"Owner: {repo_dist['owner']['login']}")
    print(f"Stars: {repo_dist['stargazers_count']}")
    print(f"Repository: {repo_dist['html_url']}")
    print(f"Description: {repo_dist['description']}")

# Анализ первого репозитория
"""
repo_dist = repo_dists[0]
"""
# print(f'\nKeys: {len(repo_dist)}')
# for key in sorted(repo_dist.keys()):
#     print(key)
"""
# Основные записи самого популярного репозитория
print("\nSelected information about first repository:")
print(f"Name: {repo_dist['name']}")
print(f"Owner: {repo_dist['owner']['login']}")
print(f"Stars: {repo_dist['stargazers_count']}")
print(f"Repository: {repo_dist['html_url']}")
print(f"Created: {repo_dist['created_at']}")
print(f"Updated: {repo_dist['updated_at']}")
print(f"Description: {repo_dist['description']}")
"""
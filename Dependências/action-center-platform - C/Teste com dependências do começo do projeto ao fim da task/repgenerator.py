import os
import csv
import requests

import requests
import json

commit_code = "22a7d7e2aee5029b43c5e44775b26e53bd6eb246"
url = f"https://api.github.com/search/commits?q={commit_code}"
response = requests.get(url)
json_data = json.loads(response.text)
repository_url = json_data["items"][0]["repository"]["html_url"]
print(repository_url)


def download_repos(csv_file_path, url_column_name, folder_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        urls = set(row[url_column_name] for row in reader)
    for url in urls:
        repo_name = url.split('/')[-1]
        os.makedirs(os.path.join(folder_path, repo_name), exist_ok=True)
        api_url = f'https://api.github.com/repos/{url[19:]}/tarball'
        response = requests.get(api_url)
        with open(os.path.join(folder_path, repo_name, f'{repo_name}.tar.gz'), 'wb') as f:
            f.write(response.content)


download_repos(r'D:\Taiti Pesquisa\Dependências\action-center-platform - C\Teste com dependências do começo do projeto ao fim da task\tasks_990(1).csv','REPO_URL',r'D:\Taiti Pesquisa\Repositórios necessários')

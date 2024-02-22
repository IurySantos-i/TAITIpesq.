from github import Github
g = Github()

commit = g.search_commits('2e63899a140d5a0d9186959fa4e965fabff9e291')[0]
url = commit._rawData['repository']['url']

print(url)
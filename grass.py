import requests
import datetime

access_token = 'your_access_token_here'

days = 365
data = []
for i in range(days):
    date = datetime.datetime.now() - datetime.timedelta(days=i)
    count = 1
    data.append({'date': date.strftime('%Y-%m-%d'), 'count': count})

url = 'https://api.github.com/user/repos'
headers = {'Authorization': 'token ' + access_token}
for d in data:
    payload = {'name': 'dummy', 'description': 'dummy', 'private': 'true'}
    r = requests.post(url, headers=headers, json=payload)
    if r.status_code == 201:
        repo_url = r.json()['html_url']
        commit_url = repo_url + '/commits'
        payload = {'date': d['date'], 'count': d['count']}
        r = requests.post(commit_url, headers=headers, json=payload)
        if r.status_code != 201:
            print('Failed to create commit: ' + r.text)
    else:
        print('Failed to create repository: ' + r.text)

import os
from datetime import datetime
import requests
from pprint import pprint

URL = 'https://superheroapi.com/api/2619421814940190/'

NAME_LIST = ['Hulk', 'Captain America', 'Thanos']


def the_smartest(name_list):
    intelligence_dict = dict()
    for name in name_list:
        resp = requests.get(URL + f'/search/{name}')
        resp.raise_for_status()
        for i in resp.json()['results']:
            if i['name'] in name_list:
                intelligence_dict[i['name']] = int(i['powerstats']['intelligence'])
    return max(intelligence_dict, key=intelligence_dict.get)


# print(the_smartest(NAME_LIST))


class YaUploader:
    UPLOAD_URL = r'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        res = requests.get(self.UPLOAD_URL,
                           params={'path': os.path.basename(file_path),
                                   'overwrite': 'true'},
                           headers={'Authorization': f'OAuth {self.token}'}
                           )
        res.raise_for_status()
        href = res.json()['href']
        with open(file_path, 'rb') as f:
            res1 = requests.put(href, files={'file': f})
        res1.raise_for_status()
        return 'Вернуть ответ об успешной загрузке'


# if __name__ == '__main__':
#     uploader = YaUploader(TOKEN)
#     res = uploader.upload(file_path)


def title_of_python(url):
    now = datetime.today().replace(hour=3, minute=0, second=0, microsecond=0)
    second_now = int(datetime.timestamp(now))

    resp = requests.get(url, params={
        'tagged': 'python',
        'fromdate': second_now - 172800,
        'todate': second_now,
        'site': 'stackoverflow'
    })
    resp.raise_for_status()
    items = resp.json()['items']
    for item in items:
        print(item['title'])


# title_of_python('https://api.stackexchange.com/2.2/questions')

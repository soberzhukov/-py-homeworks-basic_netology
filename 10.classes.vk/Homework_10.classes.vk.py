from pprint import pprint
import requests


class Vk_api:
    URL = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }

    def get_id(self):
        my_id = requests.get(self.URL + 'users.get', params={**self.params})
        my_id.raise_for_status()
        return my_id.json()['response'][0]['id']

    def friends_getMutual(self, target_id,  my_id=None):
        params = {
            'source_uid': my_id,
            'target_uid': target_id
        }
        res = requests.get(self.URL + 'friends.getMutual', params={**self.params, **params})
        res.raise_for_status()
        return res.json()

    def __and__(self, other):
        return self.friends_getMutual(other.get_id())

    def __str__(self):
        return 'vk.com/id' + str(self.get_id())


if __name__ == '__main__':
    VERS = 5.131
    vk_1 = Vk_api(TOKEN1, VERS)
    vk_2 = Vk_api(TOKEN2, VERS)

    print(vk_1 & vk_2)




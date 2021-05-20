import requests

class Meme:

    def getMeme(self):
        response = requests.get('https://meme-api.herokuapp.com/gimme')

        if response.status_code != 200:
            raise ApiError('GET /tasks/ {}'.format(response.status_code))

        return str(response.json()['url'])

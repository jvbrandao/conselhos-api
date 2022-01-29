import requests


def conselho(self):
    r = requests.get('https://api.adviceslip.com/advice')
    advices = r.json()
    self.advice = advices['slip']['advice']

    return self.advices
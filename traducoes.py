import json
import requests


def traducao(self, frase):
    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "deep-translate1.p.rapidapi.com",
        'x-rapidapi-key': "3c95f575b5mshd769d9cb61ce258p1165e4jsne444235f252b"
    }
    payload = json.dumps(
        {
            "q": f"{frase}",
            "source": "en",
            "target": "pt"
        }
    )
    try:
        response = requests.post(url, headers=headers, data=payload,)
        self.data = response.json()
        return self.data['data']['translations']['translatedText']

    except Exception as E:
        print(E)

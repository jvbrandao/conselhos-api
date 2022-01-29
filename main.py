import requests
import json


r = requests.get('https://api.adviceslip.com/advice')
advices = r.json()
advice = advices['slip']['advice']
print(advice)

url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"
headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "deep-translate1.p.rapidapi.com",
    'x-rapidapi-key': "3c95f575b5mshd769d9cb61ce258p1165e4jsne444235f252b"
}
payload = json.dumps(
    {
        "q": f"{advice}",
        "source": "en",
        "target": "pt"
    }
)
try:
    response = requests.post(url, headers=headers, data=payload,)
    data = response.json()
    print(data['data']['translations']['translatedText'])

except Exception as E:
    print(E)

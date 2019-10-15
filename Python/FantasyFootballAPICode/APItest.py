import json, requests


url = "https://www.fantasyfootballnerd.com/service/players/json/q283cs7srcvj/"
r = requests.post(url)
response = json.loads(r.text)
print(response)


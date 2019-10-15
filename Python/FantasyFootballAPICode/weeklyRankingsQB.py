import json,requests,mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
database = "mydb"
)
cursor = mydb.cursor()

url = "https://www.fantasyfootballnerd.com/service/weekly-rankings/json/q283cs7srcvj/QB/4/1"

r = requests.post(url)
response = json.loads(r.text)
players = response['Rankings']
count = 0

for i in range(15):
    query = "INSERT INTO weeklyrankingsqb (name, team, standard, ppr, injury) VALUES (%s,%s,%s,%s,%s)"
    val = [
    str(players[i]['name']),
    str(players[i]['team']),
    str(players[i]['standard']),
    str(players[i]['ppr']),
    str(players[i]['injury']),
    ]
    cursor.execute(query, val)
    count += 1
mydb.commit()

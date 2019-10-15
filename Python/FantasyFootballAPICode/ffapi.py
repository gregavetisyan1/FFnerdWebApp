import json,requests,mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
database = "mydb"
)
cursor = mydb.cursor()

url = "https://www.fantasyfootballnerd.com/service/schedule/json/q283cs7srcvj"

r = requests.post(url)
response = json.loads(r.text)
games = response['Schedule']
count = 0
for i in range(len(games)):
    query = "INSERT INTO 2019nflschedule (gameWeek, awayTeam, homeTeam, gameTimeET, tvStation, gameDate) VALUES (%s, %s, %s, %s, %s, %s)"

    val = [
    str(games[i]['gameWeek']),
    str(games[i]['awayTeam']),
    str(games[i]['homeTeam']),
    str(games[i]['gameTimeET']),
    str(games[i]['tvStation']),
    str(games[i]['gameDate'])
    ]
    cursor.execute(query, val)
    count += 1
mydb.commit()


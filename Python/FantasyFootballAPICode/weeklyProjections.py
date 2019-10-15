import json,requests,mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
database = "mydb"
)
cursor = mydb.cursor()

url = "https://www.fantasyfootballnerd.com/service/weekly-projections/json/q283cs7srcvj/RB/5/"

r = requests.post(url)
response = json.loads(r.text)
players = response['Projections']
count = 0
for i in range(15):
    query = "INSERT INTO weeklyprojectionsrb (rushAtt, rushYds, rushTD, recYds, displayName, team) VALUES (%s,%s,%s,%s,%s,%s)"
    
    val = [
    str(players[i]['rushAtt']),
    str(players[i]['rushYds']),
    str(players[i]['rushTD']),
    str(players[i]['recYds']),
    str(players[i]['displayName']),
    str(players[i]['team'])
    ]
    cursor.execute(query, val)
    count += 1
mydb.commit()




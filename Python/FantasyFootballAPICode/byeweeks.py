import json,requests,mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
database = "mydb"
)
cursor = mydb.cursor()


url = "https://www.fantasyfootballnerd.com/service/byes/json/q283cs7srcvj/"

r = requests.post(url)

response = json.loads(r.text)
bw = response['Bye Week 12']
count = 0
for i in range(len(bw)):

    query = "INSERT INTO byeweek (byeWeek, team, displayName) VALUES (%s, %s, %s)"
    val = [
    str(bw[i]['byeWeek']),
    str(bw[i]['team']),
    str(bw[i]['displayName']),
    ]
    cursor.execute(query, val)
    count += 1
mydb.commit()

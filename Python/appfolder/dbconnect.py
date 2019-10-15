import mysql.connector
from mysql.connector import Error
from newsapi import NewsApiClient
import requests
import json

def week():
    try:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "mydb"
    )
        weekQuery = "SELECT * FROM 2019nflschedule"
        cursor = mydb.cursor()
        cursor.execute(weekQuery)
        schedule = cursor.fetchall()
        gameList = []
        print("Total number of rows in 2019nflschedule is: ", cursor.rowcount)
        for games in schedule:
            gameList.append(games)
        return gameList    
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if(mydb.is_connected()):
            print("MySQL connection is connected")
    
    """      if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = mydb.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Your connected to database: ", record)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (mydb.is_connected()):
            cursor.close()
            mydb.close()
            print("MySQL connection is closed") 
            """
def weeklyRankingRB():
    try:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "mydb"
    )
        rankQuery = "SELECT * FROM weeklyrankingsrb"
        cursor = mydb.cursor()
        cursor.execute(rankQuery)
        rankings = cursor.fetchall()
        rankList = []
        for players in rankings:
            rankList.append(players)
        return rankList
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if(mydb.is_connected()):
            print("MySQL connection is connected")

def weeklyRankingQB():
    try:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "mydb"
    )
        rankQuery = "SELECT * FROM weeklyrankingsqb"
        cursor = mydb.cursor()
        cursor.execute(rankQuery)
        rankings = cursor.fetchall()
        rankList = []
        for players in rankings:
            rankList.append(players)
        return rankList
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if(mydb.is_connected()):
            print("MySQL connection is connected")

def weeklyRankingWR():
    try:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "mydb"
    )
        rankQuery = "SELECT * FROM weeklyrankingswr"
        cursor = mydb.cursor()
        cursor.execute(rankQuery)
        rankings = cursor.fetchall()
        rankList = []
        for players in rankings:
            rankList.append(players)
        return rankList
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if(mydb.is_connected()):
            print("MySQL connection is connected")

def byeWeek():
    try:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "mydb"
    )
        byeWeekQuery = "SELECT * FROM byeweek"
        cursor = mydb.cursor()
        cursor.execute(byeWeekQuery)
        byeWeeks = cursor.fetchall()
        byeWeekList = []
        for games in byeWeeks:
            byeWeekList.append(games)
        return byeWeekList
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if(mydb.is_connected()):
            print("MySQL connection is connected")

def news():
    url = "https://newsapi.org/v2/everything?sources=nfl-news&sortBy=publishedAt&apiKey=19bd266db0094bc9b20fffac8d5352a7"

    r = requests.get(url)
    response = json.loads(r.text)
    news = response['articles']

    newsList = []

    for i in range(len(news)):
        newsList = [
        str(news[i]['author']),
        str(news[i]['title']),
        str(news[i]['content']),
        str(news[i]['publishedAt'])
        ]
    return newsList
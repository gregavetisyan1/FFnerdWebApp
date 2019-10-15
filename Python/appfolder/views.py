from flask import Flask, url_for
from flask import render_template, redirect, request
from . import app
import mysql.connector
from mysql.connector import Error
from dbconnect import week
from dbconnect import byeWeek
from dbconnect import weeklyRankingRB
from dbconnect import weeklyRankingQB
from dbconnect import weeklyRankingWR
from dbconnect import news
import requests


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search/", methods=['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route("/homeGames")
def homeGames():
    gameList = week()
    return render_template("homeGames.html", gameList=gameList)

@app.route("/byeWeeks")
def byeWeeks():
    byeWeekList = byeWeek()
    return render_template("byeWeeks.html", byeWeekList=byeWeekList)

@app.route("/weeklyRanksRB")
def weeklyRankingsRB():
    rankList = weeklyRankingRB()
    return render_template("weeklyRankingsRB.html", rankList=rankList)

@app.route("/weeklyRanksQB")
def weeklyRankingsQB():
    rankList = weeklyRankingQB()
    return render_template("weeklyRankingsQB.html", rankList=rankList)

@app.route("/weeklyRanksWR")
def weeklyRankingsWR():
    rankList = weeklyRankingWR()
    return render_template("weeklyRankingsWR.html", rankList=rankList)

@app.route("/news")
def FBnews():
    newsList = news()
    return render_template("news.html", newsList=newsList)

@app.route("/results/")
def search_results(weekNumber):
    if request.method == "POST":
        gameList = week()
        return render_template("results.html", gameList = gameList)
    

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

""" @app.route("/search/", methods=['POST', 'GET'])
def search():
    form = SearchForm()
    weekNumber = form.weekNumber.data
    if request.method == "POST":
        results = week(weekNumber)
        return render_template("search.html", form=form, weekNumber=weekNumber, results=results)
        #return redirect(url_for('search_results', weekNumber=weekNumber))
    return render_template("search.html", form=form)
 """
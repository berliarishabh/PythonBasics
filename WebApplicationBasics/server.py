#!/usr/bin/env python3
#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : server.py
#date : 2016.10.23
#purpose : Using Flask, read a file, query a database, take value from user, post it and use it to query a database.
#version: 1.0.0
#features: Error handling, BootstrapCSS
#dependencies: the following directories (/template /static) are required for the templates to load and Bootstrap to work



from flask import Flask, render_template, Markup, request
import os, sys, sqlite3

app = Flask(__name__)


#function to read file, find the line with max. length, print length and the line
def readFile(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()
        list = [i.strip() for i in lines]
    return list

#function to get entire database
def queryDB(db):
    db = sqlite3.connect(db)
    db.row_factory = sqlite3.Row
    query = "select * from planets"
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

#function to get row of database where columun is passed by user
def queryResults(db, planetName):
    db = sqlite3.connect(db)
    query = "select * from planets where name=?"
    t = (planetName.lower(),)
    cursor = db.cursor()
    cursor.execute(query,t)
    rows = cursor.fetchall()
    return rows
#home-page
@app.route('/')
def index():
    return render_template('index.html')

#read file1.txt page
@app.route('/readfile')
def readFilePage():
    lineList = readFile('file1.txt')
    #return "<pre>%s<br></pre>" % Markup.escape(f)
    return render_template('template.html',lineList=lineList)

#Query Database page
@app.route('/planetsDB')
def queryDBPage():
    dbList = queryDB('planetsDB.sq3')
    return render_template('template.html',dbList=dbList)

#Query Database with name page
@app.route('/planetsDB/name')
#Show form first and take input.
def myform():
    form = 1;
    return render_template('template.html',form=form)

@app.route('/planetsDB/name', methods=['GET','POST'])
def myform_post():
    dbList = request.form['myVar']
    planetName = queryResults('planetsDB.sq3',dbList)
    if planetName:
        return render_template('template.html',planetName=planetName)
    else:
        return render_template('error.html',dbList=dbList)


#error handling
@app.errorhandler(404)
@app.errorhandler(500)
@app.errorhandler(401)
def errorpage(e):
    return render_template('error.html')



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)

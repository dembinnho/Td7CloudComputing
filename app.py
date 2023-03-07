# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:19:55 2023

@author: layss
"""
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongo-td6:27017/")


db = client.mydb

# Get a reference to mycollection
collection = db.mycollection

@app.route('/')
def index():
    with open('file.txt', 'r') as file:
        firstContent = file.read()
        
        secondContent = list(collection.find())
        secondContent = str(secondContent)
        
    return render_template('index.html', firstContent=firstContent, secondContent=secondContent)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

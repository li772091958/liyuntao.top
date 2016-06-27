#!/usr/bin/env python
# coding=utf-8

from flask import Flask, render_template
from bs4 import BeautifulSoup

from html import post
from getAllImgsName import getNames

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    user = { 'nickname': 'Miguel' }
    
    lofterHtml = post('http://li772091958.lofter.com',{"pageIndex":1})
    soup = BeautifulSoup(lofterHtml)
    imgs = soup.find_all("img")
    return render_template('home.html',
                           user = user,
                           imgs = imgs)
    
@app.route('/', methods=['GET', 'POST'])
def index():
    imgs = getNames()
    return render_template('index.html', imgs = imgs)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

#!/usr/bin/env python
# coding=utf-8

from flask import Flask, render_template
from html import post
from bs4 import BeautifulSoup

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
    imageName = range(1001,1100)
    imgs = []
    for item in imageName:
        imgs.append('static/images/show/'+str(item)+'.jpg')
    return render_template('index.html', imgs = imgs)

if __name__ == '__main__':
    app.run()

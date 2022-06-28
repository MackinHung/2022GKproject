from flask import Flask, request, jsonify,render_template,url_for
from flask_cors import CORS
import numpy as np
import requests as req
import pandas as pd
from requests_html import HTML
import re
import random
import json
from bs4 import BeautifulSoup
from openpyxl import Workbook
from time import sleep
# from wait import wait_crawler
app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

@app.route('/',methods=['POST','GET'])
@app.route('/home',methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/crawler',methods=['POST','GET'])
def test1():
    if request.method =='POST':
        if request.values['send']=='送出':
            global keyword
            global page_num
            global year_start
            global year_end
            keyword=request.values['keyword']
            page_num=request.values['page_num']
            year_start=request.values['year_start']
            year_end=request.values['year_end']
            if page_num == '':
                page_num = 10
            if year_start == '':
                year_start = 2019
            if year_end == '':
                year_end = 2022
            return render_template('crawler2.html',name="爬蟲中請稍候") #等待頁面
    return render_template('crawler1.html',name="") #爬蟲頁面

@app.route('/test2',methods=['POST','GET'])
def test2():
    from crawler_all import crawler_all
    crawler_all(keyword,page_num,year_start,year_end)
    return render_template('crawler3.html',name="下載成功囉!!") #完成頁面

@app.route('/test3',methods=['POST','GET'])
def test3():
    return render_template('crawler3.html') #完成頁面

@app.route('/analysis',methods=['POST','GET'])
def test_a():
    if request.method =='POST':
        if request.values['send']=='送出':
            global keyword_png
            global brand1
            global brand2
            global brand3
            global brand4
            global brand5
            global brand6
            global brand7
            global brand8
            global brand9
            global brand10

            keyword_png=request.values['keyword_png']
            brand1=request.values['brand1']
            brand2=request.values['brand2'] 
            brand3=request.values['brand3']
            brand4=request.values['brand4'] 
            brand5=request.values['brand5']
            brand6=request.values['brand6']
            brand7=request.values['brand7']
            brand8=request.values['brand8'] 
            brand9=request.values['brand9']
            brand10=request.values['brand10']
            return render_template('png2.html',name="畫圖中請稍候") #等待頁面
    return render_template('png1.html',name="") #爬蟲頁面

@app.route('/test_b',methods=['POST','GET'])
def test_b():
    from png_all import png_all
    png_all(keyword_png,brand1,brand2,brand3,brand4,brand5,brand6,brand7,brand8,brand9,brand10)
    return render_template('png3.html',name=keyword_png) #完成頁面

@app.route('/test_c',methods=['POST','GET'])
def test_c():
    return render_template('png3.html') #完成頁面

@app.route('/')
def index():
    return "Hello World with flask"
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=5000)
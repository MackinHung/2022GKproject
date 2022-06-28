from flask import Flask, request, jsonify,render_template,url_for
from flask_cors import CORS
import numpy as np
import requests as req
import pandas as pd
from requests_html import HTML
import re
import random
import time
import json
from bs4 import BeautifulSoup
from openpyxl import Workbook

app = Flask(__name__)
CORS(app)
# app.config["DEBUG"]=True

@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index2.html')

@app.route('/analysis',methods=['POST','GET'])
def analysis():
    if request.method =='POST':
        if request.values['send']=='送出':
            keyword=request.values['user']
            from png_all import png_all
            png_all(keyword=keyword)
            return render_template('analysis.html',name="不給你看!!",keyword=keyword)    
    return render_template("analysis.html",name="")

@app.route('/crawler',methods=['POST','GET'])
def crawler():
    if request.method =='POST':
        if request.values['send']=='送出':
      
            keyword=request.values['user']
            from crawler_all import crawler_all
            crawler_all(keyword=keyword)
            
            return render_template('crawler.html',name="下載成功自己去找!!")
    return render_template('crawler.html',name="")
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=5000)

# Flask 설치
# https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html 공식문서
from urllib.parse import urlencode
import requests
import pandas as pd
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET

from flask import Flask
# sercer01의 내용을 접목 시킨다
url = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline'
response1 = requests.get(url)

url2 = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
params2 ={'serviceKey' : '/+==', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'XML', 'dataCd' : 'ASOS', 'dateCd' : 'DAY', 'startDt' : '20100101', 'endDt' : '20100601', 'stnIds' : '108' }
response2 = requests.get(url2, params=params2)

app = Flask(__name__)

# 태그 사용가능
@app.route('/')
def hello_world():
    return '<h2>Hel World!</h2>'

@app.route('/make')
def make():
    return response1.content

@app.route('/data')
def data():
    return response2.content

# 실행
# if __name__ == '__main__':
#     app.run()

# 디버깅 실행
app.run(debug=True)


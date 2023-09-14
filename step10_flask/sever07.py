import random
from urllib.parse import urlencode
import requests
import pandas as pd
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET

from flask import Flask

app = Flask(__name__)

# 태그 사용가능
menu = [
    {'id':1,'title':'HTML','body':'html is ...'},
    {'id':2,'title':'CSS','body':'css is ...'},
    {'id':3,'title':'JS','body':'javascript is ...'}
]
@app.route('/')
def index():
    liTags =""
    for i in menu:
        # f-String: f''
        # 문자열 앞에 f를 붙인다
        # 문자열 중간에 변수나 계산식을 넣을 수 있다{}
        liTags = liTags + f'<li><a href="/read/{["id"]}">{i["title"]}</a></li>'


    return f'''
     <!doctype html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                <ol>
                    {liTags}
                </ol>
                <h2>Welcome</h2>
                Hello, Web
            </body>
        </html>
    '''

@app.route('/create')
def create():
    return '<h2> Create </h2>'

# 파라미터는 String인데 int로 변경 해준다 <int: id>
@app.route('/read/<int:id>')
def read(id):
    liTags =""
    for i in menu:
        liTags = liTags + f'<li><a href="/read/{["id"]}">{i["title"]}</a></li>'

    title =''
    body =''
    for i in menu:
        if id == i['id']:
            title = i['title']
            body = i['body']
            break
    return f'''
    <!doctype html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                <ol>
                    {liTags}
                </ol>
                <h2>{title}</h2>
                {body}
            </body>
        </html>
'''

    return '<h2> Read %s </h2>' %id


# 디버깅 실행
app.run(debug=True)


# Flask 설치
# https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html 공식문서

from flask import Flask
app = Flask(__name__)

# 태그 사용가능
@app.route('/')
def hello_world():
    return '<h2>Hel World!</h2>'

@app.route('/make')
def make():
    return 'Hel make!'

@app.route('/data')
def data():
    return 'Hel data!'

# 실행
# if __name__ == '__main__':
#     app.run()

# 디버깅 실행
app.run(debug=True)


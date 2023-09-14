from flask import Flask, send_from_directory


app = Flask(__name__)

# 태그 사용가능
@app.route('/')
def hello_world():
    return send_from_directory('html','index.html')

@app.route('/<path:name>')
def start(name):
    return send_from_directory('html',name)

# 디버깅 실행
app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/hello')
def hello():    # 위에 (hello) 쓰면 함수명도 hello쓰는게 일반적
    return render_template('01.hello.html')

if __name__ == '__main__':
    app.run(debug=True)

# 1. cmd창에 > python 01.app.py 실행
# 2. 웹페이지 주소창에> localhost:5000 입력 --> Hello Flask
# 3. localhost:5000/hello 입력 --> Hello World!
# 파일저장확인/ 웹안되면 cmd죽었는지 확인, 살리기
# url 틀리면 404에러(Not Found)뜸

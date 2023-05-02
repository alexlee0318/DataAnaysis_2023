from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/hello')
def hello():    # 위에 (hello) 쓰면 함수명도 hello쓰는게 일반적
    return render_template('01.hello.html')

@app.route('/login', methods=['GET', 'POST'])   # methods 복수로
def login():
    if request.method == 'GET':
        return render_template('02.login.html') # 페이지 띄워줌
    else:    # 'POST'이면
        return '환영합니다.'    # 페이지에 표시
    
if __name__ == '__main__':
    app.run(debug=True)

# 1. cmd창에 > python 02.app.py 실행
# 2. 웹페이지 주소창에> localhost:5000/login 입력 --> login창 뜸
# 3. ID, PSW 아무거나 입력 --> 환영합니다.
# 웹오류시 확인: 파일저장/ cmd에 파일명/ cmd죽었는지 확인, 살리기(1번 재실행)
# url 틀리면 404에러(Not Found)뜸

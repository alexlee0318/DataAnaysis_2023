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
    
@app.route('/user/<uid>')   # localhost:5000/user/james --> 'james'
def user(uid):
    return f'<h1>{uid}</h1>'

@app.route('/int/<int:number>') # localhost:5000/int/256 --> 256
def int_fn(number):
    return f'<h1>{number}</h1>'

@app.route('/float/<float:pi>') # localhost:5000/float/1.256 --> 1.256
def float_fn(pi):
    return f'<h1>{pi}</h1>'

# 사용자가 localhost:5000/add/4/and/5 입력
@app.route('/add/<int:a>/and/<int:b>')  # and를 써서 파라미터 2개 이상 전달 가능
def add(a, b):
    return f'<h1>{a} + {b} = {a+b}</h1>'

if __name__ == '__main__':
    app.run(debug=True)

# * 라우팅....주소영역 안에 parameter passing해주는 방법. /를 사용한 요즘 최신방식(옛날엔 ?).

# 1. cmd창에 > python 03.route.py 실행
# 2. 웹페이지 주소창에> localhost:5000/user/james 입력 --> 'james' 뜸
# 3. ID, PSW 아무거나 입력 --> 환영합니다.
# 웹오류시 확인: 파일저장/ cmd에 파일명/ cmd죽었는지 확인, 살리기(1번 재실행)
# url 틀리면 404에러(Not Found)뜸

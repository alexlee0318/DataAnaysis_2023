from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/hello')
def hello():    # 위에 (hello) 쓰면 함수명도 hello쓰는게 일반적
    return render_template('01.hello.html')

# 아무런 얘기 없으면 GET방식
# localhost:5000/area?pi=3.14&radius=5
@app.route('/area') # 브라우저가 요청한 값을 서버가 알아내서 가져옴
def area():
    pi = request.args.get('pi', '3.14159')  # http://localhost:5000/area?radius=10
    radius = request.values['radius']
    a = float(pi) * float(radius) ** 2
    return f'<h1>pi={pi}, radius={radius}, area={a}</h1>'

@app.route('/login', methods=['GET', 'POST'])   # methods 복수로
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:    # 'POST'이면
        uid = request.form['uid']
        pwd = request.values['pwd'] # args는 못 씀
        return f'<h1>uid={uid}, pwd={pwd}</h1>' 
            # localhost:5000/login --> uid=alex, pwd=1234
    
if __name__ == '__main__':
    app.run(debug=True)

# 웹오류시 확인: 파일저장/ cmd에 파일명/ cmd죽었는지 확인, 살리기(1번 재실행)
# url 틀리면 404에러(Not Found)뜸

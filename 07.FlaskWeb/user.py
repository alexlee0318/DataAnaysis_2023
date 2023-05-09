from flask import Blueprint, request, render_template, session
from flask import redirect, flash   # flash: 팝업창 띄우기
import hashlib, base64, json

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/login', methods=['GET', 'POST'])    # localhost:5000/user/login 이 처리되는 곳
def login():
    if request.method == 'GET':
        return render_template('prototype/user/login.html')
    else:
        uid = request.form['uid']
        pwd = request.form['pwd']
        with open('static/data/passsword.txt') as f:
            s = f.read()
        passwords = json.loads(s)
        try:
            db_pwd = passwords[uid]
            pwd_sha256 = hashlib.sha256(pwd.encode())
            hashed_pwd = base64.b64encode(pwd_sha256.digest()).decode('utf-8')
            if hashed_pwd == db_pwd:
                flash('환영합니다!')        # 초기화면으로 보내줌
                session['uid'] =uid         # 세션값 설정-> 사용자가 로그인하였음을 알게 해줌
                return redirect('/')
            else:
                flash('비밀번호가 틀립니다.')   # 로그인 화면을 다시 보내줌
                return redirect('/user/login')
        except:
            flash('등록되지 않은 ID입니다. 회원가입페이지로 이동합니다.')
            return redirect('/user/register')
        
@user_bp.route('/logout')
def logout():
    session.pop('uid', None)        # 설정한 세션값을 삭제
    return redirect('/')
        
@user_bp.route('/register')
def register():
    return render_template('prototype/user/register.html')
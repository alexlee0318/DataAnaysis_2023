import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method =='GET':
        return render_template('14.file.html')
    else:
        file_image = request.files['image']
        filename = os.path.join(app.static_folder, f'upload/{file_image.filename}') # img/비숑숑.jpg -> 비숑숑이 파일이름이 됨 
        file_image.save(filename) # 저장
        return render_template('14.file_res.html', fname=f'upload/{file_image.filename}')   #fname이란 형태로 이미지 보기

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
import crawl_util as cu

# 인터파크 베스트셀러
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')    
def index():
    return 'Hello Flask'

@app.route('/interpark', methods=['GET'])
def interpark():
    book_list = cu.interpark()  # rendering parameter
    return render_template('11.interpark.html', book_list=book_list)

    
if __name__ == '__main__':
    app.run(debug=True)
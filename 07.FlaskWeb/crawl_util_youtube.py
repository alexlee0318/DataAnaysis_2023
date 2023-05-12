import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from selenium import webdriver
import warnings
import time
warnings.filterwarnings('ignore')

def convert(s):
    s= s.replace('억','').replace('개','').replace(',','').replace('만','0000')
    return int(s)

def youtube():
    lines = []
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome('C:/Users/YONSAI/Downloads/chromedriver', options=options)
    for page in tqdm(range(1, 11)):
        url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=' + str(page)
        driver.get(url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        trs = soup.select('.aos-init')

        for tr in trs:
            rank = int(tr.select_one('.rank').get_text().strip())
            category= tr.select_one('.category').get_text().strip()[1:-1]
            channel = tr.select_one('h1 > a').get_text().strip()
            subs = convert(tr.select_one('.subscriber_cnt').get_text().strip())
            view = convert(tr.select_one('.view_cnt').get_text().strip())
            video = convert((tr.select_one('.video_cnt').get_text()[:-1]))
            lines.append({
                '순위': rank, '카테고리':category, '채널명':channel, 
                '구독자수':subs, '조회수':view, '비디오':video
                })
    return lines
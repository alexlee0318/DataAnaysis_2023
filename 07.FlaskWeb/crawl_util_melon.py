import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def melon():
    url = 'https://www.melon.com/chart/'
    result = requests.get(url)
    result.text

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    result = requests.get(url, headers=header)
    soup = BeautifulSoup(result.text, 'html.parser')
    trs = soup.select_one('tbody').find_all('tr')
    line=[]
    for tr in trs:
        rank = tr.select_one('.rank').get_text()
        img = tr.select_one('.wrap > a > img')['src']
        title = tr.select_one('.ellipsis.rank01').get_text().strip()
        artist = tr.select_one('.ellipsis.rank02').find('a').get_text().strip()
        album = tr.select_one('.ellipsis.rank03').find('a').get_text().strip()
        line.append({'rank':rank, 'img':img, 'title':title, 'artist': artist, 'album':album})
    return line
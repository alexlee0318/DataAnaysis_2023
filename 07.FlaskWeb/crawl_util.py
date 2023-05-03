
# 인터파크 베스트셀러
import requests
from bs4 import BeautifulSoup

    # 크롤링> 05.인터파크 파일에서 정보 받아오기 
def interpark():
    base_url = 'http://book.interpark.com'  # 책페이지 url앞부분 추가
    url = '/display/collectlist.do?_method=BestsellerHourNew201605&bestTp=1&dispNo=028'
    result = requests.get(base_url + url)   # url들 넣어줌
    soup = BeautifulSoup(result.text, 'html.parser')
    lis = soup.select('.rankBestContentList > ol > li')
    lines = []
    for li in lis:
        img = li.select_one('.coverImage').find('img')['src']    # 커버이미지
        href = li.select_one('.coverImage').find('a')['href']    # 커버이미지 링크
        rank_data = li.select('.rankBtn_ctrl')
        if len(rank_data) == 1:
            rank = int(rank_data[0]['class'][-1][-1])
        else:
            rank = int(rank_data[0]['class'][-1][-1] + rank_data[1]['class'][-1][-1])
        title = li.select_one('.itemName').get_text().strip()
        author = li.select_one('.author').get_text().strip()
        company = li.select_one('.company').get_text().strip()
        price = li.select_one('.price > em').get_text().strip()
        lines.append({'순위': rank, '제목':title, '저자':author, '출판사':company, 
                      '가격':price, 'img':img, 'href':base_url+href})

    return lines
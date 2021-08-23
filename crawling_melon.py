import time
import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 연결
driver = webdriver.Chrome()

# 멜론 웹 페이지 접근
driver.get('https://www.melon.com/chart/index.htm')
driver.implicitly_wait(10)

# 모~든 가사들을 모으는 리스트
all_lyrics = []


#  가사정보 크롤링 함수
def craw_lyrics():
    lyric = driver.find_elements_by_class_name('lyric')
    driver.implicitly_wait(10)

    lyrics = []

    lyrics = lyric[0].text.split('\n')

    # 공백 제거
    lyrics = list(filter(None, lyrics))

    # 영어 제거
    lyrics = list(filter(lambda i: i.upper() == i.lower(), lyrics))

    for i in lyrics:
        all_lyrics.append(i)

    print(all_lyrics)

# data-song-no를 모으는 리스트
song_num = []

lst50 = driver.find_elements_by_id('lst50')
lst100 = driver.find_elements_by_id('lst100')
for i in lst50:
    song_num.append(i.get_attribute('data-song-no'))
for i in lst100:
    song_num.append(i.get_attribute('data-song-no'))

# 상세 페이지 접근
for i in range(100):
    driver.get('https://www.melon.com/song/detail.htm?songId={song_num}'.format(song_num=song_num[i]))
    craw_lyrics()

# 데이터 프레임 생성
df = pd.DataFrame({"lyric": all_lyrics, "label": 0})

# csv 파일로 저장
df.to_csv("crawling_melon.csv",  encoding='utf-8-sig')
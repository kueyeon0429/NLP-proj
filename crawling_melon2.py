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


# 각종 리스트
titles = []  # 제목
artists = [] # 아티스트
lyrics = [] # 가사
jangleus = [] # 장르
eras = [] # 시대

# 시대 리스트
eras_list = [1990, 2000, 2010]



#  음악 정보 크롤링 함수
def craw_lyrics(era):
    # 제목 크롤링
    title = driver.find_element_by_class_name('song_name')
    titles.append(title.text)


    # 아티스트 크롤링
    artist = driver.find_element_by_class_name('artist_name')
    artists.append(artist.get_attribute('title'))


    # 가사 크롤링
    lyric = driver.find_elements_by_class_name('lyric')
    driver.implicitly_wait(10)

    tmp = []

    tmp = lyric[0].text.split('\n')
    # 공백 제거
    tmp = list(filter(None, tmp))
    # 영어 제거
    tmp = list(filter(lambda i: i.upper() == i.lower(), tmp))

    lyrics.append(' '.join(tmp)) # 다시 합침


    # 장르 크롤링
    jangleu = driver.find_element_by_xpath('//*[@id="downloadfrm"]/div/div/div[2]/div[2]/dl/dd[3]')
    jangleus.append(jangleu.text)


    # 시대
    eras.append(era)


    print(titles)
    print(artists)
    print(lyrics)
    print(jangleus)
    print(eras)


# data-song-no를 모으는 함수
def collect_no():
    song_num = []

    lst50 = driver.find_elements_by_xpath('//*[@id="lst50"]/td[1]/div/input')

    for i in lst50:
        song_num.append(i.get_attribute('value'))

    return song_num



# 곡 상세 페이지 접근 함수
def access_detail(song_num, era):
    for i in range(50):
        driver.get('https://www.melon.com/song/detail.htm?songId={song_num}'.format(song_num=song_num[i]))

        craw_lyrics(era)



# 시대별 차트 접근
for e in eras_list:
    driver.get('https://www.melon.com/chart/age/index.htm?chartType=AG&chartGenre=KPOP&chartDate={era}'.format(era=e))

    # 차트 바로보기 버튼
    driver.find_elements_by_xpath('//*[@id="cntt_chart_year"]/div/div[1]/div[1]/span/a/img')

    song_num = collect_no()

    access_detail(song_num, e)



# 데이터 프레임 생성
df = pd.DataFrame({"title": titles, "artist": artists, "lyric": lyrics, "jangleu": jangleus, "era": eras})



# csv 파일로 저장
df.to_csv("music_info.csv",  encoding='utf-8-sig')
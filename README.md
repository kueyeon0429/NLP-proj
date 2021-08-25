# 자연어처리를 이용한 노래 가사 감정분석
- [x] `2021-08-23` 멜론 가사 크롤링
- [x] `2021-08-24` 데이터 정제
- [x] `2021-08-25` 가사 감성 분류
***
`crawling_melon.py` 실행 시  
`lyrics.csv` 파일 생성  
col: 문장단위 가사, label

`crawling_melon2.py` 실행 시  
`music_info.csv` 파일 생성  
col: title, artist, lyric, genre, era

***

`word_cloud.py`  
시대별 가사의 키워드 분석  
music_info.csv 사용

**실행 전**  
- 나눔스퀘어 폰트 다운 https://hangeul.naver.com/font
- `NanumSquareR.otf` 을 같은 폴더에 위치시킴

***

`lyrics.csv` 정제 전 훈련 셋 (라벨링X..)  
`lyrics2.csv` 정제 전 시험 셋  
`data_cleaning.py` 데이터 정제, 실행 시 아래 파일 생성 

`train.csv` 훈련 셋  
`test.csv` 시험 셋

***

`sentiment_analysis.py` 감성 분류  
- [ ] `data_set > x_train_pre.csv`  패딩X  
- [ ] `data_set > x_test_pre.csv`  패딩X  
- [x] `data_set > x_train.csv`  
- [x] `data_set > x_test.csv` 
- [x] `data_set > y_train.csv` 
- [x] `data_set > y_test.csv`

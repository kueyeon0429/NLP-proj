from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

music = pd.read_csv("./music_info.csv")
music

!pip install konlpy

from konlpy.tag import Okt


# 토크나이저 생성
tokenizer = Okt()


# 특정 연대의 가사를 불러옴
lyrics_1990 = music[music['era']==1990]['lyric']
lyrics_2000 = music[music['era']==2000]['lyric']
lyrics_2010 = music[music['era']==2010]['lyric']

# 가사 형태소 기준으로 토크나이징, 명사 형용사 부사만 추출
morph_1990 = []
morph_2000 = []
morph_2010 = []

tmp_1990 = []
tmp_2000 = []
tmp_2010 = []

for lyric in lyrics_1990:
  tmp = tokenizer.pos(lyric)
  tmp_1990.append(tmp)

for lyric in lyrics_2000:
  tmp = tokenizer.pos(lyric)
  tmp_2000.append(tmp)

for lyric in lyrics_2010:
  tmp = tokenizer.pos(lyric)
  tmp_2010.append(tmp)

for i in tmp_1990:
  for word, tag in i:
    if tag in ['Noun', 'Adjective', 'Adverb'] and ("것" not in word) and ("수" not in word) and ("게" not in word):
      morph_1990.append(word)

for i in tmp_2000:
  for word, tag in i:
    if tag in ['Noun', 'Adjective', 'Adverb'] and ("것" not in word) and ("수" not in word) and ("게" not in word):
      morph_2000.append(word)

for i in tmp_2010:
  for word, tag in i:
    if tag in ['Noun', 'Adjective', 'Adverb'] and ("것" not in word) and ("수" not in word) and ("게" not in word):
      morph_2010.append(word)

morph_1990 = ' '.join(morph_1990)
morph_2000 = ' '.join(morph_2000)
morph_2010 = ' '.join(morph_2010)


# word cloud 생성
wordcloud_1990 = WordCloud(max_words=30, font_path='./NanumSquareR.otf', max_font_size=100, background_color='white').generate(morph_1990)
wordcloud_2000 = WordCloud(max_words=30, font_path='./NanumSquareR.otf', max_font_size=100, background_color='white').generate(morph_2000)
wordcloud_2010 = WordCloud(max_words=30, font_path='./NanumSquareR.otf', max_font_size=100, background_color='white').generate(morph_2010)


# word cloud 1990 출력
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud_1990, interpolation='lanczos')
plt.axis('off')
plt.show()

# word cloud 2000 출력
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud_2000, interpolation='lanczos')
plt.axis('off')
plt.show()

# word cloud 2010 출력
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud_2010, interpolation='lanczos')
plt.axis('off')
plt.show()
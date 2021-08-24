from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Embedding, LSTM, Flatten
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import plot_model
from tensorflow.keras.datasets import imdb

from IPython.display import display


## 사랑 노래인지 아닌지를 분류

lyrics = pd.read_csv("./lyrics.csv")
df_lyric = lyrics[['lyric', 'label']]
df_lyric


# 후렴구 제거
#df_lyric[1985:1990]
#df_lyric[2016:2019]
#df_lyric[2110:2114]
#df_lyric[2115:2133]
#df_lyric[2462:2464]
#df_lyric[2482:2484]
df_lyric = df_lyric.drop([i for i in (1985, 1990)])
df_lyric = df_lyric.drop([2016, 2017, 2018])
df_lyric = df_lyric.drop([i for i in (2115, 2133)])
df_lyric = df_lyric.drop([i for i in (2110, 2114)])
df_lyric = df_lyric.drop([2462, 2463])
df_lyric = df_lyric.drop([2482, 2483])
df_lyric

'''
# 후렴구 제거 lyrics2.csv
df_lyric = df_lyric.drop([i for i in (0, 3)])
df_lyric = df_lyric.drop([128, 130, 141])
df_lyric = df_lyric.drop([i for i in (194, 196)])
df_lyric = df_lyric.drop([i for i in (200, 205)])
df_lyric = df_lyric.drop([i for i in (208, 217)])
df_lyric = df_lyric.drop([i for i in (272, 274)])
df_lyric = df_lyric.drop([i for i in (292, 294)])
df_lyric = df_lyric.drop([i for i in (425, 455)])
df_lyric = df_lyric.drop([i for i in (456, 459)])
df_lyric = df_lyric.drop([i for i in (493, 496)])
df_lyric = df_lyric.drop([i for i in (498, 500)])
df_lyric = df_lyric.drop([501, 509, 513, 515])
df_lyric = df_lyric.drop([i for i in (743, 747)])
df_lyric = df_lyric.drop([i for i in (2213, 2215)])
df_lyric = df_lyric.drop([i for i in (2219, 2221)])
df_lyric = df_lyric.drop([i for i in (2223, 2226)])
df_lyric = df_lyric.drop([i for i in (2228, 2230)])
df_lyric = df_lyric.drop([2232, 2362, 2364, 2586, 2620])
df_lyric = df_lyric.drop([i for i in (2621, 2624)])
'''


# 중복 행 제거
df_lyric = df_lyric.drop_duplicates()
df_lyric



# 한 글자만 있는 행 제거

for i in df_lyric['lyric']:
  tmp = i.split(' ')
  if len(tmp) <= 1:
    df_lyric = df_lyric.drop(df_lyric[df_lyric['lyric']==i].index)

df_lyric

df_lyric.to_csv("train.csv",  encoding='utf-8-sig')

'''
# 시험 셋
df_lyric.to_csv("test.csv",  encoding='utf-8-sig')
'''
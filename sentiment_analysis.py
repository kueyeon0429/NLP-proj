import pandas as pd
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
import urllib.request
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# 토크나이저 생성
tokenizer = Okt()


train_data = pd.read_csv("./train.csv")
test_data = pd.read_csv("./test.csv")


# x_train 토큰나이징
x_train = []

for lyric in train_data['lyric']:
  tmp_x = []
  tmp = tokenizer.pos(lyric)
  for word, tag in tmp:
    if tag in ['Noun', 'Adjective', 'Adverb', 'Verb'] and ("것" not in word) and ("수" not in word) and ("게" not in word):
        tmp_x.append(word)
  x_train.append(tmp_x)

# x_test 토큰나이징
x_test = []

for lyric in test_data['lyric']:
  tmp_x = []
  tmp = tokenizer.pos(lyric)
  for word, tag in tmp:
    if tag in ['Noun', 'Adjective', 'Adverb', 'Verb'] and ("것" not in word) and ("수" not in word) and ("게" not in word):
        tmp_x.append(word)
  x_test.append(tmp_x)



# 정수 인코딩
tokenizer = Tokenizer()
tokenizer.fit_on_texts(x_train)
tokenizer.word_index



# 단어의 수
vocab_size = len(tokenizer.word_index)


# text seq to int seq
tokenizer = Tokenizer(vocab_size)
tokenizer.fit_on_texts(x_train)
x_train = tokenizer.texts_to_sequences(x_train)
x_test = tokenizer.texts_to_sequences(x_test)


# y_train, y_test
y_train = np.array(train_data['label'])
y_test = np.array(test_data['label'])


# 길이 확인
plt.hist([len(s) for s in x_train], bins=50)
plt.xlabel('length of samples')
plt.ylabel('number of samples')
plt.show()

# 패딩
x_train = pad_sequences(x_train, maxlen = 6)
x_test = pad_sequences(x_test, maxlen = 6)


# 훈련 셋 저장
df_x_train = pd.DataFrame(x_train)
df_y_train = pd.DataFrame(y_train)
df_x_test = pd.DataFrame(x_test)
df_y_test = pd.DataFrame(y_test)

df_x_train.to_csv("x_train.csv",  encoding='utf-8-sig')
df_y_train.to_csv("y_train.csv",  encoding='utf-8-sig')
df_x_test.to_csv("x_test.csv",  encoding='utf-8-sig')
df_y_test.to_csv("y_test.csv",  encoding='utf-8-sig')


# 컴파일 및 학습
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

checkpoint_callback = ModelCheckpoint("best_model.h5",
                                      save_best_only=True,
                                      monitor="val_loss")

hist = model.fit(x_train, y_train, epochs=15, batch_size=64,
                 validation_split=0.2,
                 callbacks=[checkpoint_callback])

# 시각화
%matplotlib inline
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')
loss_ax.set_ylim([-0.2, 1.2])

acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')
acc_ax.plot(hist.history['val_accuracy'], 'g', label='val acc')
acc_ax.set_ylim([-0.2, 1.2])

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()


# 정확도 확인
loaded_model = load_model('best_model.h5')
print("\n 테스트 정확도: %.4f" % (loaded_model.evaluate(x_test, y_test)[1]))
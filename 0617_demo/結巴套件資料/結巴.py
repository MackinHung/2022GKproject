import requests # 訪問
from bs4 import BeautifulSoup # 網頁解析
import jieba
from collections import Counter # 次數統計
# coding=utf-8
import re
from tkinter import font
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy
from PIL import Image # 圖片轉array陣列
#Python - 知名 Jieba 中文斷詞工具教學
# https://blog.kennycoder.io/2020/02/12/Python-%E7%9F%A5%E5%90%8DJieba%E4%B8%AD%E6%96%87%E6%96%B7%E8%A9%9E%E5%B7%A5%E5%85%B7%E6%95%99%E5%AD%B8/

filename = '/Users/bryant/Desktop/0510_Demo程式碼/寶寶米餅.txt'
with open(filename, encoding="utf-8", errors='ignore') as f:
    text = f.read()
# 設定分詞資料庫
# https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big 右鍵另存放目錄下
jieba.set_dictionary('/Users/bryant/Desktop/0510_Demo程式碼/0504文字雲/dict.txt.big')

# 將自己常用的詞加入字典
jieba.load_userdict('/Users/bryant/Desktop/0510_Demo程式碼/0504文字雲/userDict.txt')

# # 新增及刪除常用詞
# jieba.add_word('心錯') # 加入心錯
# jieba.add_word('誤減') # 加入誤減
# jieba.del_word('抵抗力') # 刪除抵抗力

# 斷句方式
# 用jieba.lcut(text, cut_all=False)直接返回list
# segs = jieba.cut(text, cut_all=False) # 預設模式
# segs = jieba.cut(text, cut_all=True) # 全切模式 切的很碎
seg_list = jieba.lcut(text, cut_all=False) # lcut直接返回list
words = " ".join(seg_list)

# print(seg_list)

# print('預設:', '|'.join(jieba.cut(text, cut_all=False, HMM=True)))
# print('全關閉:', '|'.join(jieba.cut(text, cut_all=False, HMM=False)))
# print('全關閉:', '|'.join(jieba.cut(text, cut_all=True, HMM=True)))
# print('搜尋引擎模式:', '|'.join(jieba.cut_for_search(text)))


# 統計分詞出現次數
dictionary = Counter(seg_list)
# print(dictionary)
# x = dictionary.most_common()
# print(x[0])

# # 移除停用詞
stopwords = ['，','\n', '│', '\u3000', '！', '「', '」', ' ', '、','？',
            '：','的','。','/','有','在','使用','.','！','於','我','了','就',
            '表示','是','它','級','都','TVBS',':','會','也','&','nbsp','為','、'
            '快點','吃','及','用','要','最','以上','後','\xa0','～','想','年',
            '新聞網','2021',' ','但','說','tvbs','com','tw','月','（','）',
            '而且','被','讓','這樣','等','看','仍','你','他','你們','他們','我們'
            ]  # 定義停用詞
[dictionary.pop(x, None) for x in stopwords] # 存字典裡刪除停用詞
x=dictionary.keys()
y=str(x)
z=y.replace('dict_keys','').replace('keys','').replace('dict','')

# #將調整過後的文字寫成txt檔案
path = 'output.txt'
with open(path, 'w') as f:
    f.write(z)

# print(type(dictionary))
# print(type(x))
# print(type(y))
# print(y)
# stopwords =['TVBS','nbsp','產品']
for del_word in stopwords:
    jieba.del_word(del_word) # 刪除抵抗力


import jieba.analyse
tags = jieba.analyse.extract_tags(text, 20)
# print ( ",".join(tags))
# #10筆最常出現的字
# #營養師,益生菌,發現,過敏,重症,疫苗,好得快,標題,爆發國,最愛吃十種
# #刪除過後
# #營養師,益生菌,過敏,疫苗,專家選,抗新冠,確診,大對策,睡覺,這飲品
# #tags = jieba.analyse.extract_tags(news, topK=5, withWeight=True)
# # jieba.analyse.extract_tags 主要有以下的參數：
# # sentence 為句子
# # topK 代表返回 TF-IDF 權重最大的關鍵字，默認為 20
# # withWeight 代表是否返回關鍵字權重值，默認為 False
# # allowPOS 代表指定詞性，默認為空，也就是不篩選

# # Jieba 詞性標註功能
# words = jieba.posseg.cut('我喜歡睡覺')
# for word, flag in words:
#     print(f'{word} {flag}')

filename = '/Users/bryant/Desktop/0510_Demo程式碼/output.txt'
with open(filename, encoding="utf-8", errors='ignore') as f:
    text2 = f.read()

# 斷句方式
# 用jieba.lcut(text, cut_all=False)直接返回list
# segs = jieba.cut(text, cut_all=False) # 預設模式
# segs = jieba.cut(text, cut_all=True) # 全切模式 切的很碎
seg_list = jieba.lcut(text2, cut_all=False) # lcut直接返回list
words = " ".join(seg_list)



#背景顏色預設黑色，改為白色、使用指定字體
font_path='/Users/bryant/Desktop/0510_Demo程式碼/0504文字雲/SourceHanSansTW-Regular.otf'
mask = numpy.array(Image.open('/Users/bryant/Desktop/0510_Demo程式碼/0504文字雲/Tsmc.svg.png')) # 遮罩
mask=(mask==0)*255 # 把舉證等於0的地方變成255 原本有數字的地方變0
# myWordClode = WordCloud(
#     background_color='white',
#     font_path=font_path,
#     # mask=mask,
#     margin=2, # 文字間距
#     max_words=200, # 取多少文字在裡面
#     width=100, height=80, # 長寬解析度
#     ).generate(words)
myWordClode = WordCloud(background_color='white',
                        font_path=font_path).generate(words)

# 用PIL顯示文字雲
plt.imshow(myWordClode)
plt.axis("off")
plt.show()

# 儲存結果圖
myWordClode.to_file('寶寶米餅3_TVBS_word_cloud.png')

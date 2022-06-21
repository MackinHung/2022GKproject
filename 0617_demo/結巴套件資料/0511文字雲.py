from email import generator
from PIL import Image # 圖片轉array陣列
import matplotlib.pyplot as plt
import wordcloud # 文字雲
import numpy
import jieba
from collections import Counter # 次數統計

filename = '/Users/bryant/Desktop/0510_Demo程式碼/0504文字雲/0511-2.txt'
with open(filename, encoding="utf-8", errors='ignore') as f:
    text = f.read()
# 設定分詞資料庫
# https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big 右鍵另存放目錄下
jieba.set_dictionary('/Users/bryant/Desktop/0510_Demo程式碼/0504文字雲/dict.txt.big')

# 將自己常用的詞加入字典
jieba.load_userdict('/Users/bryant/Desktop/0510_Demo程式碼/0504文字雲/userDict.txt')

# seg_list = jieba.lcut(text, cut_all=False) # lcut直接返回list
# print(seg_list)
wordlist = jieba.cut(text)
words = " ".join(wordlist)
# 統計分詞出現次數
# dictionary = Counter(seg_list)
# x = dictionary.most_common()
# print(x[0])

# # 移除停用詞
# stopword = ['\n', '│', '\u3000', '！', '「', '」', ' ', '、','？','：']  # 定義停用詞
# [dictionary.pop(x, None) for x in stopword] # 存字典裡刪除停用詞
# print(dictionary)

# 格式設定
font_path = '/Users/bryant/Desktop/0510_Demo程式碼/0504文字雲/SourceHanSansTW-Regular.otf'# 設定字體格式
mask = numpy.array(Image.open('/Users/bryant/Desktop/0510_Demo程式碼/0504文字雲/Tsmc.svg.png')) # 遮罩
mask=(mask==0)*255 # 把舉證等於0的地方變成255 原本有數字的地方變0

wc = wordcloud.WordCloud(background_color='white',
                         margin=2, # 文字間距
                         mask=mask, # 遮罩 有用的話則無視設定長寬
                         font_path=font_path, # 設定字體
                         max_words=50, # 取多少文字在裡面
                         width=1080, height=720, # 長寬解析度
                         relative_scaling=0.5 # 詞頻與詞大小關聯性
                         ).generate(words)
# 生成文字雲
# wc.generate_from_frequencies(words) # 吃入次數字典資料

# 輸出
wc.to_file('my_wordcloud.png')

# 顯示文字雲
plt.imshow(wc)


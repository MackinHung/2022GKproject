# coding=utf-8
import re
from tkinter import font
import requests
import jieba
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy
from PIL import Image # 圖片轉array陣列


# class crawlerPtt():
#     def __init__(self,url,pageRange):
#         # 欲抓取的看板首頁
#         self.url = url
#         # 儲存每個標題網址
#         self.urlList = []
#         # 儲存每條留言
#         self.messageList = []

#         # 抓取首頁
#         self.get_all_href(url=self.url)

#         # 往前幾頁 抓取所有標題網址
#         for page in range(1, pageRange):
#             # 使用 GET 方式下載普通網頁
#             r = requests.get(self.url)
#             # html.parser 為解析 HTML 文件的模組
#             soup = BeautifulSoup(r.text, "html.parser")
#             # 抓取按鈕群
#             btn = soup.select('div.btn-group > a')
#             # 抓取上一頁按鈕的網址
#             up_page_href = btn[3]['href']
#             # 在網址後加上上一頁的網址
#             next_page_url = 'https://www.ptt.cc' + up_page_href
#             # 爬取上一頁內容 並更新url成上一頁的網址
#             self.url = next_page_url
#             self.get_all_href(url=self.url)

#         # 透過標題網址self.urlList抓取留言 並儲存到self.messageList最後再存下來 (邊抓邊存會漏掉很多留言)
#         self.crawlerMessage()

#     # 抓取標題網址
#     def get_all_href(self,url):
#         r = requests.get(url)
#         soup = BeautifulSoup(r.text, "html.parser")
#         # 抓取文章標題
#         results = soup.select("div.title")
#         # 尋訪每個標題 取得網址
#         for item in results:
#             a_item = item.select_one("a")
#             # 標題名稱
#             title = item.text
#             if a_item:
#                 print(title)
#                 #所要儲存的網站網址
#                 url = 'https://www.ptt.cc' + a_item.get('href')

#                 if url == 'https://www.ptt.cc/bbs/Stock/M.1422199105.A.84E.html':
#                     break

#                 # 儲存網址至佇列
#                 self.urlList.append(url)


#     # 從標題網址分析留言
#     def crawlerMessage(self):

#         # 尋訪每個標題
#         for num in range(len(self.urlList)):
#             # 建立回應
#             response = requests.get(self.urlList[num])
#             # 將原始碼做整理
#             soup = BeautifulSoup(response.text, 'lxml')
#             # 使用find_all()找尋特定目標 (推文留言)
#             articles = soup.find_all('div', 'push')

#             for article in articles:
#                 # 去除掉冒號和左右的空白
#                 messages = article.find('span', 'f3 push-content').get_text().replace(':', '').strip()
#                 # 把每個留言存起來
#                 self.messageList.append(messages)

# # 實例化爬蟲 輸入爬取看板
# url = 'https://www.ptt.cc/bbs/Stock/index.html'
# stock = crawlerPtt(url,5)

# # 爬取完成
# print('OK!')

# # 將留言逐行寫入存文字檔
# f = open('test.txt', 'w', encoding='UTF-8')
# for i in range(len(stock.messageList)):
#     # print(stock.messageList[i])
#     f.write(stock.messageList[i] + '\n')
# f.close()

# 讀取文字檔
# 如果檔案內有一些編碼錯誤，使用 errors='ignore' 來忽略錯誤
filename = '/Users/bryant/Desktop/0510_Demo程式碼/0504文字雲/0511-2.txt'
with open(filename, encoding="utf-8", errors='ignore') as f:
    text = f.read()

# 設定使用 big5 斷詞
jieba.set_dictionary('/Users/bryant/Desktop/0510_Demo程式碼/0504文字雲/dict.txt.big')
wordlist = jieba.cut(text)
words = " ".join(wordlist)
# print(words)

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
font_path='/Users/bryant/Desktop/0510_Demo程式碼/0504文字雲/SourceHanSansTW-Regular.otf').generate(words)

# 用PIL顯示文字雲
plt.imshow(myWordClode)
plt.axis("off")
plt.show()

# 儲存結果圖
myWordClode.to_file('5益生菌_TVBS_word_cloud.png')
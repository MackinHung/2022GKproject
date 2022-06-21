#完整程式碼
def pos_neg_analysis_brand(keyword):
        
    import requests # 訪問
    import jieba
    from collections import Counter # 次數統計
    import re
    from tkinter import font
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
    import numpy
    from PIL import Image # 圖片轉array陣列
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.font_manager import FontProperties
    import seaborn as sns
    import os
    #設定圖表顯示中文
    sns.set(font=['sans-serif'])
    sns.set_style("whitegrid",{"font.sans-serif":['Taipei Sans TC Beta']})
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    h=[]
    b=[]
    #設定各品牌關鍵字關鍵字

    web = 'total'
    keyword_list  = ['老協珍','田原香','農純鄉','芳茲','娘家','純煉']
    # keyword_list = ['鱸魚精']
    
    os.makedirs('static/images',exist_ok = True)
    images_folder = 'static/images/'
    raw_folder = keyword+'/'
    # txt_folder = '_Txt.txt'
    analysis_folder = keyword + '_analysis/'

    all_article = raw_folder + keyword + '_'  + web +'_網路爬蟲.txt'
    dict_path='結巴套件資料/'

    for keywords in keyword_list:
        #讀取檔案
        with open(keywords +'/' + keywords + '_'  + web +'_網路爬蟲.txt', encoding="utf-8", errors='ignore') as f:
            text_s = f.read()

        # 設定分詞資料庫
        # https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big 右鍵另存放目錄下
        jieba.set_dictionary(dict_path + 'dict.txt.big')

        # 將自己常用的詞加入字典
        jieba.load_userdict(dict_path + 'userDict.txt')

        
    #-------------------------------------------------------------------------------設定詞彙
        
        #帶入正向詞彙
        import sys
        res=[]
        text_good=[]
        with open(dict_path + '壞拷.txt',encoding="utf-8", errors='ignore') as f:
            for i in f:
                res.append(list(i.strip('\n').split(',')))      
        for j in res:
            text_good.append(j[0])
        res=[]
        text_bad=[]
        #帶入負向詞彙
        with open(dict_path + '壞.txt', encoding="utf-8", errors='ignore') as f:
            for i in f:
                res.append(list(i.strip('\n').split(',')))      
        for j in res:
            text_bad.append(j[0])


        text_x = text_good+text_bad

        for usual_word in text_x:
            jieba.add_word(usual_word)
        # jieba.del_word('不') # 刪除不單詞

    #---------------------------------------------------------------------切開文章

        seg_list = jieba.lcut(text_s, cut_all=False) # lcut直接返回list
        words = " ".join(seg_list)
        asd = []
        zxc = []
        for g in seg_list:
            if g in text_x:
                asd.append(g)
                zxc = Counter(asd)
        xcv = dict(zxc)
        print(keywords)
    #--------------------------------------------計算正負向比例
        x=0
        for i in text_good:
            if i in xcv:
                x +=xcv[i]
        print('好的',x)
        
        
        y=0
        for i in text_bad:
            if i in xcv:
                y +=xcv[i]
        print('壞的',y)

        if x != 0 and y != 0:
            s =float(x/(x+y)*100)
            boos = int('%.0f' %s)
            h.append(boos)
            print('%.2f' %s)
            u =float(y/(x+y)*100)
            yes = int('%.0f' %u)
            b.append(yes)
            print('%.2f' %u)
            
        else:
            s = 100
            h.append(s)
            u = 0
            b.append(u)
    #-----------------------------------------畫出圖表
    os.makedirs(analysis_folder,exist_ok = True)

    plt.figure(figsize=(9,7))
    plt.bar(keyword_list, h,color="#A9D08E",label="正向評價")
    plt.bar(keyword_list, b,color="#9BC2EF",bottom=h,label="負向評價")
    plt.xticks(fontsize=14)
    #取消網格線
    plt.grid(False)

    ax = plt.gca()
    ax.spines['top'].set_visible(False)#取消上框
    ax.spines['right'].set_visible(False)#取消右框
    ax.spines['left'].set_visible(False)#取消左框
    ax.get_yaxis().set_visible(False)#取消y軸數值
    for i in range(len(keyword_list)):
        plt.text(i,
            h[i]/2,# - 0.5,                 # 計算垂直高度
            h[i],
            fontsize=12,
            horizontalalignment='center')  # 設定 horizontalalignment 屬性水平置中
        plt.text(i,
            b[i]/2 + h[i] - 1,
            b[i],
            fontsize=12,
            horizontalalignment='center')
    plt.title('各品牌 正負評價比',fontweight='bold',fontsize = 16)
    # plt.legend(loc = "best") 
    
    plt.savefig(images_folder + keyword + '_正負評價比_各品牌.png') #要在show之前
    plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
    # plt.show()

keyword = '滴雞精'
pos_neg_analysis_brand(keyword=keyword)
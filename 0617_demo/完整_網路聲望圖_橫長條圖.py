def buzz(keyword) :
    #完整程式碼_結巴+文字雲
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
    import csv
    import os 
    # titles = ['發佈日期','文章標題','文章內容',"留言內容",'關鍵字',
    #         "文章ID","作者",'看板',"推推留言",'平平留言','噓噓留言',
    #         "文章分類","文章網址",'留言數','喜歡數','標籤']


    column = '品牌'

    #滴雞精
    keyword_list = ['農純鄉','田原香','老協珍','享食尚','娘家','純煉','金牌大師','芳茲','珍苑']
    #寶寶粥
    # keyword_list = ['農純鄉','桂格','飯友','郭老師','兒食樂','親子御膳坊',
    #                 '大地之愛','波堤寶寶','幸福米寶','琉元堂','寶膳']
    #'永豐餘','王朝','魚鮮森'
    # 益生菌
    # keyword_list = ['農純鄉','純煉','大本山','船井生醫','鑫耀生技','小兒利','悠活原力','孕哺兒','寶乖亞',
    #                 '威德','陽明生醫','森下仁丹','娘家']
    # '營養師輕食','天地合補','生展生技','生寶','創益生技','可爾必思','如新華茂','葡萄王','護一生', '統一',
    # '景岳生技','新普利','我的健康日記','MIHONG','長行生技','義美生醫','德和生技','統一AB','味全','達摩本草',
    # '樂健非凡','sakuyo','世華生技','大研生醫','台塑生醫','多利生醫','健美生','普羅家族','五洲生醫','善存',
    # '白蘭氏','優倍多','永信HAC', '諾得','享食尚', 'Nutrimate','好菌家'

    #功效
    # keyword_list =['增肌', '功效', '感冒', '疲勞', '皮膚', '白髮', '掉髮', '血壓', '抵抗力', '睡眠', 
    # '抗疲勞', '減脂', '腸胃', '免疫', '過敏', '記憶力', '頭髮', '關節', '膝蓋', '私密處', '精神', '促鐵', 
    # '腦部', '黑髮','長高', '好睡', '入睡', '蛀牙', '血脂', '血糖', '體脂', '骨質', '延緩衰老', '護肝', '牙齒', '減肥', 
    # '增重', '代謝', '牙齒', '肚子痛', '護眼', '老花', '腰', '腎', '攝護腺', '好氣色', '護眼', '衰老', 
    # '眼睛', 'Q彈', '異位性', '鼻子', '美白', '保濕', '抗老化', '明目', '累', '便祕', '厭食', '營養不良', 
    # '更年期', '肌少症', '頭痛', '痠痛', '失智', '老人癡呆', '白內障', '中風', '心肌梗塞', '性能力', '憂鬱', 
    # '骨質疏鬆', '性能力', '憂鬱', '骨質疏鬆']
    #成分
    # keyword_list =['蔬菜', '洋蔥', '地瓜', '有機', '馬玲薯', '無毒', '柴魚', '高麗菜', '鐵', '魚', '雞', '蘋果', '蛋白質', '番茄', '奶', '藜麥', '山藥', '菇', '雞精', '蛋', '海鮮', '蝦', '維他命', '橘子', '滴雞精', '干貝', '蒜', '檸檬', '葡萄', '紅蘿蔔', '牛', '鈣', '維生素']
    # keyword_list =['海鮮', '雞', '豬', '牛', '魚', '羊', '干貝', '蝦', '蛤蜊', '蔬菜', 
    # '素', '葷', '奶', '蛋', '蛋白質', '藻', '有機', '無毒', '高麗菜', '洋蔥', '蘋果', '鳳梨', 
    # '芹', '山藥', '蘆筍', '藜麥', '番茄', '馬玲薯', '地瓜', '紅蘿蔔', '菇', '維生素', '維他命', 
    # '鈣', '鐵', '糙米', '柴魚', '滴雞精', '雞精', '薑', '酒', '蒜', '草莓', '檸檬', '牛奶', '柳橙', 
    # '橘子', '葡萄', '奶粉', '枸杞', '紅棗', '九尾草', '馬卡', '膠原蛋白', '膳食纖維', '魚油', '紅麴', '胜肽']
    #風味
    # keyword_list =['無調味', '糖', '鹽', '醬油', '胡椒', '果汁', '草莓', '檸檬', '牛奶', '可爾必思', 
    #                '柳橙', '橘子', '葡萄', '水蜜桃', '香蕉', '辣', '酸', '甜', '苦']

    web = 'total'
    target_content = '文章標題'
    target_content2 = '文章內容'
    target_content3 = '留言內容'
    os.makedirs('static/images',exist_ok = True)
    images_folder = 'static/images/'
    raw_folder = keyword+'/'
    # txt_folder = '_Txt.txt'
    analysis_folder = keyword + '_analysis/'

    all_article = raw_folder +keyword + '_'  + web +'_網路爬蟲.txt'
    dict_path='結巴套件資料/'

    with open(all_article, encoding="utf-8", errors='ignore') as f:
        text = f.read()
    # 設定分詞資料庫
    # https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big 右鍵另存放目錄下
    jieba.set_dictionary(dict_path+'dict.txt.big')

    # 將自己常用的詞加入字典
    jieba.load_userdict(dict_path+'userDict.txt')

    # # 新增及刪除常用詞

    for kw in keyword_list:
        jieba.add_word(kw)

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

    x = dictionary.most_common()
    keys =[]
    values =[]
    for i in x:
        keys.append(i[0])
        values.append(i[1])

    dictionary = dict(zip(keys,values))
    keyword_values =[]

    for lis in keyword_list:
        try:
            value = dictionary[lis]
            keyword_values.append(value)
        except KeyError as k :
            print(k)
        except ValueError as v :
            print(v)
    # print(keyword_list)
    # print(keyword_values)

    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties
    try:
        sns.set(font=['sans-serif'])
        sns.set_style("whitegrid",{"font.sans-serif":['Taipei Sans TC Beta']})
        plt.rcParams["font.weight"] = "bold"
        plt.rcParams["axes.labelweight"] = "bold"
        # plt.figure(figsize=(400,400),dpi=400,linewidth = 0.6)
        dictionary = dict(zip(keyword_list,keyword_values))
        # print ("按值(value)排序:")  
        dict1 = sorted(dictionary.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
        #將字典轉成df
        keyword_list = []
        keyword_values =[]
        for i in dict1:
            kw = i[0]
            value = i[1]
            keyword_list.append(kw)
            keyword_values.append(value)
        print('排序過後的關鍵字：',keyword_list)
        # print(keyword_values)
        dictionary = dict(zip(keyword_list,keyword_values))
        # print(dictionary)
        df = pd.DataFrame([dictionary])
        df = pd.DataFrame.from_dict(dictionary,orient='index',columns=['出現次數'])
        # df = df.reset_index().rename(columns={'index':'','關鍵字':'出現次數'})
        df = df.reset_index().rename(columns={'index':' ','出現次數':''})

        os.makedirs(analysis_folder,exist_ok = True)

        # df = df.reset_index().rename(columns={'關鍵字':'出現次數'})
        plt.figure(figsize=(8,6))

        #顏色們
        # 預設deep muted pastel bright dark colorblind
        current_palette = sns.color_palette()
        bright_palette = sns.color_palette("bright") # 改變主題
        blue_palette = sns.color_palette("Blues") # 藍色的調色盤，由淺到深
        blue_r_palette = sns.color_palette("Blues_r") # 藍色的調色盤，由深到淺
        OrRd_palette = sns.color_palette("OrRd") # 橘色混紅色的調色盤
        hls_default_palette = sns.hls_palette() # hls預設的調色盤
        hls_palette = sns.hls_palette(h = 0.5, l = 0.4, s = 0.6) # 改變hls的預設值
        # color = ['black','red','green','orange','blue','limegreen','darkgreen','royalblue','navy']
        colors = ['#9BC2EF','#A9D08E','#F4B084','#B494F4','#FF7C80','#ffe88c',
                '#6FB7B7','#9999CC','#B766AD']

        ax = sns.barplot(x='', y=' ', data=df,palette=colors )#,palette=bright_palette)

        ax.set_title(keyword + column +'網路聲量圖',fontweight='bold',fontsize = 16)
        # sns.set_color_codes("pastel")
        #取消網格線
        plt.grid(False)
        for x,y in enumerate(keyword_values): 
            plt.text(y,x,'%s'%y,va='center',fontsize = 10)
        # plt.savefig( keyword + '_品牌網路聲量圖_o.png') #要在show之前
    except KeyError as k :
        print(k)
    except ValueError as v :
        print(v)
    # plt.savefig( analysis_folder + '/' + keyword + '_'+ column+'_聲量圖.png') #要在show之前
    plt.savefig(images_folder + keyword +'_品牌聲量圖.png')
    # plt.show()

keyword = '綠豆糕'
buzz(keyword=keyword)
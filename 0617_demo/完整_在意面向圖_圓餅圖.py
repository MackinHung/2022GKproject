# -*- coding:utf-8 -*-
def pie_analysis(keyword):
    #圓餅圖繪製
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties
    import numpy as np
    from tkinter import font
    from appscript import k
    import requests # 訪問
    import jieba
    from collections import Counter # 次數統計
    import re
    from tkinter import font
    from wordcloud import WordCloud
    import numpy
    from PIL import Image # 圖片轉array陣列
    import csv
    import os
    # -*- coding: utf-8 -*-
    web = 'total'
    os.makedirs('static/images',exist_ok = True)
    images_folder = 'static/images/'
    raw_folder = keyword+'/'
    # txt_folder = '_Txt.txt'
    analysis_folder = keyword + '_analysis/'

    all_article = raw_folder +keyword + '_'  + web +'_網路爬蟲.txt'
    dict_path='結巴套件資料/'

    with open(all_article, encoding="utf-8", errors='ignore') as f:
        text = f.read()

    #功效
    keyword_list_effect =['功效', '抵抗力', '感冒', '長高', '睡眠', '好睡', '入睡', '蛀牙', '血壓', '抗疲勞', '血脂', '過敏', '免疫', '體脂', '疲勞', '骨質', '腸胃', '促鐵', '增重', '增肌', '減脂', '精神', '代謝', '牙齒', '肚子痛', '老花', '膝蓋', '關節', '腰', '腎', '攝護腺', '好氣色', '護眼', '頭髮', '掉髮', '黑髮', '白髮', '記憶力', '衰老', '腦部', '眼睛', 'Q彈', '皮膚', '異位性', '鼻子', '美白', '保濕', '抗老化', '明目', '累', '便祕', '厭食', '營養不良', '更年期', '肌少症', '頭痛', '痠痛', '失智', '老人癡呆', '白內障', '中風', '心肌梗塞', '憂鬱', '性能力', '骨質疏鬆', '增強體力', '抗憂鬱', '食補', '養生', '術後調養', '運動健身', '養胎產後', '樂齡', '保健', '護肝', '調節血脂', '調節血糖', '免疫調節', '牙齒保健', '延緩衰老', '促進鐵吸收', '胃腸功能改善', '輔助調節血壓', '不易形成體脂肪', '輔助調整過敏體質', '加速傷口修復', '促進食慾', '提高運動表現', '保養身體', '減少焦慮', '營養密度高', '潤腸通便', '酸化腸道環境', '抑制害菌增殖', '調解菌叢平衡', '改善腸蠕動消化', '保護力', '維持消化道機能', '飽足感', '訓練咀嚼', '豐富鈣質', '增加學習力', '增強免疫力', '睡眠的更好', '產生血清素', '增加飽足感', '容易嚼食', '陪伴', '番茄紅素', '換季紅腫濕疹', '鼻', '嚴重', '忌口', '出力', '幫助腸胃吸收', '過期的', '胃口', '體脂下降', '尿道炎', '發炎', '排便的問題', '便秘', '巴氏腺囊腫', '囊腫破裂', '陰道炎', '對乳酸菌過敏者', '腸躁症', '外陰前庭炎', '過敏體質', '腸胃保健', '分泌物', '白色分泌物', '綠色分泌物', '紅色分泌物', '念珠菌', '感染', '搔癢', '天氣悶熱', '抵抗力下降', '骨盆腔感染', '大腸桿菌', '異位性皮膚炎', '脹氣打嗝', '飯後', '消化', '地中海貧血的症狀', '用藥', '加速治療', '正常大便', '徽菌', '打嗝脹氣', '念珠菌感染', '加速代謝', '排氣', '胃食道逆流', '蠕動腸胃', '減肥', '通宵', '阿德比腸胃', '增胖', '順暢', '瀉藥', '肚子超痛', '幫助吸收', '盲腸炎', '蠶豆症', '病', '抗黴菌', '口臭', '輔助', '體重', '內分泌失調', '工作忙碌', '壓力大', '晚睡', '身體免疫力上升', '平衡', '腸鳴', '益壽', '副食品', '疾病照護', '癌症', '滋補', '調理', '偏食', '養身', '不加任何一滴水', '低熱量', '零膽固醇', '零脂肪', '低熱量', '多膽固醇', '增強免疫力', '疲累感', '急性期', '增加體力', '加米精', '含鐵米精', '不舒服', '保養', '復發', '不發炎','綠豆糕']
    #成分
    keyword_list_element =['海鮮', '雞', '豬', '牛', '魚', '羊', '干貝', '蝦', '蛤蜊', '蔬菜', '葷', '奶', '蛋', '蛋白質', '藻', '有機', '無毒', '洋蔥', '蘋果', '鳳梨', '芹', '山藥', '蘆筍', '番茄', '馬玲薯', '地瓜', '菇', '維他命', '鈣', '鐵', '糙米', '柴魚', '滴雞精', '雞精', '薑', '酒', '蒜', '草莓', '檸檬', '牛奶', '柳橙', '橘子', '葡萄', '奶粉', '枸杞', '紅棗', '九尾草', '馬卡', '膠原蛋白', '膳食纖維', '魚油', '紅麴', '胜肽', '膳食纖維', '麥芽糊精', '全脂奶粉', '大本山葡萄萃取物', '乾酪乳酸桿菌', '植物乳桿菌', '副乾酪乳桿菌', '雷特氏B菌', '短雙歧桿菌', '嗜酸乳桿菌', '葡萄糖', '乳鐵蛋白', '石蓴多醣', 'BCAA', '膠質', '維生素A', '維生素D', '維生素E', '維生素K', '維生素B1', '維生素B2', '維生素B3', '維生素B5', '維生素B6', '維生素B7', '維生素B9', '礦物質', '微量元素', '水', '台灣香米', '玉米粒', '牛肉', '紅蘿蔔', '馬鈴薯', '番茄糊', '洋蔥', '黃豆芽', '蔥', '鮮乳', '香菇', '柴魚粉', '鯖魚', '鰹魚', '蓮藕', '青花菜', '海苔粉', '甘藍', '橄欖油', '小松菜', '天然奶油', '洋菇', '非基改醬油', '玉米澱粉', '細砂糖', '香蕉果汁粉', '凍乾香蕉片', '脫脂奶粉', '草莓果汁粉', '草莓濃縮汁', '菊糖', '草莓果粒', '維生素C', '黑蒜', '牛磺酸', '肌肽', '甲肌肽', '麩胺酸', '甘胺酸', '苯丙胺酸', '纈胺酸', '蘇胺酸', '色胺酸 ', '異白胺酸', '白胺酸', '甲硫胺酸', '離胺酸', '組胺酸', '普林', '小分子胜肽', '胺基酸', '支鏈胺基酸', '鈉', '油脂', '脂肪酸', '紅藜', '藜麥', '胚芽米', '胡蘿蔔', '菠菜', '卵磷脂', '果寡糖', '里肌肉', '葵花卵磷脂', '雞胸肉', '黑木耳', '玉米筍', '芡實', '小薏仁', '燕麥', '芹菜', '珠貝', '紫山藥', '山藥', '芝麻粉', '黑豆粉', '地瓜粉', '苔粉', '豬高湯', '牛高湯', '碘', '地瓜', '高麗菜', '牛奶魚', '金針菇', '澱粉', '吻仔魚', '鮭魚', '生機米', '米半杯', '雞胸半片', '鹽巴', '宿霧菜粥', '水果磨泥', '肉絲', '高蛋白', '天然植物成份', '葉酸', '綜合維他命', '鈣片', '菌種菌', '白木耳湯', '豬腳', '維生素Ｃ', '地瓜葉', '火龍果', '香蕉金', '針菇', 'BB536', '菲德氏菌', '優格', '優酪乳', '優碘坐浴', '夜酵素', '酵素', '纖維粉', '葉黃素', 'B群', '鈣粉', '維生素', '鳳梨酵素', 'DHC', '鮮奶', '火龍果芒果', '壞菌', '維他命C', 'DHC薏仁精華', '甘銨酸亞鐵', '甲殼素吸油', '乳寡醣', '養樂多', 'LP33', '菌數', '菌種', '菌株數量', 'LP28', '鼠李糖乳桿菌', '株洛德乳桿菌', 'GR-', 'RC-4', '紅色火龍果', '柿子', '益生菌', 'LCG菌', 'TCI633', '玻尿酸', '蔓越莓萃取', '米胚芽萃取GABA', '色胺酸', '穀維素', '芝麻萃取', '水果', '洋蔥水', '牛樟芝', '雞成分', '燕窩', '玉米', '甲肌肽', '肌肽', '牛磺酸', '鉬', '硒', '維生素A', '維生素B', '維生素C', '維生素D', '維生素K', '維生素E', '胺基酸', '黃體素', '鐵質', '白胺酸', '異白胺酸', '纈胺酸', '維他命B1', '維他命B2', '維他命B3', '維他命B4', '維他命B5', '維他命B6', '維他命D', 'dha', '葉酸', '小安素', '甲萘醌', '葉醌', '生育三烯酚', '生育酚', '鈣化醇', '抗壞血酸', '鈷胺素', '泛酸', '碎肉', '鈉含量', '洋蔥泥', '絲瓜鱸魚', '碎肉', '岩鹽','綠豆糕']
    #風味
    keyword_list_flavor =['米泥', '水果泥', '高麗菜半顆', '莓果益生菌', '蔓越梅益生菌', '蘋果調味乳', '蔓越莓錠', '乳酸菌', '酸', '甜', '粉', '小顆粒', '益生菌膠囊', '蔓越莓益生菌錠', '元錠', '喝膩', '台啤酵母錠', '無糖', '顆粒粉狀', '寵物益生菌', '爆漿滴雞精', '貢丸', '牛精', '烏骨雞', '晨露', '苦瓜炒蛋', '豬腥味', '薑茶', '黑蒜蛤蜊', '藥膳包', '泌乳湯', ' 酪梨', '牛肉', '雞油', '酪梨', '動物油脂', '薄荷糖', '蘋果白米糊', '紫心地瓜白米糊', '紅蘿蔔胚芽米糊', '甜玉米', '番茄口味', '黑寶玉米', '綜合蔬果', '蛤蠣', '山藥紫薯', '奶香野菇燉飯', '虱目魚樂樂粥', '鮮蔬豬肉烏龍麵', '蘋果蝦蝦炒飯', '鄉番茄海鮮燉飯', '兒食樂蔬果米泥', '蔬果雪花粉','綠豆糕']

    #氣味
    keyword_list_smell=['鮮味', '雞湯味', '腥味', '酸味', '水果味', '番茄味', '肉香味', '油香味', '酒味', '油臭味', '霉味', '氨水味道', '臭味', '酸味', '牛肉味', '豬肉味', '海鮮味', '蔬菜味', '清香', '芬芳', '刺鼻', '濃鬱', '焦香', '香味', '溫和的', '雞腥味', '肉腥味', '雞湯味', '南瓜味', '清淡的', '腥臭','綠豆糕']
    #價格
    keyword_list_prices=['昂貴', '非常昂貴', '便宜', '非常便宜', '廉價', '非常廉價', '平價', '物美價廉', '奢侈', '高價', '佛心', '普通', '特價', '可以接受', '無法接受', 'CP值高', '划算', '很虧', '不值得', '值得', '沒必要', '手刀購入', '花多少', '省錢', '不斐', '高昂', '組合價格', '不貴', '彩虹組合', '優惠','綠豆糕']
    #其他
    keyword_list_others=['無防腐劑', '無塑化劑', '無動物用藥', '無大腸桿菌', '無抗生素', '獨家專利', '無化學調味', '天然的', '無添加', '無調味劑', '無甜味劑', '無添加鹽', '無添加糖', '無添加人工添物劑', 'FDA', 'HACCP', '無生菌', '檢驗報告', '農藥殘留', '營養', '乾淨', '衛生', '在地新鮮食材', '用料實在', '有效期限', '吃好菌', '鈉含量', '超標', '鎘含量', '金屬殘留', '重金屬', '保持乾燥', '保健食品', '專利', '健康食品', '認證', '專利菌株', '健字號', '雙效認證', '小綠人標誌', '國際雙認證', '嚴選', 'CAS', 'NQ國家品質標章', '吃膩', '膩口', '難吞嚥', '嚐鮮', '田原香', '無毒農', '原粹', '鈞媽', '妙可適', '康貝兒', '艾多美', '三得利', '比菲多', 'Suntory比菲德氏菌', '台酒S', '娘家', 'Vitabox', '赫而司', '農純鄉', '皇家', '冠能', '愛肯拿', '渴望', 'ID', '伍零牌', '優沛康', '善存', '露奇亞', '葡萄王', '威德', '粥琉元堂', '頤珍', '元進莊', '恩典牌', '禧元堂', '元榆牧場', '享食尚', '嘉馨', '淞品', '石安牧場', '老茶', '芳茲', '勤益', '金牌大師', '王朝', '黃家', '圃美', '京紅', '大成', '元榆', '勤億', '品純萃', '永安', '小農牌', '蔡記', 'OH野', '真食補', '韓媽咪', '冊子', '捷捷', '旅居', '旅居漁村', '瀚克寶寶', '琉元堂', '森永', '王朝', '米米基地', 'kitty', '樂扉', '芽米寶貝', '郭老師', '森林', '丸碧', '日初禾作', '丞馨', '成新', '清潔', '女人心事', '婆媳問題', '離婚', '寶寶吃喝', '開箱文', '料理雞精', '哪裡買', '天然', '評鑑', '不需冷凍', '保存方便', '即食滴雞精', '營養補給', '月子中心', '團隊研發', '木耳飲', '成長紀錄', '孕吐', '牧場', '不適合', '行玉米雞', '甘蔗雞鹽水雞', '醉蝦麻油雞', '牛三寶', '美食', '手作', '親子丼', '麵線料理', '生產', '媽媽手冊', '月子餐', '營養品', '小舖', '饅頭', '母嬰用品', '冬蟲夏草', '廚房', '用品分享', '媽祖', '哺乳營養品', '雞魚饗宴', '月子滴雞精', '團購', '台灣品牌', '孕期怎麼吃', '代言', '推薦', '育兒用品', '食譜', '居家生活', '野飼崎雞', '用品', '分享', '居家安全', '產後滴雞精', '懷孕飲食', '養胎', '懷孕', '備孕', '初期養胎', '孕期', '擁有完整', '不用擔心', '保留', '威脅', '疫情', '流感', '安全的', '製程', '備料', '亨煮', '蒸氣萃取', '加工', '脫油', '建議', '防護力', '育兒津貼', '滴雞精諮詢', '單純', '物色', '有葉', '助孕', '養卵', '養卵子', '多喝水', '磨牙餅乾', '哺乳', '有檢驗的', '自己煮', 'mc', '噁心的東西', '業配仔', '業配文', '打荷爾蒙', '打激素', '好爛的', '好粗糙的', '耐熱鋁', '油耗味', '食用', '喝冰開水', '喝溫開水', '較高', '聞味道比較重', '香味重', '不能吃太重', '過鹹', '生菌數', '賀爾蒙', '不會拉稀', '托嬰', '代替', '全矽膠', '包覆', '解決方法', '有效嗎', '早上空腹', '沒這個疑慮', '瘦身', '瘦', '貓', '狗', '胖', '有用', '私密處', '沒什麼用', '沒用', '飼料', '改變體質', '評價', '功能障礙', '廁所', '多運動', '抗生素', '遺傳', '小鳥胃', '青汁飲食', '發作', '嬰幼兒', '小孩', '家庭', '營養師', '志玲', '寶寶', '醫師', '老公', '媽咪', '媽媽', '阿姨', '公公', '爸爸', '阿爸', '外公', '外婆', '男友', '男朋友', '女朋友', '孩童', '女友', '飯友', '大寶寶', '母嬰', '親子', '新生兒', '婆媳','綠豆糕']

    # 設定分詞資料庫
    # https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big 右鍵另存放目錄下
    jieba.set_dictionary(dict_path + 'dict.txt.big')

    # 將自己常用的詞加入字典
    jieba.load_userdict(dict_path + 'userDict.txt')

    # # 新增及刪除常用詞
    all_keyword_list = [keyword_list_effect,keyword_list_element,keyword_list_flavor,
            keyword_list_smell,keyword_list_prices,keyword_list_others]
    for kw_list in all_keyword_list :
        for kw in kw_list :
            jieba.add_word(kw)
            # print(kw)
    # 斷句方式
    # 用jieba.lcut(text, cut_all=False)直接返回list
    # segs = jieba.cut(text, cut_all=False) # 預設模式
    # segs = jieba.cut(text, cut_all=True) # 全切模式 切的很碎
    seg_list = jieba.lcut(text, cut_all=False) # lcut直接返回list
    words = " ".join(seg_list)
    # print(seg_list)

    dictionary = Counter(seg_list)
    # raw_stopwords =['，','\n', '│', '\u3000', '！', '「', '」', ' ', '、','？',
    #             '：','的','。','/','有','在','使用','.','！','於','我','了','就',
    #             '表示','是','它','級','都','TVBS',':','會','也','&','nbsp','為','、',
    #             '快點','吃','及','用','要','最','以上','後','\xa0','～','想','年',
    #             '新聞網','2021',' ','但','說','tvbs','com','tw','月','（','）',
    #             '而且','被','讓','這樣','等','看','仍','你','他','你們','他們','我們',
    #             '大','到','可','出','超','最常','分','得','人','下','太','喝','成',
    #             '問卦','嗎','Re','請','好','為','會','需要','問題','選擇','可以','處',
    #             '很','要','如何','賣','問有','該','怎麼','心得','想','討論','一直','對',
    #             '求','對','沒','[', ']', '超商', '甚麼','或', '推', '哪家', '最頂', '?',
    #             '帶', '每天', '一包', '怎樣', '阿','比', '較', '有效', '之', '拉', '屎', 
    #             '虛偽', '八卦', '完', '拉到', '快', '死', '掉', '不', '就是', '推薦', '認真',
    #             '牌子', '什麼', '時候', '真有', '這麼', '猛', '判斷', '加', '最近', '是不是', 
    #             '賺', '!', '貴', '啊', '何現', '一堆', '廣告', '打', '現成', '何不', '+',
    #             '請問', 'D3', '和', '能否', '一起', '三歲', '4M', '請益', '上', '很多', '元',
    #             '(', ')', '比較', '高', '舒', '請教', '多久', '詢問', '相關','>','與', '不過',
    #             '問寶乖', '亞吃', '多', '閒聊', '換過', '幾種','呢','好像','但是','這個',
    #             '一天', '多種', '知道', '哪款', '幾款','送', '這款', '免費', '買', '1', '分享', '好康', 
    #             '抽', '真的', '有人','"', '剛好', '一百元', '抵用券', '來', '顧個', '或是', 
    #             '值得', '今天', '台股', '又', '大跌', '上禮', '拜', '五', '賠錢', '賣興富',
    #             '發買', '進台', '積電', '結果', '套牢', '主力', '盯上', '4', '~', '打開',
    #             '電視', '各種', '想問', '大家', '哪個',  '另外', '台灣', '484','才', '狂',
    #             '感謝', '※', '板務', 'GossipPicket', '檢舉板', '實名', 'a', '張貼',
    #             '注意', '充實', '文章', '內容', '是否', '專板', '本板', '並非', '萬能',
    #             '問板', 'b', '只能', '兩則', '自刪', '刪', '算', '兩篇', '內', '超貼者將',
    #             '水桶', 'c', '本', '看板', '嚴格', '禁止', '政治', '發文', '前', '先',
    #             '仔細', '閱讀', '板規', 'd', '未滿', '30', '繁體', '中', '文字', '3', 
    #             '個', '嚴', '重者', '以鬧', '板論', '↑', '提醒', '刪除', 'ctrl', 'y', 
    #             '那麼','還是', '改帶','安安', '斜', '前方', '同事', '阿嬌', '中午', '完飯', 
    #             '小弟', '好奇', '卦', '剛剛', '看到', '大部份', '經過','跟', '能', '進到', 
    #             '已', '甚至', '已經', '會不會','幾年', '開始', '自', '製','當', '做', '一年',
    #             '左右', '發現','之前','顆','那', '=', 'https', '所以', '★','因為', 'i', 'imgur', 
    #             'jpg', '目前', '去','﹞','﹝',',','-','｜','免','無','❤','．','大甲','X','x','DIY',
    #             '古','法',';','\u200b','gt','amp','quot','lt','自己','隻','.&','更','喔','再',
    #             '時','加入','完全','www', '從', '2','而','雞','補充',  '覺得', '非常', '沒有', 
    #             '把', '直接', '她', '一下', '感覺','還有', '如果', '包', '一個', '時間',
    #             '像', '其實','一樣','除了', '這', '小','不用', "''", '醫生','著', '現在','起來', '吧',
    #             '適合','...','⋯','啦', '建議', '一','們','不是','長','以','不要','一點','精','囉',
    #             '其他','話', '5','一定', '喝起','一次','唷','早上','麵', '劑','http','雖然',
    #             '可能','準', '準備','看看','一些', '手術','特別','幫', '有點','東西', '只',
    #             '鬆','只有', '10', '只要','應該','每', 'span','怕','任何', '不能', '平常',
    #             '這次', '當然', '出來', '只是','加上', '*', '工作', '給', '復', '妳', '_', 
    #             '拿','最好', '作', '^', '放入', '好好', '水', '每個', '想要', '6', '▲', '馬',
    #             'x000D', '朋友','謝謝','—', '哦','…','大便', '母奶', '認證', '嚴重',
    #             '增加','聽', '蠻', '常常', '不好', '找','每次', '各位','歲','參考',
    #             '媽咪', '媽媽','方式','-----','不同', '不會', '農純鄉','分鐘','外出',
    #             '即可', '因此','容易', '●','擔心', '父母','寶寶吃','均衡','輕', 
    #             '黃', '我家','8','由', '愛', '39', '家', '熬',"''", '所','p',
    #             "'", '過敏', '便', '改善', '健康', '腸胃', '奶粉', '便秘', '小孩',
    #             '體質', '寶寶', '孩子', '幫助', '添加', '效果', '專利', '食用', '成分', '️', '菌', '配方', '產品', '皮膚', '好菌', '排便', '營養', '狀況', '調整', '試試', '保養', '味道', '吸收', '身體', '正常', '喜歡', '不錯', '餵', '品牌', '食物', '消化', '私密處', '口味', '重要', '小朋友', '懷孕', '感染', '包裝', '方便', '嗯', '裡面', '膠囊', '食品', '舒服', '天然', '希望', '飲食', '研究','搭配', '保健食品', '習慣', '副食品', '女兒', '功效', '維持', '安心', '肚子', '官網', '睡', '一般', '寶貝', '#', '免疫力', '有感', '我覺', '兩個', '擦', '卡蘿琳', '醫師', '提升', '癢', '大概', '日本','C', '生活', '環境',
    #             '妹妹', '哭', '含有', '$', '這些', '才能', '本身', '恩', '粉', '影響', '方法', '係','啟賦', '攝取', '挑選','出生', '外', '😂', '困擾', '天', '情況', '還', '好吃', '寶寶喝', '耶', '；', '商品', '主要', '順', '症狀', '消化道', '機能', '體驗','造成', '有些', '以前','以及', '有用', '技術', '晚上', '🏻', '補','慢慢', '炎', '功能', '運動', '12', '大人', '7', '吃過', '😭', '品質', '減少', '持續', '新','一盒', '少', '這罐', '了解', '種', '量', '期', '原本', '\t', '兒', '保健', '次', '寶寶的', '萃取', '滿', '含', '一歲', '可是',
    #             '泥','小籠', '口感', '料理','美味','市售','份量', '一餐','完成', '食譜','安全','作法', '至', '育兒', '咀嚼','香', '豐富', '出門', '攪', '蔔', '將', '晴', '炒', '冰磚', '作息','系列','嘗試', '奶', '20', '杯', '廚房', '棒', '飽', '防腐', '挑食', '碗', '藜麥', '快速', '吐司', '材料','rarr','粥品', '粉絲團','鈞媽','添加物', '請點', 'facebook', '旅居', '放心', '在家', '吻', '原味', '均', '零食', '天晴', '階段', '採用', '9','需', '光光', '杯水', '爸媽', '新鮮', '處理','選', '片', '湯匙', '切丁', '森', 'bull', '適量', '鱻', '▼', '外鍋', '所有', '穀', '15', '幸福米寶', 'blog', '海鮮', '愛吃', '00', '喝奶','鹹', '盒', '波堤寶寶', '森林', '接觸', '煮粥', '鹽', '讚', '含量', '勻', '人工', '蝦', '嚥', '餐點','net','6M', '給予', '媽媽們', '稍微', '吞', '鈞', '初體驗', '放', '堅持', '工作坊', '顏色', '色素', '入口', 'pixnet', '胡蘿', '倒', '嬰幼兒', '給寶寶吃', '＆', '玩', '冰箱', '味', '紫', '組合', '全攻略', '連結', '顆粒', '星星', '原', '不管', '標示', '餓', '收到', '料', '食堂','按', '延伸','試吃', '地', '皆', '變成', '清楚',
    #             '手指', '即','親子', '必須', '類', '爸爸', '完整', '餐椅', '價值', '過程', '家裡', '營養師', '農粥', '婆婆', '蒸煮', '倒入', '進食', '條', '飯友', '一碗', '倍', '用心', '得到','忙碌', '需求', '牙齒', '新手', '芽', '不想', '起', '燙', '總', '接受', '魚精', '軟', '月齡', '公克','容器', '＝', '單', 'ee','食量','幼兒', '難', '乾燥', '滿足', '克', '重','少許', '熱量', '餐廳', '接受度', '晚餐', '媽御', '低', '◆', '養生', '過', '兩種', 'cc', '富含', '副食', '點', '醬','13', '一姐', '嚐', '發育', '開箱', '冰', '空間', '弄', '細', '依照', '稠度', '放在', '<', '滿滿', '飲料','入', '選用', '接', '不少', '三種', '號', 'shp','家庭', '秒', '挑', '澱', '農', '早餐', '大小','烹煮', '註', 'post', '陪伴', '優惠', '漁村', '接著', '比例', '隨時', '第一','捷捷', '工具', '多元', '一份', '導致', '反應', '官方', '標準',
    #             '爸', '保留', '每餐', '200g', '照片', '申請', '幸福', '切碎', '部落', '時期', '大約', '十倍', '嚴選', '用餐', '手', '貝兒','150g', '並', '下去', '加水','16', '老公', '貼心', '各式', '熱水', '1.5', '上面', '詳細', '根', '客服', '鮮', '爐','調味料', '說明', '相當', '分裝', '衛生', '家中', '內鍋', '裸', '100', '決定', '腥味', '其', '150', '蓋', '實在', '橄欖油', '這裡', '銜接','♡','紅', '很快', 'reurl', '調理', '麻煩', '拿出','享用', '買過', '清洗', '更好','品', '寶寶也', '資料', '例如', '單純', '抓', '或者','就算', '洗淨', '40', '幫手','RoseLily', '發生', '少量', '二', '發展', '原來', '不足','拒食','塊', '線', '就要', '兜', 'FB', '14', '菇', '拍', '格', '上班', '適用', '學習', '幾個', '米',
    #             '有助','降低','眼睛','／','不知', '誰', '守護','出現', '回答','2022', '呼叫', '5914', '該問', '傳媒','版權', '©', 'All', 'Rights', 'Reserved', '體內','系統', '指出', '產生','透過', '患者', '》', '《', '其中','使','控制', '包括','如','引起','性','關鍵', '藥物', '粉末', 'D','根據','不僅','適度', '脹氣', '提高', '超過', '糞', '此外', '大量', '私密','狀態', '抑制', '飲', '常見', '食材', '質', '認為', '減重', '因', '達', '心情', '廁所', '有關','還能', '美國', '不適','空氣','症', '型', 'QQ', '價格', '之一', '陳', '更是','進行', '過度', '保濕', '民眾', '變化', '良好', '平時'] 
    #             # 定義停用詞
    # stopwords = []
    # for stopword in raw_stopwords :
    #     if stopword not in stopwords:
    #         stopwords.append(stopword)

    # [dictionary.pop(x, None) for x in stopwords] # 存字典裡刪除停用詞
    x = dictionary.most_common()
    # print(x[:20])
    keys =[]
    values =[]
    for i in x:
        keys.append(i[0])
        values.append(i[1])

    dictionary = dict(zip(keys,values))

    # for i,(k,v) in enumerate(dictionary.items()):
    #     print({k:v},end="")
    #     if i==10:
    #         print()
    #         break

    sns.set(font=['sans-serif'])
    sns.set_style("whitegrid",{"font.sans-serif":['Taipei Sans TC Beta']})
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"

    #ax1 圓餅圖
    # make figure and assign axis objects
    # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig = plt.figure(figsize=(12,9))
    fig=plt.gcf()
    # fig.set_facecolor('yellow')

    #    ['氣味', 40], ['其他', 40]],

    # explode=[0.1,0,0,0,0] #突出顯示第五塊數據
    # bar chart parameters
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
    colors = ['#9BC2EF','#A9D08E','#F4B084','#B494F4','#FF7C80','#ffe88c']

    #功效的資料處理
    keyword_values_effect =[]
    keyword_keys_effect = []
    for lis in keyword_list_effect:
        try:
            value = dictionary[lis]
            keyword_values_effect.append(value)
            keyword_keys_effect.append(lis)
        except KeyError as k :
            print(k)

    dictionary_effect = dict(zip(keyword_keys_effect,keyword_values_effect))
    dictionary_effect = sorted(dictionary_effect.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)

    keyword_keys_effect = []
    keyword_values_effect =[]
    for i in dictionary_effect:
        kw = i[0]
        value = i[1]
        keyword_keys_effect.append(kw)
        keyword_values_effect.append(value)
    # print('排序過後的關鍵字：',keyword_list)
    # print(keyword_values)
    keyword_keys_effect = keyword_keys_effect[:10]
    keyword_values_effect=keyword_values_effect[:10]
    # print(keyword_values_effect)
    dictionary_effect = dict(zip(keyword_keys_effect,keyword_values_effect))
    # print(dictionary)
    df = pd.DataFrame([dictionary_effect])
    df = pd.DataFrame.from_dict(dictionary_effect,orient='index',columns=['出現次數'])
    # print(df)
    # df = df.reset_index().rename(columns={'index':'','關鍵字':'出現次數'})
    df_effect = df.reset_index().rename(columns={'index':'  ','出現次數':' '})
    # print(df1[:11])
    df_effect = df_effect[:10]
    sum_effect =int(df_effect[' '].sum())
    df_effect[' ']=1

    ax1 =plt.subplot2grid((12,12),(0,11),rowspan=3, colspan=1)
    for x,y in enumerate(keyword_values_effect): 
        plt.text(0.3,x,'%s'%y,va='center',fontsize = 10)

    ax1 = sns.barplot(x=' ', y='  ', data=df_effect,color='#9BC2EF')
    # ,fontsize = 8)
    ax1.set_title('功效',fontweight='bold',fontsize = 10)
    sns.despine(top = True, right = True,left=True,bottom=True)
    # sns.despine(top = False, right = False,left=False,bottom=False)

    # ax1.set_xlim(0,0.5)
    plt.xticks(())

    #成分的資料處理
    keyword_values_element =[]
    keyword_keys_element = []
    for lis in keyword_list_element:
        try:
            value = dictionary[lis]
            keyword_values_element.append(value)
            keyword_keys_element.append(lis)
        except KeyError as k :
            print(k)

    dictionary_element = dict(zip(keyword_keys_element,keyword_values_element))
    dictionary_element = sorted(dictionary_element.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)

    keyword_keys_element = []
    keyword_values_element =[]
    for i in dictionary_element:
        kw = i[0]
        value = i[1]
        keyword_keys_element.append(kw)
        keyword_values_element.append(value)
    # print('排序過後的關鍵字：',keyword_list)
    # print(keyword_values)
    keyword_keys_element = keyword_keys_element[:10]
    keyword_values_element=keyword_values_element[:10]
    # print(keyword_values_element)
    dictionary_element = dict(zip(keyword_keys_element,keyword_values_element))
    # print(dictionary)
    df = pd.DataFrame([dictionary_element])
    df = pd.DataFrame.from_dict(dictionary_element,orient='index',columns=['出現次數'])
    # print(df)
    # df = df.reset_index().rename(columns={'index':'','關鍵字':'出現次數'})
    df_element = df.reset_index().rename(columns={'index':'  ','出現次數':' '})
    # print(df1[:11])
    df_element = df_element[:10]
    sum_element =int(df_element[' '].sum())
    df_element[' ']=1

    ax2 =plt.subplot2grid((12,12),(5,11),rowspan=3, colspan=1)
    for x,y in enumerate(keyword_values_element): 
        plt.text(0.3,x,'%s'%y,va='center',fontsize = 10)

    ax2 = sns.barplot(x=' ', y='  ', data=df_element,color='#A9D08E')
    # ,fontsize = 8)
    ax2.set_title('成分',fontweight='bold',fontsize = 10)
    sns.despine(top = True, right = True,left=True,bottom=True)
    # sns.despine(top = False, right = False,left=False,bottom=False)

    # ax2.set_xlim(0,0.5)
    plt.xticks(())


    #風味的資料處理
    keyword_values_flavor =[]
    keyword_keys_flavor = []
    for lis in keyword_list_flavor:
        try:
            value = dictionary[lis]
            keyword_values_flavor.append(value)
            keyword_keys_flavor.append(lis)
        except KeyError as k :
            print(k)

    dictionary_flavor = dict(zip(keyword_keys_flavor,keyword_values_flavor))
    dictionary_flavor = sorted(dictionary_flavor.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)

    keyword_keys_flavor = []
    keyword_values_flavor =[]
    for i in dictionary_flavor:
        kw = i[0]
        value = i[1]
        keyword_keys_flavor.append(kw)
        keyword_values_flavor.append(value)
    # print('排序過後的關鍵字：',keyword_list)
    # print(keyword_values)
    keyword_keys_flavor = keyword_keys_flavor[:10]
    keyword_values_flavor=keyword_values_flavor[:10]
    # print(keyword_values_flavor)
    dictionary_flavor = dict(zip(keyword_keys_flavor,keyword_values_flavor))
    # print(dictionary)
    df = pd.DataFrame([dictionary_flavor])
    df = pd.DataFrame.from_dict(dictionary_flavor,orient='index',columns=['出現次數'])
    # print(df)
    # df = df.reset_index().rename(columns={'index':'','關鍵字':'出現次數'})
    df_flavor = df.reset_index().rename(columns={'index':'  ','出現次數':' '})
    # print(df1[:11])
    df_flavor = df_flavor[:10]
    sum_flavor =int(df_flavor[' '].sum())
    df_flavor[' ']=1


    ax3 =plt.subplot2grid((12,12),(9,11),rowspan=3, colspan=1)
    for x,y in enumerate(keyword_values_flavor): 
        plt.text(0.3,x,'%s'%y,va='center',fontsize = 10)

    ax3 = sns.barplot(x=' ', y='  ', data=df_flavor,color='#F4B084')
    # ,fontsize = 8)
    ax3.set_title('風味',fontweight='bold',fontsize = 10)
    sns.despine(top = True, right = True,left=True,bottom=True)
    # sns.despine(top = False, right = False,left=False,bottom=False)

    # ax3.set_xlim(0,0.5)
    plt.xticks(())

    #氣味的資料處理
    keyword_values_smell =[]
    keyword_keys_smell = []
    for lis in keyword_list_smell:
        try:
            value = dictionary[lis]
            keyword_values_smell.append(value)
            keyword_keys_smell.append(lis)
        except KeyError as k :
            print(k)

    dictionary_smell = dict(zip(keyword_keys_smell,keyword_values_smell))
    dictionary_smell = sorted(dictionary_smell.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)

    keyword_keys_smell = []
    keyword_values_smell =[]
    for i in dictionary_smell:
        kw = i[0]
        value = i[1]
        keyword_keys_smell.append(kw)
        keyword_values_smell.append(value)
    # print('排序過後的關鍵字：',keyword_list)
    # print(keyword_values)
    keyword_keys_smell = keyword_keys_smell[:10]
    keyword_values_smell=keyword_values_smell[:10]
    # print(keyword_values_smell)
    dictionary_smell = dict(zip(keyword_keys_smell,keyword_values_smell))
    # print(dictionary)
    df = pd.DataFrame([dictionary_smell])
    df = pd.DataFrame.from_dict(dictionary_smell,orient='index',columns=['出現次數'])
    # print(df)
    # df = df.reset_index().rename(columns={'index':'','關鍵字':'出現次數'})
    df_smell = df.reset_index().rename(columns={'index':'  ','出現次數':' '})
    # print(df1[:11])
    df_smell = df_smell[:10]
    sum_smell =int(df_smell[' '].sum())
    df_smell[' ']=1

    ax4 =plt.subplot2grid((12,12),(0,0),rowspan=3, colspan=1)
    for x,y in enumerate(keyword_values_smell): 
        plt.text(0.3,x,'%s'%y,va='center',fontsize = 10)

    ax4 = sns.barplot(x=' ', y='  ', data=df_smell,color='#B494F4')
    # ,fontsize = 8)
    ax4.set_title('氣味',fontweight='bold',fontsize = 10)
    sns.despine(top = True, right = True,left=True,bottom=True)
    # sns.despine(top = False, right = False,left=False,bottom=False)

    # ax4.set_xlim(0,0.5)
    plt.xticks(())

    #價格的資料處理
    keyword_values_prices =[]
    keyword_keys_prices = []
    for lis in keyword_list_prices:
        try:
            value = dictionary[lis]
            keyword_values_prices.append(value)
            keyword_keys_prices.append(lis)
        except KeyError as k :
            print(k)

    dictionary_prices = dict(zip(keyword_keys_prices,keyword_values_prices))
    dictionary_prices = sorted(dictionary_prices.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)

    keyword_keys_prices = []
    keyword_values_prices =[]
    for i in dictionary_prices:
        kw = i[0]
        value = i[1]
        keyword_keys_prices.append(kw)
        keyword_values_prices.append(value)
    # print('排序過後的關鍵字：',keyword_list)
    # print(keyword_values)
    keyword_keys_prices = keyword_keys_prices[:10]
    keyword_values_prices=keyword_values_prices[:10]
    # print(keyword_values_prices)
    dictionary_prices = dict(zip(keyword_keys_prices,keyword_values_prices))
    # print(dictionary)
    df = pd.DataFrame([dictionary_prices])
    df = pd.DataFrame.from_dict(dictionary_prices,orient='index',columns=['出現次數'])
    # print(df)
    # df = df.reset_index().rename(columns={'index':'','關鍵字':'出現次數'})
    df_prices = df.reset_index().rename(columns={'index':'  ','出現次數':' '})
    # print(df1[:11])
    df_prices = df_prices[:10]
    sum_prices =int(df_prices[' '].sum())
    df_prices[' ']=1

    ax5 =plt.subplot2grid((12,12),(5,0),rowspan=3, colspan=1)
    for x,y in enumerate(keyword_values_prices): 
        plt.text(0.3,x,'%s'%y,va='center',fontsize = 10)

    ax5 = sns.barplot(x=' ', y='  ', data=df_prices,color='#FF7C80')
    # ,fontsize = 8)
    ax5.set_title('價格',fontweight='bold',fontsize = 10)
    sns.despine(top = True, right = True,left=True,bottom=True)
    # sns.despine(top = False, right = False,left=False,bottom=False)

    # ax5.set_xlim(0,0.5)
    plt.xticks(())

    #其他的資料處理
    keyword_values_others =[]
    keyword_keys_others = []
    for lis in keyword_list_others:
        try:
            value = dictionary[lis]
            keyword_values_others.append(value)
            keyword_keys_others.append(lis)
        except KeyError as k :
            print(k)

    dictionary_others = dict(zip(keyword_keys_others,keyword_values_others))
    dictionary_others = sorted(dictionary_others.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)

    keyword_keys_others = []
    keyword_values_others =[]
    for i in dictionary_others:
        kw = i[0]
        value = i[1]
        keyword_keys_others.append(kw)
        keyword_values_others.append(value)
    # print('排序過後的關鍵字：',keyword_list)
    # print(keyword_values)
    keyword_keys_others = keyword_keys_others[:10]
    keyword_values_others=keyword_values_others[:10]
    # print(keyword_values_others)
    dictionary_others = dict(zip(keyword_keys_others,keyword_values_others))
    # print(dictionary)
    df = pd.DataFrame([dictionary_others])
    df = pd.DataFrame.from_dict(dictionary_others,orient='index',columns=['出現次數'])
    # print(df)
    # df = df.reset_index().rename(columns={'index':'','關鍵字':'出現次數'})
    df_others = df.reset_index().rename(columns={'index':'  ','出現次數':' '})
    # print(df1[:11])
    df_others = df_others[:10]
    sum_others =int(df_others[' '].sum())
    df_others[' ']=1

    ax6 =plt.subplot2grid((12,12),(9,0),rowspan=3, colspan=1)
    for x,y in enumerate(keyword_values_others): 
        plt.text(0.3,x,'%s'%y,va='center',fontsize = 10)

    ax6 = sns.barplot(x=' ', y='  ', data=df_others,color='#ffe88c')
    # ,fontsize = 8)
    ax6.set_title('其他',fontweight='bold',fontsize = 10)
    sns.despine(top = True, right = True,left=True,bottom=True)
    # sns.despine(top = False, right = False,left=False,bottom=False)

    # ax6.set_xlim(0,0.5)
    plt.xticks(())
    try:
        #ax0圓餅圖
        ax0 =plt.subplot2grid((12,12),(2,1),rowspan=10, colspan=10)
        # fig.subplots_adjust(wspace=0)
        df = pd.DataFrame([
            ['功效', sum_effect], ['成分', sum_element], ['風味', sum_flavor],['氣味', sum_smell],
            ['價格',sum_prices],['其他',sum_others]],
            columns=['在意面向', '數值'])

        ax0.pie(df['數值'], labels=df['在意面向'], autopct='%1.0f%%'
        ,startangle=120,counterclock=False,colors=colors)
        # textprops = {"fontsize" : 10})

        # 調整圓餅圖圓的大小radius=1.7)
        #,explode=explode)
        # ax0.legend(loc = "best")
        ax0.set_title('網友在意的' + keyword + '面向',fontweight='bold',fontsize = 16)
    except KeyError as k :
        print(k)
    except ValueError as v :
        print(v)
    os.makedirs(analysis_folder,exist_ok = True)

    plt.legend(loc = 'upper right') 
    plt.savefig( images_folder + keyword + '_網友在意面向圖.png') #要在show之前
    # plt.show()

keyword = '綠豆糕'
pie_analysis(keyword=keyword)
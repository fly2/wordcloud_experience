import matplotlib.pyplot as plt
import pickle
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
import numpy as np
import pandas as pd
import random
from os import path
#得到地址
d = d = path.dirname('.')
#定义色系
def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
def get_wc(f,name):
    #读取文本，需分好词（以空格隔开词）
    #text = open('/home/weblogic/DATA/private/shangguanxf/cc_bigdata/create/寿险预约咨询工单.txt', 'r', encoding='utf-8').read()
    #backgroud_Image = plt.imread('/home/weblogic/DATA/private/shangguanxf/pictures/colored_3.png')
    #plt.imread图片只支持.jpg格式
    back_coloring = plt.imread('/home/weblogic/DATA/private/shangguanxf/sucai/cloud.jpg')
    #github原版获取图片方法,可获取.png格式
    #back_coloring = np.array(Image.open('/home/weblogic/CODE/shangguan/wordcloud-master/image/alice_color.png'))

    wc = WordCloud( background_color = 'white',    # 设置背景颜色
                    mask = back_coloring,        # 设置背景图片
                    max_words = 1000,            # 设置最大现实的字数
                    stopwords = STOPWORDS,        # 设置停用词
                    font_path='/home/weblogic/DATA/private/shangguanxf/sucai/fonts/方正启体简体.ttf',
                    max_font_size = 100,            # 设置字体最大值
                    random_state = 1             # 设置有多少种随机生成状态，即有多少种配色方案
                    )
    #wc.generate(text)
    '''
    #得到词频并导出
    words=wc.process_text(text)
    df=pd.DataFrame(columns=('词', '频数规范化'))
    n=0
    for i in words:
        df.loc[n]=[i[0],i[1]]
        n=n+1
    df.to_excel('/home/weblogic/DATA/private/shangguanxf/cc_bigdata/create/词云/'+name+'.xlsx',sheet_name='Sheet1')
    '''
    #用词频画图 f应为字典的list格式
    wc.generate_from_frequencies(f)
    # 从背景图片生成颜色值
    image_colors = ImageColorGenerator(back_coloring)
    # 以下代码显示图片
    plt.imshow(wc.recolor(color_func=grey_color_func, random_state=5))
    plt.axis("off")

    '''
    # 绘制词云
    plt.figure()
    #绘制灰色系的图片
    plt.imshow(wc.recolor(color_func=grey_color_func, random_state=5))
    # 绘制以背景图片颜色为颜色的图片
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis("off")
    #绘制背景
    plt.figure()
    plt.imshow(backgroud_Image, cmap=plt.cm.gray)
    plt.axis("off")
    '''
    plt.show()
    # 保存图片
    #wc.to_file(path.join(d, name+'.png'))

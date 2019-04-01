'''
wordcloud是优秀的词云展示第三方库
-词云以词语为基础的基本单位，更加直观和艺术的展示文本
worldcloud库的安装
（cmd命令行）pip install worldcloud

-wordcloud.WordCloud()代表一个文本对应的词云
-可以根据文本中词语出现的频率参数绘制词云
-绘制词云的形状、尺寸、和颜色都可以设定

wordcloud库的使用
方法              描述
w.generate(txt)     向wordcloud对象w中加载文本txt
                    w.generate("python and wordcloud")
w.to_file(filename) 将词云输出为图像文件，.png / .jpg格式
                    w.to_file("outfile.png")

步骤1、配置对象参数
步骤2、加载词云文件
步骤3、输出词云文件

import wordcloud
c=wordcloud.WordCloud()
c.generate("i love python ,i am a small boy!")
c.to_file("pywordcloud.png")

配置对象参数
参数                  描述
min_font_size       指定词云中字体的最小字号，默认4号
                    w=wordcloud.WordCloud(min_font_size=10)
max_font_size       指定词云中字体的最大字号，根据高度自动调节
                    w=wordcloud.WordCloud(max_font_size=20)
font_step           指定词云中字体字号的步进间隔，默认为1
                    w=wordcloud.WordCloud(font_step=2)
font_path           指定字体文件的路径，默认None
                    w=wordcloud.WordCloud(font_path="msyh.ttc")
max_words           指定显示的最大单词量，默认200
                    w=wordcloud.WordCloud(max_words=20)
stop_words          指定词语的排除词列表，既不显示的单词列表
                    w=wordcloud.WordCloud("python")

参数                  描述
mask                    指定词云形状。默认为长方形，需要引用IMread（）函数
            form scipy.misc import imread
            mk=imread("pic.png")
            w=wordcloud.WordCloud(mark=mk)
background_color        指定词云的背景颜色，默认为黑色
                    w=wordcloud.WordCloud(background_color="white")
#英文文本
import wordcloud
txt = "Life is short, you need python"
w=wordcloud.WordCloud(font_path="msyh.ttf")
w=wordcloud.WordCloud(background_color="white")
w.generate(txt)
w.to_file("pyython.jpg")
#汉字文本
import jieba
import wordcloud
txt = "程序设计语言是计算机能够理解和" \
      "识别用户操作意图的一种交互体系，它按照" \
      "特定规则组织计算机指令，是计算机能够自动" \
      "进行各种运算处理"
w=wordcloud.WordCloud(width=1000,font_path="msyh",height=700)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("pywcloud.png")

生成不同形状的词云
'''
"""
政府工作报告
生成词云优化词云

#govrptwordcloud1.py
import jieba
import wordcloud
f=open("文本文档/乡村振兴.txt","r",encoding="gbk")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttc",width=1000,height=700,background_color="white",
                      max_words=20)
w.generate(txt)
w.to_file("grwordcloud2.png")
"""

import jieba
import wordcloud
from scipy.misc import imread
mask=imread("timg.jpg")
f=open("文本文档/薛之谦.txt","r",encoding="gbk")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttc",mask=mask ,width=1000,height=700,background_color="white")
w.generate(txt)
w.to_file("之谦.png")















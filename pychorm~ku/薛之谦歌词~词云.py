import jieba
import wordcloud
f=open("文本文档/薛之谦.txt","r",encoding="gbk")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttc",width=1000,height=700,background_color="white")
w.generate(txt)
w.to_file("花儿与少年.png")
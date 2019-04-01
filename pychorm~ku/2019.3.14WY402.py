#字典
#字典类型操作函数和方法
'''
函数或方法       描述
del d[k]        删除字典d中键k对应的数据值
k in d          判断k是否在字典d中，如果在返回true，否则False
d.key()         返回字典d中所有的键的信息
d.values()      返回字典d中所有的值的信息
d.items()       返回字典d中所有的键值对的信息
d={"中国":"北京","美国":"华盛顿","法国":"巴黎","日本":"东京"}
print("中国"in d)

print(d.keys())

print(d.values())


列表类型操作函数和方法
函数或方法               描述
d.get(k,<default>)      键k存在，则返回相应的值，不在则返回<default>值
d.pop(k,<default>)      键k存在，则取出（在原字典中删除）相应的值，不在则返回<default>值
d.popitem()             随机从字典d中取出一个键值对，以元组形式返回
d.clear()               删除所有的键值对
len(d)                  返回字典d中的元素

d={"中国":"北京","美国":"华盛顿","法国":"巴黎","日本":"东京"}
a=d.get("中国","伊斯兰堡")
b=d.get("巴基斯坦","伊斯兰堡")
print(a,b)
print(d.popitem())
'''


"""
1、定义空字典d
2、向d新增两个键值对元素
3、修改第二个元素
4、判断“C”是否是d的键
5、计算d的长度
6、清空 d
d={}
d["A"]=1;d["B"]=2
d["B"]=3
"c" in d
len(d)
d.clear()
"""
'''jieba库概述
-中文文本需要通过分词或得单个词语
-jieba是优秀的中文分词的第三方库，需要额外安装
-jieba库提供了三种分词模式，最简单只需掌握一个函数

jieba库的安装
（cmd命令行）    pip install jieba

jieba库的使用·jieba分词依靠中文词库
-利用一个中文词库，确定汉字之间的关联概率
-汉字间概率大的组成词组，形成分词的结果
-除了分词，用户还可以添加自定义的词组

jieba分词的三种模式
精确模式、全模式、搜素引擎模式
-精确模式：把文本精确的切开，不存在*余单词
-全模式：把文本中所有可能的单词都扫描出来
-搜索引擎模式：在精准模式基础上，对长词再次切分

jieba库常用函数
函数                              描述
jieba.lcut(s)               精确模式，返回一个列表了类型的分词结果
jieba.lcut(s,cut_all=True)  全模式，返回一个列表类型的分词结果，存在*余
jieba.lcut_for_search(s)    搜素引擎模式，返回一个列表类型的分词结果，存在*余
jieba.add_word(w)           向分词词典增加新词W

import jieba
print(jieba.lcut("我爱河北师范大学"))
print(jieba.lcut("我爱河北师范大学",cut_all=True))
print(jieba.lcut_for_search("我爱河北师范大学"))
print(jieba.add_word("蟒蛇语言"))
print(jieba.lcut("什么是蟒蛇语言"))
#['我', '爱', '河北师范大学']
#Prefix dict has been built succesfully.
#['我', '爱河', '河北', '河北师范大学', '北师', '师范', '师范大学', '大学']
#['我', '爱', '河北', '北师', '师范', '大学', '河北师范大学']
#None
#['什么', '是', '蟒蛇语言']
'''
#统计单词的数量
def gettext():
    txt=open("cheat.txt","r").read()#打开文件
    txt=txt.lower()#将这个TXT文件中的字母全部变成小写
    for ch in '!"#$%^&*():;",<>.*~':#用文本操作将特殊符号变成空格
        txt=txt.replace(ch," ")
    return txt

hamletxt=gettext()
words=hamletxt.split()#split 将文本以空格来分隔，以列表的形式返回，words是列表类型
#一个单词和他出现的次数，便构成了映射，所以用字典来定义
counts={}#定义了一个空字典
for word in words:
    counts[word]=counts.get(word,0)+1
#对单词出现的次数进行排序
items=list(counts.items())# items() 函数以列表返回可遍历的(键, 值) 元组数组。
##然后将其转化成列表的形式
#返回给items
items.sort(key=lambda x:x[1],reverse=True)#现阶段要记住，他的作用是将字典的第二个元素排序，（从大到小）
#打印出现的次数
for i in range (10):
    word,count=items[i]
    print("{0:<10}{1:5}".format(word,count))













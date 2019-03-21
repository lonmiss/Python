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
'''
import jieba
jieba.lcut("我爱河北师范大学")
jieba.lcut("我爱河北师范大学",cut_all=True)
jieba.lcut_for_search("我爱河北师范大学")
jieba.add_word("蟒蛇语言")
jieba.lcut("什么是蟒蛇语言")

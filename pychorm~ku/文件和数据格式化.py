"""
字符串格式化
"{}{}{}".format()
将字符串按照一定的规格和样式进行规范

数据格式化
将一组数据按照一定的规格和样式进行规范：表示、存储、运算等

本节课学习内容：
文件的使用
实例11：自动化轨迹绘制
一维数据的格式化和处理
二维数据的格式化和处理
wordcloud库的使用
实例12：政府工作报告词云


文件的理解
文件是数据的抽象和集合
-文件是存储在存储器上的数据序列
-文件是数据存储的一种形式
-文件展现形态：文本文件和二进制文件

由单一特定编码组成的文件，如UTF-8编码
由于存在编码，也被看成是存储着的长字符串
适用于：TXT 文件 py文件

二进制文件
直接有比特0和1组成，没有同一字符的编码
一般存在二进制0和1的组织构成，即文件格式
.png文件 .avi文件


#以文本的形式打开文件
tf=open("f.txt","rt")
print(tf.readline())
tf.close()
#中国是个伟大的国家！

#以二进制形式打开文件
tf=open("f.txt","rb")
print(tf.readline())
tf.close()
#中国是个伟大的国家！
#b'\xd6\xd0\xb9\xfa\xca\xc7\xb8\xf6\xce\xb0\xb4\xf3\xb5\xc4\xb9\xfa\xbc\xd2\xa3\xa1'


文件的打开
<变量名>=open(<文件名>，<打开模式>)
<文件名>文件路径和名称（源文件同目录可以省略路径）
<打开模式>文本or二进制

文件路径和名称 "D:/PYE/f.txt"      如果在同一文件名下"./PYE/f.txt"
源文件同目录下可省略路径   "D:\\PYE\\f.txt"
(相对路径，绝对路径)

打开模式
"r" 只读模式，默认值，如果文件不存在，返回filenotfound
"w"覆盖写模式，文件不存在则创建，存在则完全覆盖
"x"创建写模式，文件不存在则创建，存在则返回fileexistserror
"a"追加写模式，文件不存在则创建，存在则在文件最后追加内容
"b"二进制文件模式
"t"文本文件模式，默认值
"+"与r/w/x/a一同使用，在原功能基础上增加同时读写功能

f=open("f.txt")              #文本形式、只读模式、默认值
print(f.readline())
f=open("f.txt","rt")              #文本形式、只读模式、同默认值
print(f.readline())
f=open("f.txt","w")              #文本形式、覆盖写模式
print(f.readline())
f=open("f.txt","a+")              #文本形式、追加写模式+读文件
print(f.readline())
f=open("f1.txt","x")              #文本形式、创建写模式
print(f.readline())
f=open("f1.txt","b")              #二进制形式、只读模式
print(f.readline())
f=open("f.txt","wb")              #二进制形式、覆盖写模式
print(f.readline())

文件关闭
<变量名>.close()

文件内容读取
操作方法                描述
<f>.read(size=-1)读入全部内容，如果给出参数，读入前size长度
<f>.readline(size=-1)读入一行内容，如果给出参数，读入该行前size长度
<f>.readlines(hint=-1)  读入文件所有行，以每行为元素形成列表；如果给出参数，读入前hint行

文件的全文本操作
方法一：
fname=input(“请输入要打开的文件名称：”)
fo = open(fname,"r")
txt=fo.read()
#对全文TXT进行处理
fo.close()
#如果文本太大的话，代价太大

方法二：
fname=input("请输入要打开的文件名称：")
fo=open(fname,"r")
txt=fo.read(2)  #每次只读入两个字节
while txt="":
    #对txt进行处理
    txt=fo.read(2)
fo.close()      #-按数量读入，逐步处理

文件的逐行操作
方一
fname=input("请输入要打开的文件的名称：\n")
fo=open(fname,"r")
for i in fo.readlines():   #一次读入，分行处理
    print(i)
fo.close()
'''
请输入要打开的文件的名称：
不再爱.txt
1、

input标签中type属性的常用取值及其对应的控件：

（1）、type="text"时，输入框为文本输入框

（2）、type="password"时，输入框为密码输入框

（3）、type="radio"时，控件为单选框

（4）、type="checkbox",控件为复选框

（5）、type="file",用于文件上传

（6）、type="subit",提交按钮，提交表单信息到服务器

（7）、type="reset",重置按钮，重置表单信息至初始状态

（8）、type="button",普通按钮

方二
fame=input(请输入要打开的文件名称：\n)
fo=open(fname,"r")
for line in fo:
    print(line)
fo.close()          #分行读入，逐行处理


数据的文件写入
<f>.writes(s)       向一个文件写入一个字符或字节流
<f>.writelines(lines)   将一个元素全为字符串的列表写入文件
'''

"""
#a=open("f.txt","rt")
#print(a.readline())
#print(a.read(2))
#a.close()

f=open("不再爱.txt","a+")
f.write("中国是一个伟大的国家")
ls=["/n""德国","美国","法国"]
f.writelines(ls)
f.close()

























#字典类型及操作
#字典类型定义
'''
理解“映射”
映射是一种键（索引）和值（数据）的对应
序列类型由0.。。N整数作为数据的默认索引
映射类型则由用户为数据定义的索引

字典类型是映射的体现
-键值对：键是数据索引的扩展
-字典是键值对的集合，键值对之间无序
-采用大括号{}和dict()创建，键值对用冒号：表示

字典类型的用法
    在字典变量中，通过键或的值
    <字典变量>={<键1>：<值1>，...,<键N>:<值n>}
    修改字典
    <值>=<字典变量>[<键>]     <字典变量>[<键>]=<值>
        []用来向字典变量中索引或增加元素
'''
d={"中国":"北京","美国":"华盛顿","法国":"巴黎"}
print(d,"\n")
print(d["中国"])
#定义一个空的字典
de={};type(de)
#<class 'dict'>   type(x)   返回变量x的值
'''
技术能力的扩展
-获取多个数据：从控制台获取多个不确定数据的方法
-分隔多个函数：模块化设计方法
-充分利用函数：充分利用python提供的内容函数

'''
"""
#基本统计值得计算
#CalStatisticsV1.py
def getnum():
    nums=[]
    inumstr=input("请输入数字（回车退出）：")
    while inumstr !="":
        nums.append(eval(inumstr))
        inumstr=input("请输入数字（回车退出）：")
    return nums

def mean(numbers):
    s=0.0
    for i in numbers:
        s=s+i
    return s/len(numbers)

def dev(numbers,mean):#计算方差
    sdev = 0.0
    for i in numbers:
        sdev = sdev+(i-mean)**2
    return pow(sdev/len(numbers)-1,0.5)

#sorted 可以直接给列表排序
def median(numbers):#计算中位数
    sorted(numbers)
    size=len(numbers)
    if size%2==0:
        med=(numbers[size//2-1]+numbers[size//20])/2
    else:
        med=numbers[size//2]
    return med

n=getnum()
m=mean(n)
print("平均值{},方差：{:.2}.".format(m,dev(n,m)))
"""

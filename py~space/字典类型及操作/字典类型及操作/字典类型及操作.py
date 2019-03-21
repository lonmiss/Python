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
    sdev=0.0
    for i in numbers:
        sdev = sdev+((i-mean)**2)
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
print("平均值{},方差：{:.2},中位数：{}.".format(m,dev(n,m),median(m)))

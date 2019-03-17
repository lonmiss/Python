#random库的概述
#random库是使用随机数的Python库
#伪随机数：采用梅森旋转算法生成的（伪）随机序列中的元素
'''
random 库包含两类函数，常用的共八个
-基本随机数函数：seed() random()
-扩展随机数函数: randint() getrantdbits()、uniform(),
                randrange(),choice(),shuffle()
'''
"""
基本随机数函数
函数                  描述
seed(a=None)       初始化给定的随机数种子，默认当前系统时间
                    》》》random.seed(10)#产生种子10对应的序列
random（）          生成一个[0.0,1.0]之间的随机小数
                    》》》random.random()
"""

'''
import random 
random.seed(10)
a=random.random()
s=a+1
print(a,end=" ")#0.571402594689913
print('\n')
c=random.randint(10,1000)
print(c)
#random.random()
'''

'''
扩展随机数函数
random()
randint(a,b)    生成一个[a,b]之间的整数
    random.randint(10,100)      64
randrange()     randrange(m,n,k)生成一个[m,n]之间以k为步长的随机整数
    random.randrange(10,100,10)     80
choice()        从序列seq中随机选择一个元素
                random.choice([1,2,3,4,5,6,7,9])   5
getrandbits()   生成一个k比特长的随机整数
    random。getrandbits(16)      37885
shuffle()       将序列seq中元素随机排序，返回打乱后的序列

》》》
s=[1,2,3,4,5,6,7,8]
random.suffle(s)
print(s)
[3,2,1,5,8,7,4,6]


uniform()       生成一个[a,b]之间的随机小数
     random.uniform(10,100)     13.096321648808136

随机函数的使用
-能够利用随机数种子产生“确定”伪随机数
-能够产生随机整数
-能够对序列类型进行随机操作
'''
#print("又见面了，Python!\n")


'''
圆周率的计算
蒙塔卡罗方法（通过概率来计算圆周率）
'''
#计算圆周率的程序

'''
#方一
pi=0
n=100
for k in range(n):
    pi += 1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(k*8+6))
print("方一：圆周率的值是：{}\n".format(pi))

#方二
import random
#import perf_counter
darts=1000*1000
hits=0.0
#start=time.perf_conter()
for i in range(1,darts+1):
    x=random.random()
    y=random.random()
    dist=pow(x**2+y**2,0.5)
    if(dist<=1.0):
        hits+=1
pi=4*hits/darts
print("方二 圆周率的值是:{:.8f}".format(pi))
#print("运行的时间是：{:.5f}s(秒)".format(perf_counter()-start)
'''


#举一反三
"""
    理解方法的思维
-数学思维：找到公式，利用公式求解
-计算思维：抽象了一种过程，利用计算机自动化求解

"""










'''
自动轨迹绘制
1、定义数据文件格式（接口）
2、编写程序，根据文件接口解析参数绘制图形
3、编制数据文件
'''
#autotracedraw.py
import turtle as t
t.title('自动绘制')
t.setup(800,600,0,0)#绘制窗口的大小
t.pencolor("red")#画笔的初始颜色
t.pensize(5)#画笔的大小
#数据文件的读取
datals = []
f=open("data.txt")
for line in f:
    line=line.replace("\n","")
    datals.append(list(map(eval,line.split(","))))
    #list map eval 作用是去掉字符串中的引号
    #f.close()

#自动绘制
for i in range (len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])#表示一行的第一个元素表示行进距离
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
f.close()














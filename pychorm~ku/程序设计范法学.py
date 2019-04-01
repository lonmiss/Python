'''
程序设计的方法学
8.1体育经济分析
8.2python程序设计思维
8.3python第三方库安装
8.4模块7：os库的基本使用
8.5第三方库自动安装脚本

计算思维：抽象+自动化

比赛规则：
    -双人比赛：A&B，回合制，5局3胜
    -开始时一方先发球，直至判分，接下来省着发球
    -球员只能在发球局的分，15分一局

逐步组成复杂系统的有效测试方法
-分单元测试，逐步组装
-按照自顶向下相反的路径操作
-直至，系统各部分以组装的思路经过测试和验证
'''
"""
体育竞技分析
    程序总体框架及步骤
-1、打印程序的介绍性信息式                  printinfo(）
-2、获得西横须运行参数：proA,proB,n         getinputs()
-3、利用qui球员A和B的能力值，模拟n局比赛    simngames()
-4、输出球员A和B获胜比赛的场次及概率        printsummary()
"""

from random import random
#简单介绍
def printsummary(winsA,winsB):
    n=winsA+winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获得{}场比赛，占{:0.1%}".format(winsA,winsA/n))
    print("选手B获得{}场比赛，占{:0.1%}".format(winsB, winsB/n))
def printintro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("这个程序运行需要A和B的能力值（以0和1之间的小数表示）")

#第一阶段
def getinputs():
    a=eval(input("请输入选手A的能力值（0-1）："))
    b=eval(input("请输入选手B的能力值（0-1）："))
    n=eval(input("模拟比赛的场次："))
    return a,b,n

#判断一局比赛结束
def gameover(a,b):
    return a==15 or b==15 #返回的是true or flase

#模拟1局比赛，并将其循环N次

#进行一局比赛
def simonegame(probA,probB):
    scoreA,scoreB=0,0
    serving="A"
    while not gameover(scoreA,scoreB):
        if serving=="A":
            if random()<probA:
                scoreA+=1
            else:
                serving="B"
        else:
            if random()<probB:
                scoreB+=1
            else:
                serving="A"
    return scoreA,scoreB

def simngames(n,probA,probB):
    winsA,winsB=0,0
    for i in range(n):
        scoreA,scoreB=simonegame(probA,probB)
        if scoreA>scoreB:
            winsA+=1
        else:
            winsB+=1
    return winsA,winsB


def main():
    printintro()
    probA,probB,n=getinputs()
    winsA,winsB=simngames(n,probA,probB)
    printsummary(winsA,winsB)



main()

"""
举一反三
理解自顶向下和自顶向上
-理解自顶向下的设计思维：分而治之
-理解自低向上的执行思维：模块化集成
-自顶向下是“系统”思维的简化 
"""















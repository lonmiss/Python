'''
序列类型及操作
序列处理函数及方法
元组类型及操作
列表类型及操作
序列类型及应用场景

序列类型定义：
序列是具有先后关系的一组元素
    序列是一维元素向量，元素类型可以不同
    类似数学元素序列
    元素间由序号引导，通过下标访问序列的特定元素

序列类型：字符串类型、元组类型、列表类型
正向递增、反向递减

六个操作符;
    x in s              如果x是序列s的元素，返回True,否则返回False
    x not in s          如果x是序列s的元素，返回False,否则返回True
    s+t                 连接连个序列s和t
    s*n或n*s            将序列s复制n次
    s[i]                索引，返回s中的第i各元素，i是序列号
    s[i:j]或是[j;i:k]     切片，返回序列s中第i个到j以k为步长的元素子序列
       #ls=["python",123,".io"]#['.io', 123, 'python']
       #ls=ls[::-1]
       #print(ls)

五个函数和方法
len(s)          返回序列S的长度
min(s)          返回序列s的最小元素，s中的元素需要可比较
max(s)          返回序列s的最大元素，s中的元素需要课比较
s.index(x)或s.index(x,i,j)   返回序列s从i开始到j位置第一次出现x的位置

元组类型的定义：
元组是序列类型的一种扩展
    元组是一种序列类型，一旦创建就不能被修改
    使用小括号（）或tuple（）创建，元素之间用逗号，分隔
    可以使用或不使用小括号
  元组继承了序列类型的全部通用操作、元组因为创建后不能被修改，因此没有特殊的操作性
    

creature="dog","cat","tiger","human"
print(creature)
#('dog', 'cat', 'tiger', 'human')
color=(0x001100,"blue",creature)
print(color)
#(4352, 'blue', ('dog', 'cat', 'tiger', 'human'))

列表类型的定义
列表是一种序列类型的一种扩展，十分常用
    列表是一种序列类型，创建后可以被随意被修改
    使用方括号[]或list（）创建，元素间逗号，分隔
    可以使用或不使用小括号
        ls=["cat","dog","tiger",1024]
        print(ls)
        #['cat', 'dog', 'tiger', 1024]
        lt=ls
        print(lt)
        #['cat', 'dog', 'tiger', 1024]
        #注意方括号[]真正创建一个列表，赋值进传递引用
    ls[i]=x         替换列表ls第i个元素为x
    ls[i:j:k]=lt    用列表lt替换ls切片后所对应的元素字列表
    del ls[i]       删除ls中第i个元素
    del ls[i:j:k]   删除列表ls中第i个到第j个以k为步长的元素
    ls+=lt          更新列表ls，将列表lt元素增加到列表ls中
    ls*=n           更新列表ls，奇元素重复n次
        ls=["cat","dog","tiger",1024]
        ls[1:2]=[1,2,3,4,5,6]
        print(ls)
        #['cat', 1, 2, 3, 4, 5, 6, 'tiger', 1024]
        del ls[::3]
        print(ls)
        #[1, 2, 4, 5, 'tiger', 1024]
        print(ls * 2)
        #[1, 2, 4, 5, 'tiger', 1024, 1, 2, 4, 5, 'tiger', 1024]
列表类型操作函数和方法
        ls.append(x)        在列表ls最后增加一个元素x
        ls.clear()          删除列表ls中所有的元素
        ls.copy()           生成一个新列表，赋值ls中所有元素
        ls.inset(i,x)       在列表ls的第i个位置增加元素x
        ls.pop(i)           将列表ls中的元素取出并删除
        ls.remove(x)        将列表ls中出现的第一个元素x删除
        ls.reverse()        将列表ls中的元素反转

                ls=[]
        print(ls)
        ls+=[1,2,3,4,5]
        print(ls)
        ls[2]=6
        print(ls)
        ls.insert(2,8)
        print(ls)
        del ls[1]
        print(ls)
        del ls[1:4]
        print(ls)
        print(0 in ls)
        print(ls.index(1))
        """
        []
        [1, 2, 3, 4, 5]
        [1, 2, 6, 4, 5]
        [1, 2, 8, 6, 4, 5]
        [1, 8, 6, 4, 5]
        [1, 5]
        False
        0

数据保护
-如果不希望数据被程序所改变，转换成元组类型
        ls=["cat","dog","tiger",1024]
        ls=tuple(ls)#将列表转换成元组
        print(ls)
        #('cat', 'dog', 'tiger', 1024)
'''





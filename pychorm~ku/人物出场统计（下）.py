#升级代码
import jieba
txt=open("三国.txt","r",encoding="utf-8").read()
excludes={"将军","却说","荆州","二人","不可","不能","如此"}
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="孔明" or word=="孔明曰":
        rword="诸葛亮"
    elif word=="关公"or word=="云长":
        rword="关羽"
    elif word=="玄德" or word=="玄德曰":
        rword="刘备"
    elif word=="孟德" or word=="丞相":
        rword="曹操"
    else:
        word=rword
    counts[word]=counts.get(word,0)+1
for j in excludes:
    del counts[j]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))



'''
import jieba
txt=open("三国.txt","rb",encoding="utf-8").read()

words=jieba.lcut(txt)
counts={}
for word in words:
    if(len(word)==1):
        continue
    else:
        counts[word]=counts.get(word,0)+1
# items() 函数以列表返回可遍历的(键, 值) 元组数组。
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count=items[i]
    print("{0:<10}{1:>20}".format(word,count))
'''



























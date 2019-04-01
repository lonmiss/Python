#计算中位数
def median(numbers):
    sorted(numbers)
    size=len(numbers)
    if size % 2==0:
        med=(numbers[size//2-1]+numbers[size//2])/2
    else:
        med=numbers[size//2]
    return med
def getnums():
    n=[]
    n1=input()
    while n1!="":
        n.append(eval(n1))
        n1=input()
    return n

m=getnums()
print(sorted(m),end=" ")
print("这组数据的中位数是%d\n"%median(m))
print("这组数据的中位数是{}".format(median(m)))

'''
numbers=[9,2,3]
for i in range (len(numbers) - 1):
    for j in range (len(numbers) - i - 1):
        if (numbers[j] > numbers[j + 1]):
            numbers[j + 1], numbers[j] = numbers[j], numbers[j + 1]
for k in range (len(numbers)):
    print("%d\n"%numbers[k])
n=[6,5,9,8,5,3]
print(sorted(n))

'''

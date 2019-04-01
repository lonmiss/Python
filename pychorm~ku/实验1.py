def swap_number(a,b):
    temp=a
    a=b
    b=temp
    print("a=%d,b=%d"%(a,b))
    return a,b


x=3
y=4
swap_number(x,y)
print("%d,%d"%(x,y))

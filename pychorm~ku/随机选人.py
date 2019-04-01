import random
names=['李建民','谢好','刘婉婷','史凯伦','周双文','郑薇薇','郝天恒','李佳宇','张世禹','郭雨晨']
a=random.choice(names)
print("出场的小可爱是：")
print(a)
names.remove(a)
print(names)
print("候补小可爱是：（么么哒）")
print(random.choice(names))
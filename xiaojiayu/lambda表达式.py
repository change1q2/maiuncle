'''
作者：seak
时间：
项目：
题目：
作用：
备注：
python写一些执行脚本时，使用lambda就可以省下定义函数的过程，使用lambda可以使函数更精简
'''
#单个参数
#定义一个普通的函数
def ds(x):
    return 2 * x + 1
#调用这个函数传入参数5
ds(5)
print(ds(5))#打印出来

#定义一个lambda表达的函数
lambda x : 2 * x +1
g = lambda x : 2 * x + 1
g(5)
print(g(5))

print("_________________________")
#多个参数
def add(x,y):
    return x + y
print(add(3,4))

l = lambda x,y : x + y
print(l(5,5))


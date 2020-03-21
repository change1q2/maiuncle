'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''

#help(filter)
# filter(function or None, iterable) --> filter object
#filter解释说明中说filter有2个参数，一个是对象或者空，第二个是可迭代，
'''
function
/ˈfʌŋkʃn/
n. 功能；[数] 函数；职责；盛大的集会
vi. 运行；活动；行使职责

iterable
可迭代的
我们已经知道可以对list、tuple、dict、set、str等类型的数据使用for...in...的循环语法从其中依次拿到数据进行使用，我们把这样的过程称为遍历，也叫迭代。
把可以通过for...in...这类语句迭代读取一条数据供我们使用的对象称之为可迭代对象（Iterable）。
在Python中，迭代可通过for ... in来完成，例如列表的迭代：

可以使用 isinstance() 判断一个对象是否是 Iterable 对象：
from collections import Iterable
isinstance([], Iterable)
 True

'''
#filter会过滤掉0和非Ture的内容
filter(None,[1,0,'dada','aa',False,True])
print(list(filter(None,[1,0,'dada','aa',False,True])))
print("- - - - - - - - - - - -")

#写一个过滤掉偶数的方式
def odd(x):
    return x % 2
temp = range(0,10)
show = list(filter(odd,temp))
print(show)

#使用lambda一行带啊名实现过滤掉偶数
print(list(filter(lambda x: x % 2,range(0,10))))
'''
作者：seak
时间：
项目：
题目：
作用：
备注：

map:映射
'''

#help(map())
'''
    map(func, *iterables) --> map object 
    Make an iterator that computes the function using arguments from
    each of the iterables.  
    Stops when the shortest iterable is exhausted.
    
    map(func， *iterables)——>映射对象
创建一个迭代器，使用来自的参数计算函数每个迭代。
当最短的迭代结束时停止
'''
#map将range(10)产生的值，放到lambda里面进行加工然后再列表中打印出来
print(list(map(lambda x : x * 2,range(10))))
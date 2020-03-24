'''
作者：seak
时间：
项目：
题目：
作用：
备注：
d
'''
#阶层
# def factorial(n):
#     result = n
#     for i in range(1,n):
#         result *= i
#     return result
# num = int(input("请输入一个数："))
# print("递归算法的结果是:{}".format(factorial(num)))

#递归的写法
#递归的条件：
#1.有调用函数自身的行为
#2.有一个正确的返回条件
def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)
number = int(input("请输入一个正整数："))
result = factorial(number)
print("{}的阶层是{}".format(number,result))
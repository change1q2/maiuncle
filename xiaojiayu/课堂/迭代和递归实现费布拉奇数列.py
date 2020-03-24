'''
作者：seak
时间：
项目：
题目：
作用：
备注：
'''

#迭代

# def fab(n):
#     n1 = 1
#     n2 = 1
#     n3 = 1
#
#     if n < 1:
#         print("输入有误！")
#
#     while (n-2) > 0:
#         n3 = n2 +n1
#         n1 = n2
#         n2 = n3
#         n += 1
#     return n3
#
# result = fab(5)
# if result != -1:
#     print(F"总共有{result}只小兔子")
# print(result)

#递归算法
def fab(n):
    if n < 1 :
        print("输入有误!")
        return -1

    if n == 1 or n ==2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

result = fab(2)
if result != -1:
    print("总共有%d只小兔子诞生"%result)

'''
作者：seak
时间：
项目：
题目：
作用：
备注：
知识点：
1.python以.py结尾
2.执行程序： python mai.py
3.print是一个函数，用来打印输入
4.要打印的内容成为参数，参数一定要放在（）里
5.字符串可以是单引号，双引号或者三引号
'''
print("""
             
             |\__|/ _____ //--seak------   \\xx/
             | xx\ /%%%%///   __     __  \\ \
             \_xxx %%%%  /   /  \   /  \    |
             / /x%%%%       ((0) ) ((0) )   |
            / #/|%%%%        \__/   \__/     \__  ______-------
            \#/ |%%%%             @@            \/
              _/%%%%                             |_____
     ________/|%%%%                              |    -----___
-----         |%%%%     \___                  __/
           ___/\%%%%    /  --________________//
     __----     \%%%%                     ___/
    /             \%%%%                   _/
                     \%%%%              _/
                       \%%%%           /
                          \%%         |
                           |%%        |
""")
print('你好，小海')
print('下海，你愿意跟我一起去异次元吗？')
print("-- -- -- -- --- -- --- -- -- -- - -- --")
#6变量，在内存中分配的一个小盒子，后面可以用变量名的名字来使用它里面的值
#7字符串可以通过+来拼接，可以把字符串和变量拼接在一起
#8变量名字小写，比较长的用下划线连接
name = '麦叔'
robot_name = '小麦'
print("你好," + name + ",我是"+ robot_name)
print("-- -- -- -- --- -- --- -- -- -- - -- --")
#format格式化
print("你好{},"  "我是{}".format(name,robot_name))
print("-- -- -- -- --- -- --- -- -- -- - -- --")
#format的进化方法(语法糖衣)
print(f"你好,{name},我是{robot_name}")
#转义字符
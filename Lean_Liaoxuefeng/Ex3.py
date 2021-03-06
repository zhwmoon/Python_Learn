# def fact(n):
#     return fact_item(n,1)
#
# def fact_item(num,prod):
#     if num == 1:
#         return prod
#     else:
#         print(prod)
#         print(num)
#         return fact_item(num-1,num*prod)
#
# res = fact(5)
# print(res)

# -*- coding: utf-8 -*-
'''
请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法。

实现这个算法可以简单分为三个步骤：
    1. 把n-1个盘子由A 移到 B；
    2. 把第n个盘子由A 移到 C；
    3. 把n-1个盘子由B 移到 C；

从这里入手，在加上上面数学问题解法的分析，我们不难发现，移到的步数必定为奇数步：
    1. 中间的一步是把最大的一个盘子由A移到C上去；
    2. 中间一步之上可以看成把A上n-1个盘子通过借助辅助塔（C塔）移到了B上，
    3. 中间一步之下可以看成把B上n-1个盘子通过借助辅助塔（A塔）移到了C上；

参考：https://www.cnblogs.com/dmego/p/5965835.html
'''

def hanoi(n, a, b, c):
    if n == 1:                          # 圆盘只有一个时，只需将其从A塔移到C塔
        print(a, '-->', c)              # 将编b号为1的圆盘从A移到C
    else:
        hanoi(n - 1, a, c, b)           # 递归，把A塔上编号1~n-1的圆盘移到B上，以C为辅助塔
        print(a, '-->', c)              # 把A塔上编号为n的圆盘移到C上
        hanoi(n - 1, b, a, c)           # 递归，把B塔上编号1~n-1的圆盘移到C上，以A为辅助塔

print(hanoi(5, 'A', 'B', 'C'))
# -*- coding: utf-8 -*-
'''
小米二面：
    分子为1的分数称为埃及分数。现输入一个真分数(分子比分母小的分数，叫做真分数)，请将
    该分数分解为埃及分数。如：8/11 = 1/2+1/5+1/55+1/110。
'''
# 埃及分数有多种方式解答，但是题目给出的示例用的是方法一

# 方法一
up,down = list(map(int,input().split('/')))
res = ''

while up!=1:
    if down%(up-1)==0:
        res += '1/'+str(down//(up-1))+'+'
        up = 1
    else:
        res += '1/'+str(down//up+1)+'+'
        x = up-down%up
        down = down*(down//up+1)
        up = x
        if down%up == 0:
            down = down//up
            up = 1
res += '1/'+str(int(down))
print(res)


# 方法二
'''
输入： a/b
解法：不断找到小于当前a/b的最大的埃及分数（即分子为1的真分数）
推导：设c为 b/a 的商，r为余数，则：
    b = a*c+r，
    除以a,有 b/a = c + r/a < c+1 (因为余数 0<=r <a)
    同时取倒数： a/b > 1/(c+1)
    即 1/(c+1)是小于当前真分数a/b的最大埃及分数，
    设 e=c+1，则剩余的部分为 (a/b) - (1/e) = (a*e-b)/b*e,继续找真分数(a*e-b)/b*e的下一个
    最大的埃及分数，直至最后所有分解后的真分数均为埃及分数。
'''

#up,down = list(map(int,input().split('/')))
#res = ''
#
#while up!=1:
#    if down%up != 0:
#        tmp = '1/'+str(down//up+1) + '+'
#        res += tmp
#        e = down//up+1
#        up = up*(e)-down
#        down = down*(e)
#        # 处理特殊情况，即 剩余部分(a*e-b)/b*e的分子已经等于1的情况，外循环就不会进入，需要在
#        # 此处判断后连接到输出字符串上
#        if down%up == 0:
#            down = down//up
#            up = 1
#            res += '1/' + str(down)
#    else:
#        down = down//up
#        up = 1 
#        res += '1/' + str(down)
#print(res) 
#            

# -*- coding: utf-8 -*-
"""
    赛吗网的编程题，需要自己处理输入输出部分。
    1)python输入：
            s = input() # 任意格式的输入，转换成字符串
            nm = []
            if s != "":
                # for x in s.split():  # 这样写也行
                for x in s.strip().split():  
                    nm.append(int(x))  
            m = nm[0]
            n = nm[1]
    2)python输出：
            print()
    3)输入多组数据，输出多组数据结果，用循环表示
        while True:
    4)python直接写代码，都不用写类和函数名；c++的话直接写在main()函数里；
    
            使用语言：C++
            参考正解代码如下：
            
            #include<stdio.h>
            
            int main(){
                int m,n;
                while(scanf("%d%d",&m,&n)!=EOF){
                        int t=0;
                    for(int i=m; i<=n; i++){
                        int a=i/100;
                        int b=i%100/10;
                        int c=i%10;
                        
                        if(i==a*a*a+b*b*b+c*c*c && t==0){
                            printf("%d ",i);
                            t++;
                        }
                        else if(i==a*a*a+b*b*b+c*c*c && t==1){
                            printf("%d ",i);
                        }
                    }
                    if(t!=0){ printf("\n"); }
                    if(t==0){ printf("no\n"); }
                }
                return 0;
            }

"""
"""
题目描述：
    春天是鲜花的季节，水仙花就是其中最迷人的代表，数学上有个水仙花数，他是这样定义的： “水仙花数”是
    指一个三位数，它的各位数字的立方和等于其本身，比如：153=1^3+5^3+3^3。 现在要求输出所有在m
    和n范围内的水仙花数。
输入
    输入数据有多组，每组占一行，包括两个整数m和n（100<=m<=n<=999）。

输出
    对于每个测试实例，要求输出所有在给定范围内的水仙花数，就是说，输出的水仙花数必须大于等于m,并且
    小于等于n，如果有多个，则要求从小到大排列在一行内输出，之间用一个空格隔开; 如果给定的范围内不存
    在水仙花数，则输出no; 每个测试实例的输出占一行。

样例输入
    100 120
    300 380

样例输出
    no
    370 371
"""

while True:
    s = input()
    nm = []
    if s != "":
        # for x in s.split():  # 这样写也行
        for x in s.strip().split():  
            nm.append(int(x))  
    m = nm[0]
    n = nm[1]

    if m>n:
    	print('no')
    res = []
    for num in range(m,n+1):
        gewei = num%10
        shiwei = num//10%10
        baiwei = num//100
        if num == (baiwei**3+shiwei**3+gewei**3):
            res.append(str(num))
    if len(res)<=0:
        print('no')
    ret = ' '
    print(ret.join(res))

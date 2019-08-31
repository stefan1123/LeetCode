# coding:utf-8

'''
华为2019.08.28 软件题第二题
题目：一个矩阵，5*5，取相邻（二个成员有一个边是相同的）的6个，输入一个6个成员列表，判断是否满足？
矩阵成员如下：
[[1,2,3,4,5],
 [11,12,13,14,15],
 [21,22,23,24,25],
 [31,32,33,34,35],
 [41,42,43,44,45]]

'''              

def hasPath(matrix, len_mat, path):
    # write code here
    if len(path)<0 or len_mat<0 or len(matrix)<(len_mat):
        return False
    visited = [False]*(len_mat)
    global pathlen 
    pathlen = 0 
    for i in range(len_mat):
        if check(matrix,len_mat,i,path,visited,pathlen):
            return True
    return False
    
def check(matrix,len_mat,i,path,visited,pathlen):
    if pathlen == len(path):
        return True
        # 检查是否符合要求
    curhaspath = False
    if i>=0 and i<len_mat \
        and path[pathlen]== matrix[i]\
        and not visited[i]:
            # 先改变当前的状态
        visited[i] = True
        pathlen += 1
                    
        curhaspath = check(matrix,len_mat, i+1,path,visited,pathlen)
        
        if not curhaspath:
            visited[i] = False
            pathlen -= 1
    return curhaspath

if __name__ == '__main__':

    datas=['1 2 3 4 5 11\n', '1 2 11 14 25 15\n','2 3 4 5 11 12\n']

    for data in datas:
        data = data.split('\n')[0].split(' ')
        data = list(map(int,data))
            
        matrix = [1,2,3,4,5,
                      11,12,13,14,15,
                      21,22,23,24,25,
                      31,32,33,34,35,
                      41,42,43,44,45]
                        
        if hasPath(matrix,5*5, data):
            print(1)
        else:
            print(0)
    

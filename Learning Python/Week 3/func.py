#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
Python 函数学习

@author zhaoyb
'''
#----------------------------------------------------------------------
def intersect(s1,s2):
    """"""
    lst = list()
    for i in s1:
        if i in s2:
            lst.append(i)
    return lst

'''
fibonacci F(n) = F(n - 1) + F(n - 2), n>1, F(1) = Fib(2) = 1 
'''
import re
#----------------------------------------------------------------------
def _fibonacci(n):
    """fibonacci序列-递归算法"""
    n = int(n)
    if n <= 1:
        return n
    else:
        return _fibonacci(n-1) + _fibonacci(n-2)
#----------------------------------------------------------------------
def _fibonacci2(n):
    """fibonacci序列-非递归算法-效率更高"""
    nRet = nP = nPp = 1
    n = int(n)
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return nRet
    else:
        for i in range(3,n+1):
            nRet,nPp= nP + nPp,nP
            nP = nRet
        return nRet
#----------------------------------------------------------------------
def get_fibonacci(n,recurrence=True):
    """
    获取斐波那契序列，默认使用递归算法(recurrence=True)
    """
    #保证输入的是正数
    pattern = re.compile(r'\d')
    match =pattern.match(str(n))
    if not match:
        print "The input char '%s' is not a positive integer,skipping..." % (n)
    else:    
        ls =list()
        if(recurrence):
            for i in range(n+1):
                ls.append(_fibonacci(i))
        else:
            for i in range(n+1):
                ls.append(_fibonacci2(i))                
        return ls
#----------------------------------------------------------------------
def fibonacci(n):
    """
    利用yeild生成器
    """
    nRet,nP=0,1
    for i in range(n+1): 
        yield nRet
        nRet,nP=nP,nRet+nP 

if __name__ == "__main__":
    
    #-----找到相同字符---
    s1='abcde'
    s2='defgl'
    print intersect(s1, s2)
    
    #-----fibonacci-----
    # yield
    print list(fibonacci(10))  
    # 递归
    print get_fibonacci(10)
    # 自写非递归
    print get_fibonacci(10, recurrence=False)
    
    print list(fibonacci(20))  
    print get_fibonacci(20)
    print get_fibonacci(20, recurrence=False)
    
    ###递归算法效率低下，计算50的fibonacci序列时候要计算3分钟
    #print get_fibonacci(50)
    print list(fibonacci(50))  
    print get_fibonacci(50, recurrence=False)
    
    ###非递归算法计算500的fibonacci序列也只需要1秒
    print get_fibonacci(500, recurrence=False)
    print list(fibonacci(500)) 
    

    
    
                
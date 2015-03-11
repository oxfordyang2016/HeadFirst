#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Python 模块

@author zhaoyb
'''

#----------------------------------------------------------------------
def fetchfromleft(string,locnumber):
    """"""
    return string[:locnumber]
#----------------------------------------------------------------------
def turntoupercase(string):
    """"""
    return string.upper()

if __name__ == "__main__":
    
    print fetchfromleft("asdfghjkl;'",6)
    print turntoupercase("asdfghjkl;'")
    

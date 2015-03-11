#!/usr/bin/env python
#-*- coding: gb2312 -*-  


########################################################################
class Counter(dict):
    """
    OOP思想的统计对象.
    继承自dict  self本身就是一个dict
    """
    
    '''被统计的字符关键字'''
    __data_key = "abcdefghijklmnopqrstuvwxyz"
    
    '''被统计的字段串'''
    __data_str = str()
    
    #----------------------------------------------------------------------
    def __init__(self,strValue,strKey=None):
        """Constructor"""
        '''strValue 需要统计的字符串,strKey 统计的关键字可以自定义'''
        
        self.__data_str = strValue
        if strKey is not None:
            self.__data_key = strKey
        
        #初始化字典
        for c in self.__data_key:
            self[c] = 0
            
        #统计频度 字母转换为小写
        for s in self.__data_str.lower():
            if s in  self.__data_key:
                self[s] = self[s] + 1        
        
    #----------------------------------------------------------------------
    def getStrValue(self):
        """获取数据"""
        return self.__data_str
    #----------------------------------------------------------------------
    def getStrKey(self):
        """获取数据"""
        return self.__data_key
    
    #----------------------------------------------------------------------
    def getResult(self):
        """获取未排序的数据"""
        return self
    
    #----------------------------------------------------------------------
    def getSortByKeyResult(self,reserve=False):
        '''根据关键字升序'''
        return self.__sorted(lambda x:x[0], reserve=reserve)
    
    #----------------------------------------------------------------------
    def getSortByValueResult(self,reserve=True):
        '''根据频度降序'''
        return self.__sorted(lambda x:x[1], reserve=reserve)
    
    #----------------------------------------------------------------------
    def __sorted(self,key,reserve=False):
        '''排序'''
        return sorted(self.iteritems(), cmp=None, key=key,reverse=reserve)
    
if __name__ == "__main__":
    
    #获取排序字符串 存放于脚本当前目录data.txt
    data_str = str()
    with open('data.txt','r') as data_file:
        for data_line in data_file:
            data_str += data_line  
    '''
    Useage: c = Counter(data_str,data_key)
    if data_key do not input, it will use default value 'a-z' lower case.
    '''
    c = Counter(data_str)
    print "未排序字典"
    
    print c.getResult()
    
    print "字母升序排列."
    s_dict_asc = c.getSortByKeyResult()
    for i in s_dict_asc:
        print str(i).replace('(','').replace(')','').replace(',',':')
    
    print "频度降序排列."
    s_dict_desc = c.getSortByValueResult()
    for i in s_dict_desc:
        print str(i).replace('(','').replace(')','').replace(',',':')

        
    
    
    
        
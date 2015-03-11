#!/usr/bin/env python
#-*- coding: gb2312 -*-  


########################################################################
class Counter(dict):
    """
    OOP˼���ͳ�ƶ���.
    �̳���dict  self�������һ��dict
    """
    
    '''��ͳ�Ƶ��ַ��ؼ���'''
    __data_key = "abcdefghijklmnopqrstuvwxyz"
    
    '''��ͳ�Ƶ��ֶδ�'''
    __data_str = str()
    
    #----------------------------------------------------------------------
    def __init__(self,strValue,strKey=None):
        """Constructor"""
        '''strValue ��Ҫͳ�Ƶ��ַ���,strKey ͳ�ƵĹؼ��ֿ����Զ���'''
        
        self.__data_str = strValue
        if strKey is not None:
            self.__data_key = strKey
        
        #��ʼ���ֵ�
        for c in self.__data_key:
            self[c] = 0
            
        #ͳ��Ƶ�� ��ĸת��ΪСд
        for s in self.__data_str.lower():
            if s in  self.__data_key:
                self[s] = self[s] + 1        
        
    #----------------------------------------------------------------------
    def getStrValue(self):
        """��ȡ����"""
        return self.__data_str
    #----------------------------------------------------------------------
    def getStrKey(self):
        """��ȡ����"""
        return self.__data_key
    
    #----------------------------------------------------------------------
    def getResult(self):
        """��ȡδ���������"""
        return self
    
    #----------------------------------------------------------------------
    def getSortByKeyResult(self,reserve=False):
        '''���ݹؼ�������'''
        return self.__sorted(lambda x:x[0], reserve=reserve)
    
    #----------------------------------------------------------------------
    def getSortByValueResult(self,reserve=True):
        '''����Ƶ�Ƚ���'''
        return self.__sorted(lambda x:x[1], reserve=reserve)
    
    #----------------------------------------------------------------------
    def __sorted(self,key,reserve=False):
        '''����'''
        return sorted(self.iteritems(), cmp=None, key=key,reverse=reserve)
    
if __name__ == "__main__":
    
    #��ȡ�����ַ��� ����ڽű���ǰĿ¼data.txt
    data_str = str()
    with open('data.txt','r') as data_file:
        for data_line in data_file:
            data_str += data_line  
    '''
    Useage: c = Counter(data_str,data_key)
    if data_key do not input, it will use default value 'a-z' lower case.
    '''
    c = Counter(data_str)
    print "δ�����ֵ�"
    
    print c.getResult()
    
    print "��ĸ��������."
    s_dict_asc = c.getSortByKeyResult()
    for i in s_dict_asc:
        print str(i).replace('(','').replace(')','').replace(',',':')
    
    print "Ƶ�Ƚ�������."
    s_dict_desc = c.getSortByValueResult()
    for i in s_dict_desc:
        print str(i).replace('(','').replace(')','').replace(',',':')

        
    
    
    
        
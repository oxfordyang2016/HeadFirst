#-*- coding: gb2312 -*-  
'''避免中文乱码'''
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

统计data.txt中文件中出现a-z的次数，存储在字典中，并升序打印出来 

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import operator
#定义需要统计的字符集
characters = 'abcdefghijklmnopqrstuvwxyz'

data_str = ''
"""
获取被统计字符文件
"""
with open('data.txt','r') as data_file:
    for data_line in data_file:
        data_str += data_line
        
"""
创建空字典
"""
#创建字典对象
r_dict = dict();
#初始化字典
for c in characters:
    r_dict[c] = 0
#统计频度 字母转换为小写
for s in data_str.lower():
    if s in characters:
        r_dict[s] = r_dict[s] + 1

#排序
"""
sorted(iterable, cmp=None, key=None, reverse=False)

iterable：是可迭代类型;
cmp：用于比较的函数，比较什么由key决定,有默认值，迭代集合中的一项;
key：用列表元素的某个属性和函数进行作为关键字，有默认值，迭代集合中的一项;
reverse：排序规则. reverse = True 或者 reverse = False，有默认值。
返回值：是一个经过排序的可迭代类型，与iterable一样。

一般来说，cmp和key可以使用lambda表达式。

"""

#s_dict = sorted(r_dict.iteritems(), cmp=None, key=operator.itemgetter(1),reverse=True)


"""
lambda x:x[0]  key排序 同理 operator.itemgetter(0)
lambda x:x[1]  value排序  同理 operator.itemgetter(1)
"""

#字母升序
s_dict_asc = sorted(r_dict.iteritems(), cmp=None, key=operator.itemgetter(0),reverse=False)

#频度降序
s_dict_desc = sorted(r_dict.iteritems(), cmp=None, key=lambda x:x[1],reverse=True)

print "字母升序排列."
for i in s_dict_asc:
    print str(i).replace('(','').replace(')','').replace(',',':')

print "频度降序排列."
for i in s_dict_desc:
    print str(i).replace('(','').replace(')','').replace(',',':')
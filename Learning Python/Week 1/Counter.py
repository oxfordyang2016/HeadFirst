#-*- coding: gb2312 -*-  
'''������������'''
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

ͳ��data.txt���ļ��г���a-z�Ĵ������洢���ֵ��У��������ӡ���� 

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import operator
#������Ҫͳ�Ƶ��ַ���
characters = 'abcdefghijklmnopqrstuvwxyz'

data_str = ''
"""
��ȡ��ͳ���ַ��ļ�
"""
with open('data.txt','r') as data_file:
    for data_line in data_file:
        data_str += data_line
        
"""
�������ֵ�
"""
#�����ֵ����
r_dict = dict();
#��ʼ���ֵ�
for c in characters:
    r_dict[c] = 0
#ͳ��Ƶ�� ��ĸת��ΪСд
for s in data_str.lower():
    if s in characters:
        r_dict[s] = r_dict[s] + 1

#����
"""
sorted(iterable, cmp=None, key=None, reverse=False)

iterable���ǿɵ�������;
cmp�����ڱȽϵĺ������Ƚ�ʲô��key����,��Ĭ��ֵ�����������е�һ��;
key�����б�Ԫ�ص�ĳ�����Ժͺ���������Ϊ�ؼ��֣���Ĭ��ֵ�����������е�һ��;
reverse���������. reverse = True ���� reverse = False����Ĭ��ֵ��
����ֵ����һ����������Ŀɵ������ͣ���iterableһ����

һ����˵��cmp��key����ʹ��lambda���ʽ��

"""

#s_dict = sorted(r_dict.iteritems(), cmp=None, key=operator.itemgetter(1),reverse=True)


"""
lambda x:x[0]  key���� ͬ�� operator.itemgetter(0)
lambda x:x[1]  value����  ͬ�� operator.itemgetter(1)
"""

#��ĸ����
s_dict_asc = sorted(r_dict.iteritems(), cmp=None, key=operator.itemgetter(0),reverse=False)

#Ƶ�Ƚ���
s_dict_desc = sorted(r_dict.iteritems(), cmp=None, key=lambda x:x[1],reverse=True)

print "��ĸ��������."
for i in s_dict_asc:
    print str(i).replace('(','').replace(')','').replace(',',':')

print "Ƶ�Ƚ�������."
for i in s_dict_desc:
    print str(i).replace('(','').replace(')','').replace(',',':')
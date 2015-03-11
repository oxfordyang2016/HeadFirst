# -*- coding: UTF-8 -*-

alphalist = ['a','b','c','d','e']

"""
使用最普通的index 自增， python 没有c类语言的 for(；；)这样的语法，最初可能会想到这个
"""
def loopmethod1(alist):
	print "the first method:"
	index=0
	for i in alist:
		print "index:",index,"element:",i
		index+=1

"""
使用range函数，实现对于list的遍历
"""
def loopmethod2(alist):
	print "the second method:"
	for i in range(len(alist)):
		print "index:",i,"element:",alist[i]

"""
使用while方法
"""
def loopmethod3(alist):
	print "the third method"
	index=0
	while index < len(alist):
		print "index:",index,"element:",alist[index]
		index+=1

"""
使用zip方法(python 2.3以前的推荐)
"""
def loopmethod4(alist):
	print "the 4th method"
	for i,e in zip(range(len(alist)),alist):
		print "index:",i,"element:",e

"""
目前推荐的用法，可以很方便的获得list中的各个元素和它对应的下表,程序也简单易懂
"""
def loopmethod5(alist):
	print "the 5th method"
	for i, e in enumerate(alist):
		print "index:",i,"element:",e


"""
生成数据文件的一个方法
"""
def generate_flight_sql():
	with open () 


if __name__ == '__main__':
	loopmethod1(alphalist)
	loopmethod2(alphalist)
	loopmethod3(alphalist)
	loopmethod4(alphalist)
	loopmethod5(alphalist)
	loopmethod6(alphalist)
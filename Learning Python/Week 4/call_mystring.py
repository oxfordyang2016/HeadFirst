#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Python 调用模块

@author zhaoyb
'''

import mystring

print mystring.fetchfromleft("asdfghjkl;'",6)
print mystring.turntoupercase("asdfghjkl;'")
print '---------------------------------'

import mystring as m

print m.fetchfromleft("asdfghjkl;'",6)
print m.turntoupercase("asdfghjkl;'")
print '---------------------------------'

from mystring import fetchfromleft
from mystring import turntoupercase

print fetchfromleft("asdfghjkl;'",6)
print turntoupercase("asdfghjkl;'")
print '---------------------------------'
 
from mystring import fetchfromleft as f
from mystring import turntoupercase as t

print f("asdfghjkl;'",6)
print t("asdfghjkl;'")
print '---------------------------------'
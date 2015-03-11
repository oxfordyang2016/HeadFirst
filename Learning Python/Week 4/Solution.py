#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
Python 算法题
Problem:
Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.
找出一个不字符串中不出现重复字母的最长字符串
@author zhaoyb
'''

#----------------------------------------------------------------------
def lengthOfLongestSubstring(s):
    """
    思路:从头开始遍历字符，不出现相同字符，组成字符串，出现相同，记录遍历长度，如果大于已经出现的最长，保存字符串，否则放弃，从新字符串继续遍历。
    """
    string = ""
    temp = ""
    counter = 0
    #遍历字符串
    for index in range(len(s)):
        for i in s[index:]:
            #如果temp中存在,截断，重新计数
            if i in temp:
                #如果当前计数大于已经记录的最长字符串,替换之
                if counter > len(string):
                    string=temp
                #记录当前这个已经重复的字符串-所以counter从1开始同时temp += i
                counter=0
                temp=""
                break;
            else:
                #记录长度,拼接字符串
                counter += 1
                temp += i
        #遍历完成，查看最后未重复的字符是否最长
        if counter > len(string):
            string=temp
    return string

if __name__=="__main__":
    print lengthOfLongestSubstring("abcabcbb")
    print lengthOfLongestSubstring("abcdefgabcdefghabcedfghiabcdefghijasdfghjkl;'1234567890")
    print lengthOfLongestSubstring("acbpawertyuioba")

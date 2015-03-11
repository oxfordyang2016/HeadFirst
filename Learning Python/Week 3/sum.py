#!/usr/bin/env python
#-*-coding:utf-8-*-


#----------------------------------------------------------------------
def twoSum(num,target):
    dic = {}
    """"""
    if type(num) == list:
        pass
    else:
        print "The argument 'num' must be a list,system is exiting..."
        return (0,0)
    if type(target) == int:
        pass
    else:
        print "The argument 'target' must be a integer,system is exiting..."
        return (0,0)
    #dict
    length = len(num)
    for i in range(length):
        dic[num[i]] = i+1
    for i in range(length):
        imp = num[i]
        deft = target - imp
        index = dic.get(deft)
        if index == None or index == i+1:
            continue
        else:
            return (i+1,index)
    return (0,0)
if __name__ == "__main__":
    import func
    num = []
    num = list(func.fibonacci(2000))
    print twoSum(num,4)
    print twoSum(num,11)
    print twoSum(num,90)
    print twoSum(num,199)
    print twoSum(num,238)
    print twoSum(num,380)
    print twoSum(num,990)
    print twoSum(num,1605)
    print twoSum(num,2592)
    print twoSum(num,4189)

"""格式化数据"""
def format_unique_list(in_list):
    new_list = []
    for item in in_list:
        item = item.replace('-',':')
        item = item.replace('.',":")
        if item not in new_list:
            new_list.append(item)
    return new_list
'''获取list'''
def get_list(file_name):
    try:
        with open(file_name,'r') as in_file:
            in_data = in_file.readline()
            in_list = in_data.strip().split(',')
            return in_list;
    except IOError as err:
        print "error occured: " +str(err)
        
'''生成字典'''
def get_dict(file_name):
    try:
        with open(file_name,'r') as in_file:
            in_data = in_file.readline()
            in_list = in_data.strip().split(',')
            a_set = dict()
            a_set['name'] = in_list.pop(0)
            a_set['birthday'] = in_list.pop(0)
            a_set['scores'] = in_list            
            return a_set;
    except IOError as err:
        print "error occured: " +str(err)
'''排序'''
def count_sort(in_list,reverse=False):
    in_list = format_unique_list(in_list)
    if(reverse) :
        in_list.sort(reverse=True)
    else:
        in_list.sort()    
    return in_list

#a_list = get_list('sarah.txt')
#a_set = dict()
#a_set['name'] = a_list.pop(0)
#a_set['birthday'] = a_list.pop(0)
#a_set['scores'] = a_list


a_set = get_dict('sarah.txt')
print a_set['name'] + "'s fastest times are: " + str(count_sort(a_set['scores'])[0:3])
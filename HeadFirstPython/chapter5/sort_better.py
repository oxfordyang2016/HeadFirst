#排序学习
#sort()   - > 原地排序 将排序后的值赋值给原list - print list.sort() ->none
#sorted() - > 复制排序 将排序后的值复制到新的list - new_list =  sorted(list) | print sorted(list) ->排序后的list

#数据统一格式化-清除重复数据
def format_unique_list(in_list):
    new_list = []
    for item in in_list:
        item = item.replace('-',':')
        item = item.replace('.',":")
        if item not in new_list:
            new_list.append(item)
    return new_list

#抽象出函数
def get_list(file_name,reverse=False):
    with open(file_name,'r') as in_file:
        in_data = in_file.readline()
        in_list = in_data.strip().split(',')
        in_list = format_unique_list(in_list)
        if(reverse) :
            in_list.sort(reverse=True)
        else:
            in_list.sort()
        return in_list

try:
    print get_list("james.txt",False)[0:3]
    print get_list("julie.txt",False)[0:3]
    print get_list("mikey.txt",False)[0:3]
    print get_list("sarah.txt",False)[0:3]
    
except IOError as err:
    print 'error occured when handle file: ' + str(err)
        
#排序学习
#sort()   - > 原地排序 将排序后的值赋值给原list - print list.sort() ->none
#sorted() - > 复制排序 将排序后的值复制到新的list - new_list =  sorted(list) | print sorted(list) ->排序后的list
def format_data(in_list):
    new_list = []
    for item in in_list:
        item = item.replace('-',':')
        item = item.replace('.',":")
        new_list.append(item)
    return new_list
        
try:
    with open('james.txt','r') as james_file:
        james_data = james_file.readline();
        james_list = james_data.strip().split(',') #分离成list
        james_list = format_data(james_list) #替换成统一格式
        james_list.sort() # 排序
        print james_list
    with open('julie.txt','r') as julie_file:
        julie_data = julie_file.readline();
        julie_list = julie_data.strip().split(',')
        julie_list = format_data(julie_list)
        julie_list.sort()
        print julie_list  
    with open('mikey.txt','r') as mikey_file:
        mikey_data = mikey_file.readline();
        mikey_list = mikey_data.strip().split(',')
        mikey_list = format_data(mikey_list)
        mikey_list.sort()    
        print mikey_list  
    with open('sarah.txt','r') as sarah_file:
        sarah_data = sarah_file.readline();
        sarah_list = sarah_data.strip().split(',')
        sarah_list = format_data(sarah_list)
        sarah_list.sort(r)
        print sarah_list
except IOError as err:
    print 'error occured when handle file: ' + str(err)
        
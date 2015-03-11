import nester
import os
lilei=[]
hanmeimei=[]
try:
    data = open("sketch.txt")
    for e_line in data:
        try:
            (role,words) = e_line.split(':',1)
            #删除前后空格
            words = words.strip()
            if role == 'lilei':
                lilei.append(words)
            elif role == 'hanmeimei':
                hanmeimei.append(words)
        except ValueError as err:
            print '----some error occured: ' + str(err)
    data.close()
except IOError as err:
    print '----some error occured: ' + str(err)
    
try:
    lilei_file = open('lilei_data.txt','w')
    hanmeimei_file = open('hanmeimei_data.txt','a')
    
    for ls_lilei in lilei:
        lilei_file.write(ls_lilei)
    for ls_hanmeimei in hanmeimei:
        hanmeimei_file.write(ls_hanmeimei)
    
except IOError as err:
    print '----some error occured: ' + str(err)
finally:
    lilei_file.close()
    hanmeimei_file.close()    
    
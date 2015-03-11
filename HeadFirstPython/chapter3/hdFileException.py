try:
    data = open("sketch.txt")
    for e_line in data:
        #split 当文件分割出的string个数大于1时，会报错，这里 split(":",1) 只分割第一个冒号
        #但是问题又来了，如果这一行中没有冒号怎么办呢？-->捕获异常，让程序继续执行
        try:
            (role,words) = e_line.split(':',1)
            print role,
            print ' said: ',
            print words ,
        except ValueError:
            print '-------------------------------------------------------------------------'
            print '----some error occured ,but we catched it ,so the program can continue---'
            print '-------------------------------------------------------------------------'
    data.close()
except IOError:
    print '-----------------------------------------'
    print '----The file sketch.txt does not exist---'
    print '-----------------------------------------'
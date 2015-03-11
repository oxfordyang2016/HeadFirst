########################################################################
## 类: 为了维护数据的健壮性和代码可读性 使用类  其中方法服用dictDemo.py中 ##
## 这是一个定制类
########################################################################
class Athlete:
    """"""
    #----------------------------------------------------------------------
    def __init__(self,name,birthday=None,times=[]):
        """Constructor"""
        '''
        构造方法
        '''
        self.name = name
        self.birthday = birthday
        self.times = times
        
    def top3(self):
        new_list = []
        for item in self.times:
            item = item.replace('-',':')
            item = item.replace('.',":")
            if item not in new_list:
                new_list.append(item)
        return sorted(new_list)[0:3]    
    
    def add_time(self,time):
        self.times.append(time)
    
    #----------------------------------------------------------------------
    def add_times(self,times):
        """"""
        self.times.extend(times)
        
########################################################################
## 继承类：上面一个定制类中 list 的操作都是 赋给一个新的list 如果类继承list
## 那么 self 就是一个list
########################################################################
class AthleteList(list):
    """"""
    
    #----------------------------------------------------------------------
    def __init__(self,name,birthday=None,times=[]):
        """Constructor"""
        list.__init__([])
        self.name = name 
        self.birthday =birthday
        self.extend(times)
    
    #----------------------------------------------------------------------
    def top3(self):
        """"""
        new_list = []
        for item in self:
            item = item.replace('-',':')
            item = item.replace('.',":")
            if item not in new_list:
                new_list.append(item)
        return sorted(new_list)[0:3]    
        
#直接获取Athlete类
def get_athlete(file_name):
    try:
        with open(file_name,'r') as in_file:
            in_data = in_file.readline()
            in_list = in_data.strip().split(',')  
            return Athlete(in_list.pop(0),in_list.pop(0),in_list);
    except IOError as err:
        print "error occured: " +str(err)
        
#获取AthleteList类
def get_athlete_list(file_name):
    try:
        with open(file_name,'r') as in_file:
            in_data = in_file.readline()
            in_list = in_data.strip().split(',')  
            return AthleteList(in_list.pop(0),in_list.pop(0),in_list);
    except IOError as err:
        print "error occured: " +str(err)
########################################################################
##                            Test case                               ##
########################################################################
sarah = get_athlete('sarah.txt')
print sarah.name + "'s fastest times are: " + str(sarah.top3())

sarah = get_athlete_list('sarah.txt')
print sarah.name + "'s fastest times are: " + str(sarah.top3())

jobs = Athlete('Jobs')
jobs.add_time('2.1')
print jobs.name + "'s fastest times are: " + str(jobs.top3())
jobs.add_times(['2.01','2.3','2.2'])
print jobs.name + "'s fastest times are: " + str(jobs.top3())

# -*- coding: UTF-8 -*-
#insert into  flight  values('CA1831','PEKSHA','2015-2-25''2015-3-20');
import datetime
import random
import datetime

city_list=['PEK','SHA','CAN','CTU','CHQ','XMN','TSN','LAX','JFK','TAO','LON']
airline_list=['CA','MU','3U','CN','CZ']

def write_to_sqlfile():
	with open('insertflight.sql','w') as f:
		sqllist=_generate_sql()
		for sql in sqllist:
			f.write(sql+'\n')


def _generate_sql():
	sql_template='insert into flight values(\'{flightnumber}\',\'{citypair}\',\'{begindate}\',\'{enddate}\');'
	sqllist = []
	for i in range(100):
	 	sqllist.append(sql_template
	 		.format(flightnumber=_generate_random_flightnumber(),
	 			citypair=_generate_random_citypair(),
	 			begindate=_get_sysdate(),
	 			enddate=_get_sysdate_offset_date(random.randint(1,30))))
	return sqllist




def _get_sysdate():
	return datetime.date.today().isoformat()

"""
根据偏移量返回时间
"""
def _get_sysdate_offset_date(offset):
	return (datetime.date.today()+datetime.timedelta(days=offset)).isoformat()

"""
返回一个随机的航班号
"""
def _generate_random_flightnumber():
	return airline_list[random.randint(0,len(airline_list)-1)]+str(random.randint(100,9999))

"""
返回一个随机的城市对
"""
def _generate_random_citypair():
	org=random.randint(0,len(city_list)-1)
	des=random.randint(0,len(city_list)-1)
	while org==des: #防止起飞城市和到达城市相等
		des=random.randint(0,len(city_list)-1)
	return city_list[org]+city_list[des]


if __name__ == '__main__':
	write_to_sqlfile()

	#下面是保留的测试项，大家是怎么测试的呢？
	print _generate_sql()
	print _generate_random_flightnumber()
	print _generate_random_citypair()
	print _get_sysdate()
	print _get_sysdate_offset_date(10)
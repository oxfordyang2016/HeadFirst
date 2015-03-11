#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
CZ 指令生成

@author zhaoyb
'''

#----------------------------------------------------------------------
def genetate_asi_command(flt,start_date,end_date):
    """"""
    return "AS:V/"+flt+"/"+start_date+"/"+end_date+"/D/CBS"
#----------------------------------------------------------------------
def genetate_openav_command(flt,start_date,end_date):
    """"""
    return "AS:R/"+flt+"/"+start_date+"/"+end_date+"/D/C1E"

def save_command(s):
    with open('generate_command.txt','w') as generate_command_file:
	for line in s:
	    generate_command_file.write(line+"\n")
		    
def main():
    commands = []
    start_date = str(raw_input('please input the start date:'))
    end_date = str(raw_input('please input the end date:'))
    config = int(raw_input("Choose the target command,'1' for 'ASI' system ,'2' for 'OpenAV' system:"))
    
    with open('cz_flight.txt','r') as cz_flight_file:
	if config == 1:
	    for flt in cz_flight_file:
		commands.append(str(genetate_asi_command(str(flt).replace('\n',''), start_date, end_date)).replace(' ',''))
	elif config == 2:
	    for flt in cz_flight_file:
		commands.append(str(genetate_openav_command(str(flt).replace('\n',''), start_date, end_date)).replace(' ',''))	    
	else:
	    print 'The input config is %s, do not hava this config ,system exiting' % config
    
    save_command(commands)
    
    if config == 1:
	print "genetate_asi_command finished."
    elif config == 2:
	print "genetate_openav_command finished."
if __name__ == "__main__":
    main()
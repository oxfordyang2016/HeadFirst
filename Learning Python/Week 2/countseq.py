# -*- coding: UTF-8 -*-

with open('ASI_STAT_150119.log') as f:
	counter=0
	for line in f:
		if line.find('SSRREQ')>-1:
			counter=counter+1
	print counter
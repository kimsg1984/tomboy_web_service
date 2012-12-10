#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: SunGyo Kim
# Email: Kimsg1948@gmail.com
# irc.freenode #ubuntu-ko Sungyo

import re
import os
import urllib

listFile = open('./notefile/manifest.xml')
list_content = listFile.read()
title_and_number = re.findall('<note (.+) />' , list_content)
listFile.close()
   
for t in title_and_number:
	null = 0
	newestFile = re.findall('id="(.+)" rev="(.+)"' , t)
	n_newestFile = int(newestFile[0][1])
	if n_newestFile > 99:
		newestFile = '%s/%s/%s.note' %(newestFile[0][1][0:-2], newestFile[0][1], newestFile[0][0])
	else:
		newestFile = '0/%s/%s.note' %(newestFile[0][1], newestFile[0][0])
	 
	#print '%s' %newestFile
	
	try:
		sourceFile = open('./notefile/%s' %(newestFile))
		content = sourceFile.read()
		title = re.findall(r'<title>(.+)</title>', content)
		
		try: 
			title = title[0].lower()
		except:
			null = 0
		
		print '{link}%s{/link}'%title,  
		print '{note}%s{/note}' %newestFile


	except:
		null = 0
		print 'fail: %s' %newestFile
sourceFile.close()
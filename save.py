#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: SunGyo Kim
# Email: Kimsg1948@gmail.com
# irc.freenode.net #ubuntu-ko Sungyo

# $python ./htmlparser.py $edited_file_name $notefile

import re
import os
import urllib
import sys
import subprocess
import datetime

def writeLog(comment):
	# import datetime
	t = datetime.datetime.now()
	comment = '%s : %s : %s \n ' %(t, sys.argv[0], comment)
	logfile = open('./log.txt', 'a')
	logfile.write('%s' %comment)
	logfile.close()
	# writeLog('def addTag, for l in link : %s fail to remove ' %l)

writeLog('\'%s\' file start to save to \'%s\'' %(sys.argv[1], sys.argv[2]))	
try:
	WORK_DIR='./notefile'
	edited_file = open(sys.argv[1])
	content = edited_file.read()
	edited_file.close()
except:
	writeLog('fail open the file')
	print 'unsucceed'	


edited_file_name = open(os.path.join(WORK_DIR, sys.argv[2]), 'w')
edited_file_name.write(content)
edited_file_name.close()

if os.path.isfile(os.path.join(WORK_DIR, sys.argv[2])) and os.path.getsize(os.path.join(WORK_DIR, sys.argv[2])) > 0:
	print 'succeed'
else:
	print 'Error'	
	writeLog('fail: save')



# content_xml_file = open('test.kkkk' , 'w')
# content_xml_file.write('%s')
# content_xml_file.close()
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: SunGyo Kim
# Email: Kimsg1948@gmail.com
# irc.freenode.net #ubuntu-ko Sungyo




import re
import os
import urllib
import sys
import datetime

## <def> ##

def writeLog(comment):
	t = datetime.datetime.now()
	comment = '%s : %s : %s \n ' %(t, sys.argv[0], comment)
	logfile = open('./log.txt', 'a')
	logfile.write('%s' %comment)
	logfile.close()

def readLastVer():
	listFile = open(os.path.join(WORK_DIR, 'manifest.xml'))
	list_content = listFile.read()
	last_ver = re.findall('<sync revision="(.+)" server-id' , list_content)
	last_ver = int(last_ver[0])
	listFile.close()
	return last_ver

def readFromServer():		
	notefile_sync_file = open('./notefile_sync.txt')
	server_ver = notefile_sync_file.read()
	server_ver = int(server_ver)
	notefile_sync_file.close()
	return server_ver

def editNotefile(notefile, server_ver):
	notefile_split = notefile.split("/")
 	if server_ver > 99:
 		server_ver = str(server_ver)
		notefile_edited = '%s/%s/%s' %(server_ver[0:-2], server_ver, notefile_split[-1])
	else:
		server_ver = str(server_ver)
		notefile_edited = '0/%s/%s' %(server_ver, notefile_split[-1])
	return notefile_edited



## </def> ##
WORK_DIR = './notefile'
notefile=sys.argv[1]
last_ver = readLastVer()

try:
	server_ver = readFromServer()

except:
	# 'first time!!'
	server_ver = last_ver + 1

server_ver = last_ver + 1
notefile_edited = editNotefile(notefile, server_ver)

print '%s' %notefile_edited
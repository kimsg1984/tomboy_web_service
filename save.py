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

WORK_DIR = './notefile'

def writeLog(comment):
	# import datetime
	t = datetime.datetime.now()
	comment = '%s : %s : %s \n ' %(t, sys.argv[0], comment)
	logfile = open('./log.txt', 'a')
	logfile.write('%s' %comment)
	logfile.close()
	# writeLog('def addTag, for l in link : %s fail to remove ' %l)

def mkSyncFolder(server_ver, notefile_edited_split):
	folder1=os.path.join(WORK_DIR, notefile_edited_split[0])
	folder2=os.path.join(folder1, notefile_edited_split[1])
	if not os.path.isdir(folder1):
		os.mkdir(os.path.join(folder1))
	if not os.path.isdir(folder2):
		os.mkdir(os.path.join(folder2))
	return folder2

def writeToManifest(folder2, list_content):
	listFile = open(os.path.join(WORK_DIR, 'manifest.xml'), 'w')
	listFile.write(list_content)
	listFile.close()
	listFile = open(os.path.join(folder2, 'manifest.xml'), 'w')
	listFile.write(list_content)
	listFile.close()

def writeToServer(server_ver):
	notefile_sync_file = open('./notefile_sync.txt', 'w')
	notefile_sync_file.write('%d' %server_ver)
	notefile_sync_file.close()


def saveEditedFile(content):
	edited_file_name = open(os.path.join(WORK_DIR, sys.argv[2]), 'w')
	edited_file_name.write(content)
	edited_file_name.close()
	if os.path.isfile(os.path.join(WORK_DIR, sys.argv[2])) and os.path.getsize(os.path.join(WORK_DIR, sys.argv[2])) > 0:
		print 'succeed'
	else:
		print 'Error'	
		writeLog('fail saveEditedFile')

#################################################

writeLog('\'%s\' file start to save to \'%s\'' %(sys.argv[1], sys.argv[2]))	
notefile_edited = sys.argv[2]
notefile_edited_split = notefile_edited.split("/")
listFile = open(os.path.join(WORK_DIR, 'manifest.xml'))
list_content = listFile.read()
listFile.close()

notefile_id = notefile_edited_split[-1].split(".")
last_note_ver = re.findall('<note id="%s" rev="(.+)" />' %(notefile_id[0]) , list_content)
last_server_ver = re.findall(r'<sync revision="(.+)" server-id', list_content)
last_server_ver = int(last_server_ver[0])
server_ver = last_server_ver + 1

folder2 = mkSyncFolder(server_ver, notefile_edited_split)

try:
	WORK_DIR='./notefile'
	edited_file = open(sys.argv[1])
	content = edited_file.read()
	edited_file.close()
	saveEditedFile(content)
	try:
		list_content = list_content.replace('<sync revision="%d" server-id' %(last_server_ver),'<sync revision="%d" server-id' %(server_ver))
		try:
			list_content = list_content.replace('  <note id="%s" rev="%s" />\n'%(notefile_id[0], last_note_ver[0]), '')
			list_content = list_content.replace('</sync>', '  <note id="%s" rev="%d" />\n</sync>' %(notefile_id[0], server_ver))
		except:
			# it's first time...!!
			writeLog('it\'s first time. id: %s' %notefile_id[0])
			list_content = list_content.replace('</sync>', '  <note id="%s" rev="%d" />\n</sync>' %(notefile_id[0], server_ver))
		try:
			writeToManifest(folder2, list_content)
			try:
				writeToServer(server_ver)
			except:
				writeLog('fail writeToServer:%s' %server_ver)
				print 'fail writeToServer:%s' %server_ver
		except:
			print 'fil to writeToManifest'
			writeLog('fail writeToManifest')
	except:
		writeLog('fail  write server id :%s' %server_ver)
		print 'fail  write server id :%s' %server_ver
	
	
except:
	writeLog('fail open the file')
	print 'fail open the file'





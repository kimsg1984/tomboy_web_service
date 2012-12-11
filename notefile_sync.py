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

def writeLog(comment):
	t = datetime.datetime.now()
	comment = '%s : %s : %s \n ' %(t, sys.argv[0], comment)
	logfile = open('./log.txt', 'a')
	logfile.write('%s' %comment)
	logfile.close()

def readLastVer(WORK_DIR):
	listFile = open(os.path.join(WORK_DIR, 'manifest.xml'))
	list_content = listFile.read()
	last_ver = re.findall('<sync revision="(.+)" server-id' , list_content)
	last_ver = int(last_ver[0])
	# print last_ver
	listFile.close()
	return last_ver

def writeToManifest(WORK_DIR, folder2, list_content):
	listFile = open(os.path.join(WORK_DIR, 'manifest.xml'), 'w')
	listFile.write(list_content)
	listFile.close()
	listFile = open(os.path.join(folder2, 'manifest.xml'), 'w')
	listFile.write(list_content)
	listFile.close()
	# print '%s' %list_content

def syncFolderNManifest(WORK_DIR, last_ver, server_ver, notefile_edited):
	notefile_edited_split = notefile_edited.split("/")
	folder1=os.path.join(WORK_DIR, notefile_edited_split[0])
	folder2=os.path.join(folder1, notefile_edited_split[1])
	if not os.path.isdir(folder1):
		os.mkdir(os.path.join(folder1))
		
	if not os.path.isdir(folder2):
		os.mkdir(os.path.join(folder2))
		
	listFile = open(os.path.join(WORK_DIR, 'manifest.xml'))
	list_content = listFile.read()
	listFile.close()
	
	notefile_id = notefile_edited_split[-1].split(".")
	last_note_ver = re.findall('<note id="%s" rev="(.+)" />' %(notefile_id[0]) , list_content)
	list_content = list_content.replace('<sync revision="%d" server-id' %(last_ver) ,'<sync revision="%d" server-id' %(server_ver))
	list_content = list_content.replace('  <note id="%s" rev="%s" />\n'%(notefile_id[0], last_note_ver[0]), '')
	list_content = list_content.replace('</sync>', '  <note id="%s" rev="%d" />\n</sync>' %(notefile_id[0], server_ver))
	writeToManifest(WORK_DIR, folder2, list_content)

def writeToServer(server_ver):
	notefile_sync_file = open('./notefile_sync.txt', 'w')
	notefile_sync_file.write('%d' %server_ver)
	notefile_sync_file.close()

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

WORK_DIR = './notefile'
notefile=sys.argv[1]

last_ver = readLastVer(WORK_DIR)

try:
	server_ver = readFromServer()

except:
	# 'first time!!'
	server_ver = last_ver + 1

server_ver = last_ver + 1
notefile_edited = editNotefile(notefile, server_ver)
syncFolderNManifest(WORK_DIR, last_ver, server_ver, notefile_edited)
writeToServer(server_ver)
	

print '%s' %notefile_edited
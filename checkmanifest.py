import re
import os
import urllib
import sys
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

def mkNotefile_dir(note_ver, notefile):
	if note_ver > 99:
 		note_ver = str(note_ver)
		notefile_dir = '%s/%s/%s' %(note_ver[0:-2], note_ver, notefile)
	else:
		note_ver = str(note_ver)
		notefile_dir = '0/%s/%s' %(note_ver, notefile)
	return notefile_dir


writeLog("Start to check :manifest.xml")


manifest_file = open(os.path.join(WORK_DIR, 'manifest.xml'))
manifest = manifest_file.read()
manifest_file.close()

note_id = re.findall(r'<note id="(.+)" rev="(.+)" />', manifest)
# last_note_ver = re.findall(r'<sync revision="(.+)" server-id', list_content)

for i in note_id:
	notefile = '%s.note' %i[0]
	note_ver = int(i[1])
	notefile_dir = mkNotefile_dir(note_ver, notefile)
	# print '%s, %s' %(notefile, note_ver)
	# print '%s' %(notefile_dir)
	if os.path.isfile(os.path.join(WORK_DIR, notefile_dir)):
		# print 'succeed'
		a=0
	else:
		print '%s' %(notefile_dir)
		print 'Error'	
		# writeLog('fail saveEditedFile')

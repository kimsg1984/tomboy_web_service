#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: SunGyo Kim
# Email: Kimsg1948@gmail.com
# irc.freenode.net #ubuntu-ko Sungyo

# $result1=shell_exec("python ./htmlparser.py $edited_file_name");

import re
import os
import urllib
import sys
import subprocess
import datetime


def writeLog(comment):
	t = datetime.datetime.now()
	comment = '%s : %s : %s \n ' %(t, sys.argv[0], comment)
	logfile1 = open('./log.txt', 'a')
	logfile1.write('%s' %comment)
	logfile1.close()
	# writeLog('def addTag, for l in link : %s fail to remove ' %l)

def replace_decorations(string_content):
    string_content = string_content.replace('&nbsp;', ' ')
    string_content = string_content.replace('</b>', '</bold>')
    string_content = string_content.replace('<b>', '<bold>')
    string_content = string_content.replace('</font>', '</highlight>')
    string_content = string_content.replace('<font style="background-color: yellow">', '<highlight>')
    string_content = string_content.replace('</i>', '</italic>')
    string_content = string_content.replace('<i>', '<italic>')
    string_content = string_content.replace('</font>', '</size:small>')
    string_content = string_content.replace('<font size="2">', '<size:small>')
    string_content = string_content.replace('</font>', '</size:large>')
    string_content = string_content.replace('<font size="4">', '<size:large>')
    string_content = string_content.replace('</font>', '</size:huge>')
    string_content = string_content.replace('<font size="5">', '<size:huge>')
    string_content = string_content.replace('</li>', '</list-item dir="ltr">')
    string_content = string_content.replace('<li>', '<list-item dir="ltr">')
    string_content = string_content.replace('</ul>', '</list>')
    string_content = string_content.replace('<ul>', '<list>')
    string_content = string_content.replace('</strike>', '</strikethrough>')
    string_content = string_content.replace('<strike>', '<strikethrough>')
    return string_content


def content_perser(content_html):
	content_html = '%s' %replace_decorations(content_html)
	try:
		for l in link:
			content_html = content_html.replace('<a href="dylink.php?title=%s" >%s</a>' %(l, l), '<link:internal>%s</link:internal>' %(l))
	except:
		null = 0 # there is no link:internal
	try:
		for lu in linkurl:
			content_html = content_html.replace('<a href="http://%s" >http://%s</a>' %(lu, lu), '<link:url>%s</link:url>' %(lu))
	except:
		null = 0 # there is no link:url
	return content_html


def bodyTag(title, content_xml):
	content_xml = """<title>%s</title><text xml:space="preserve"><note-content version="0.1">%s\n%s</note-content></text>""" %(title[0], title[0], content_xml)
	return content_xml

def xmlTag(content_xml, meta_data):
	content_xml = """<?xml version="1.0" encoding="utf-8"?>
<note version="0.3" xmlns:link="http://beatniksoftware.com/tomboy/link" xmlns:size="http://beatniksoftware.com/tomboy/size" xmlns="http://beatniksoftware.com/tomboy">%s%s</note>""" %(content_xml, meta_data)
	return content_xml

def getCallResult(cmdARGS):
	fd_popen = subprocess.Popen(cmdARGS.split(), stdout=subprocess.PIPE).stdout
	data = fd_popen.read().strip()
	fd_popen.close()
	return data

def addTag(content_xml):
	listFile = open('./notefile/list.txt')
	content = listFile.read()
	titles = re.findall(r'{link}(.+){/link}', content)
	titles.sort()
	
	# for l in link:
	# 	l = l.lower()
		# try: 
		# 	titles.remove('%s' %l)
		# except:
		# 	writeLog('def addTag, for l in link : %s fail to remove ' %l)
	try:
		titles.remove('%s' %title)
	except:
		null = 0 # content has no same word as 'title'
		
	# t = '웹톰'

	for t in titles:
		try:
			content_xml = content_xml.replace( ' %s ' %t, ' <link:internal>%s</link:internal> ' %t)
			
		except:
			null = 0

		
	return content_xml

writeLog('start to parse %s' %sys.argv[1])
WORK_DIR = './notefile'
edited_file = open(sys.argv[1])
content = edited_file.read()
edited_file.close()



content_html = content.replace('target="_blank"', '')
title = re.findall(r'<title>(.+)</title>', content_html)
meta_data = re.findall(r'<!--{meta_data}(.+){/meta_data}-->', content_html)
content_link=content_html.replace('</a>', '</a>\n')
content_link = content_link.replace('<br>', '\n')
link = re.findall(r'<a href="dylink.php\?title=(.+)" >', content_link)
linkurl = re.findall(r'<a href="http://(.+)" >', content_link)
content_html = re.findall(r'</title>(.+)<!--{meta_data}', content_html)
content_html = content_html[0].replace('<br>', '\n')


try:
	content_xml = '%s' %content_perser(content_html)
except:
	content_xml = '\'fail to read content_html\'\n'

try:
	meta_data = meta_data[0]
	meta_data = meta_data.replace('<br>', '\n')
except:
	content_xml = '\'fail to read meta_data\'\n%s'%content_xml
	meta_data = " "

try:
	content_xml = bodyTag(title, content_xml)
except:
	content_xml = bodyTag(' ', content_xml)

content_xml = xmlTag(content_xml, meta_data)

try:
	content_xml = addTag(content_xml)
except:
	writeLog('addTag error')

content_xml_file = open('./%s.xml' %sys.argv[1], 'w')
content_xml_file.write('%s' %content_xml)
content_xml_file.close()




print 'succeed'

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: SunGyo Kim
# Email: Kimsg1948@gmail.com
# irc.freenode.net #ubuntu-ko Sungyo

import re
import os
import urllib
import sys

def replace_decorations(string_content):
	string_content = string_content.replace('</bold>', '</b>')
	string_content = string_content.replace('<bold>', '<b>')
	string_content = string_content.replace('</highlight>', '</font>')
	string_content = string_content.replace('<highlight>', '<font style="background-color: yellow">')
	string_content = string_content.replace('</italic>', '</i>')
	string_content = string_content.replace('<italic>', '<i>')
	string_content = string_content.replace('</size:small>', '</font>')
	string_content = string_content.replace('<size:small>', '<font size="2">')
	string_content = string_content.replace('</size:large>', '</font>')
	string_content = string_content.replace('<size:large>', '<font size="4">')
	string_content = string_content.replace('</size:huge>', '</font>')
	string_content = string_content.replace('<size:huge>', '<font size="5">')
	string_content = string_content.replace('</list-item dir="ltr">', '</li>')
	string_content = string_content.replace('<list-item dir="ltr">', '<li>')
	string_content = string_content.replace('</list>', '</ul>')
	string_content = string_content.replace('<list>', '<ul>')
	string_content = string_content.replace('</link:internal>', '</a>')
	string_content = string_content.replace('</link:url>', '</a>')
	string_content = string_content.replace('</strikethrough>', '</strike>')
	string_content = string_content.replace('<strikethrough>', '<strike>')
	return string_content

WORK_DIR = './notefile'
notefile = open(os.path.join(WORK_DIR, sys.argv[1]))
content = notefile.read()
notefile.close()

head_title = re.findall(r'<title>(.+)</title>', content)
content_title = re.findall(r'<note-content(\sversion="\d.\d">|>)(.*)', content)
content_link=content.replace('</link:internal>', '</link:internal>\n')
link = re.findall(r'<link:internal>(.+)</link:internal>', content_link)
linkurl = re.findall(r'<link:url>(.+)</link:url>', content)
note_content_version = re.findall(r'<note-content(.+)\n', content)
content = content.replace('<note-content%s\n' % (note_content_version[0]), '<note-content>')
content = content.replace('\n', '<br>')
meta_data = re.findall(r'</text>(.+)</note>', content)
note_content = re.findall(r'<note-content(\sversion="\d.\d">|>)(.+)</note-content>' , content)

try:
	content_html = '%s' %replace_decorations(note_content[0][1])
	try:
		for l in link:
			content_html = content_html.replace('<link:internal>%s' %(l), '<a href="dylink.php?title=%s">%s' %(l, l))
	except:
		null = 0 # there is no link:internal
	try:
		for lu in linkurl:
			content_html = content_html.replace('<link:url>%s' %(lu), '<a href="%s">%s' %(lu, lu))
	except:
		null = 0 # there is no link:url
except:
	content_html = 'fail to read content\n'
try:
	content_html = "%s<!--{meta_data}%s{/meta_data}-->"%(content_html, meta_data[0])
except:
	content_html = 'fail to read meta_data\n%s'%content_html

print '%s' %content_html
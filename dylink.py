#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author: SunGyo Kim
# Email: Kimsg1948@gmail.com
# irc.freenode.net #ubuntu-ko Sungyo




## to exec: python dylink.py "$title"

import re
import sys

def special_characters(title_content):
	title_content = title_content.replace('&', '&amp;')
	title_content = title_content.replace('<', '&lt;')
	title_content = title_content.replace('>', '&gt;')

	return title_content

# #< (less-than sign) 	&lt;
# #> (greater-than sign) 	&gt;
# #& (ampersand) 	&amp;


title=sys.argv[1]

try: 
	title = title.lower()
except:
	null = 0


title = special_characters(title)


listFile = open('./notefile/list.txt')
content = listFile.read()
notefile = re.findall(r'{link}%s{/link} {note}(.+){/note}' %title, content)
try:
	print '%s' %notefile[0]

except:
	print '0' # <-- it means 'fail'


listFile.close()

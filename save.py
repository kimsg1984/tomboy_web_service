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


WORK_DIR='./notefile'
edited_file = open(sys.argv[1])
content = edited_file.read()
edited_file.close()


edited_file_name = open(os.path.join(WORK_DIR, sys.argv[2]), 'w')
edited_file_name.write(content)
edited_file_name.close()


print 'succeed'	
# content_xml_file = open('test.kkkk' , 'w')
# content_xml_file.write('%s')
# content_xml_file.close()
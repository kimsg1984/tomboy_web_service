# -*- coding: UTF-8 -*-
#!/usr/bin/python

# Author: Seowon Jung
# Email: jswlinux@gmail.com
# irc.freenode #ubuntu-ko Seony

import re
import os
import urllib

def replace_decorations(string_content, link):
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

def html_head(title, html_content):
	html_title="""<html><head><META http-equiv="Content-Type" content="text/html; charset=euc-kr"><meta name = "viewport" content = "initial-scale = 1.0"><title>%s</title><style type="text/css">
        
	body {  }
	h1 { font-size: x-large;
     	     font-weight: bold;
     	     border-bottom: 1px solid black; }
	div.note {
		   position: relative;
		   display: block;
		   padding: 5pt;
		   margin: 5pt; 
		   white-space: -moz-pre-wrap; /* Mozilla */
 	      	   white-space: -pre-wrap;     /* Opera 4 - 6 */
 	      	   white-space: -o-pre-wrap;   /* Opera 7 */
 	      	   white-space: pre-wrap;      /* CSS3 */
 	      	   word-wrap: break-word;      /* IE 5.5+ */ }
	</style></head><body><div class="note" id="%s"><a name="%s"></a><h1>%s</h1>%s</div></body></html>"""%(title, title, title, title, html_content)
	return html_title

HOME_DIR = os.path.expanduser('~')
WORK_DIR = '%s/.local/share/tomboy' %(HOME_DIR)
#WORK_DIR = '%s/바탕화면/script/test' %(HOME_DIR)

WEB_DIR = '%s/문서/mount_tomboy' %(HOME_DIR) 
#WEB_DIR = '%s/바탕화면/script/test' %(HOME_DIR)

#WEB_DIR = '%s/.local/share/tomboy' %(HOME_DIR)
#WEB_DIR = '/var/www/tomboy'
for f in os.listdir(WORK_DIR):
	ext = os.path.splitext(f)[-1]

	if ext == '.note':
		print 'File name: %s' %f, 
		sourceFile = open(os.path.join(WORK_DIR, f))
		content = sourceFile.read()

		title = re.findall(r'<title>(.+)</title>', content)
		
		content=content.replace(' xmlns:link="http://beatniksoftware.com/tomboy/link" xmlns:size="http://beatniksoftware.com/tomboy/size"', '')
		dup_title = re.findall(r'<note-content(\sversion="\d.\d">|>)(.*)', content)
		

		content_link=content.replace('</link:internal>', '</link:internal>\n')
		link = re.findall(r'<link:internal>(.+)</link:internal>', content_link)
		linkurl= re.findall(r'<link:url>(.+)</link:url>', content)
		
		try: 
			content = content.replace(dup_title[0][1], '')

		except:
			print 'none dup_title'


		content = content.replace('\n', '<br>')
		note_content = re.findall(r'<note-content(\sversion="\d.\d">|>)(.+)</note-content>', content)
		try:
			try:
				try:
					html_content = '%s' %(html_head(title[0], replace_decorations(note_content[0][1], link[0])))
					for l in link:

						l_url=unicode('%s'%(l), 'utf8')
						l_url=urllib.quote(l_url.encode('utf8'))
						html_content = html_content.replace('<link:internal>%s' %(l), '<a href="%s.html">%s' %(l_url, l))
						
						
					for lu in linkurl:
						html_content = html_content.replace('<link:url>%s' %(lu), '<a href="%s">%s' %(lu, lu))


					
				except:
					html_content = '%s' %(html_head(title[0], replace_decorations(note_content[0][1], '')))

			


			except:
				html_content = '%s' %(html_head(title[0], ''))

			encoding_content=""
			for h in html_content:
				try: 
					#print '%s' %(h)
					h=unicode(h,'utf-8').encode('euc-kr')
					h=h.replace('<br>', '\n')
				except:
					fake=1
				encoding_content='%s%s'%(encoding_content, h)
			#print encoding_content

			
			html_content=unicode(html_content,'utf-8').encode('euc-kr')
			html_content=html_content.replace('<br>', '\n')

			

			output = open('%s/%s.html' %(WEB_DIR, title[0]), 'w')
			output.write(html_content)
			output.close()

			if os.path.isfile(os.path.join(WEB_DIR, '%s.html' %title[0])) and os.path.getsize(os.path.join(WEB_DIR, '%s.html' %title[0])) > 0:
				print ' -> %s.html created.' %title[0]
				#print ''

			else:
				print ' -> Error' %title[0]
				#print ''

		except:
			print ' -> Error(no content??)'


			sourceFile.close()

print 'Done'

#!/usr/bin/python3

import cgi
import subprocess
import cgitb  #importing cgi-traceback module
# to showcommon error in web-browser
cgitb.enable()
print("content-type:text/html")
print("")
webdata=cgi.FieldStorage()#this is for collect all the html code with data
#now extracting value of x
data=webdata.getvalue('x')

#sending output of client via web-server
output=subprocess.getoutput(data)
print("<h2><pre>")
print(output)
print("</pre></h2>")

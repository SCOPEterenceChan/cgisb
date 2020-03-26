#!/usr/local/bin/python3.8
import time
import cgi


html5top='''
<!-- {fname} -->
<!DOCTYPE html>
<html>
 <head>
  <title>{title}</title>
 </head>
 <body>
  <h1>{header}</h1>
'''
html5bottom='''
 </body>
</html>
'''

print (html5top.format(fname='sblogon.py', title='CGI',header='Simple Billing App'))

form = cgi.FieldStorage()

if 'name' in form:
    if form['password'].value == 'abc':
        print ("<h1>Welcome, %s!</h1>" % form[ 'name' ].value)
        print('''
        <p /><ul>
                <li><a href=sbsort.py>Customer Table</a></li><br />
                <li><a href=sbsearch.py>Search Customer</a></li>
            </ul>
        <p />
        ''')
    else: print ("<h1>password incorrect %s!</h1>" % form[ 'password' ].value)
    

print (time.ctime( time.time() ))
print (html5bottom)

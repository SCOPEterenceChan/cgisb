#!/usr/local/bin/python3.8

import time
import cgi
import urllib.request

fileIn=urllib.request.urlopen('http://personal.cityu.edu.hk/~dcywchan/2004dco10803/datafile1.txt')
byteStr = fileIn.read()
lines=byteStr.decode('utf-8')
lineSep=lines.split('\r\n')

clientDT=['Name','Address','Balance']
clientDL=[]
        
for e in lineSep:
    if e != '':
        clientRec=e.split('_')
        if len(clientDL) == 0:
            if clientRec[2] == 'D':
                clientDL.append(dict(zip(clientDT,
                                     [clientRec[0],clientRec[1],float(clientRec[3])])))
            else:
                clientDL.append(dict(zip(clientDT,
                                     [clientRec[0],clientRec[1],-float(clientRec[3])])))            
        else: 
            i = 0
            while i < len(clientDL) and clientDL[i]['Name'] != clientRec[0]:
                i += 1
            
            if i == len(clientDL):
                if clientRec[2] == 'D':   
                    clientDL.append(dict(zip(clientDT,
                                         [clientRec[0],clientRec[1],float(clientRec[3])])))
                else:
                    clientDL.append(dict(zip(clientDT,
                                         [clientRec[0],clientRec[1],-float(clientRec[3])])))
            else:
                if clientRec[2] == 'D':
                    clientDL[i]['Balance'] += float(clientRec[3])
                else: clientDL[i]['Balance'] -= float(clientRec[3])

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
tableHeader='''
<table border=1>
<tr><th>Name</th><th>Address</th><th>Balance</th></tr>
'''

form = cgi.FieldStorage()

if 'searchBy' in form:
    searchBy = form[ 'searchBy' ].value
else:
    searchBy = 'Name'
    
if 'searchKey' in form:  
    searchKey = form.getvalue('searchKey')
else:
    searchKey = ''
   
print (html5top.format(fname='sbsearch.py',title='searching',header='Customer Table'))

print(tableHeader)

for e in clientDL:
    if str(e.get(searchBy)) == searchKey:
        print ('<tr><td>'+e.get('Name')+'</td>'+
               '<td>'+e.get('Address')+'</td>'+
               '<td>'+str(e.get('Balance'))+'</td></tr>')

print('</table>')
print('<hr>')

print ('''
      <form method = 'post' action = '/cgi-bin/sbsearch.py'>
      Search By:<br />''')

for field in clientDT:
    print ('''<input type = 'radio' name = 'searchBy'
      value = '%s' />''' % field)
    print (field)
    print ("<br />")

print ('''<br />Search Key:<br />
      <input type = 'text' name = 'searchKey'
      value = '' />
      <br /><br /><input type = 'submit' value = 'Search' />
      </form><br /><br />''')
 

print (time.ctime( time.time() ))
print (html5bottom)
#!/usr/local/bin/python3.8

import time
import cgi
fileIn = open('datafile1.dat', 'r')

clientDT=['Name','Address','Balance']
clientDL=[]

line = fileIn.readline()

while line != '':
    clientRec=line.split('_')
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
            
    line = fileIn.readline()
                
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

if 'sortBy' in form:
    sortBy = form[ 'sortBy' ].value
else:
    sortBy = 'Name'
 
if 'sortOrder' in form:
    sortOrder = form[ 'sortOrder' ].value
else:
    sortOrder = 'ASC'   
   
print (html5top.format(fname='sbsort.py',title='sorting',header='Customer Table'))

print(tableHeader)
for e in sorted(clientDL, key = lambda c : c[sortBy],reverse = sortOrder == 'DESC'):
    print ('<tr><td>'+e['Name']+'</td>'+
           '<td>'+e['Address']+'</td>'+
           '<td>'+str(e['Balance'])+'</td></tr>')

print('</table>')
print('<hr>')

print (
'''
\n<form method = 'post' action = '/cgi-bin/sbsort.py'>
   Sort By:<br />
''')

for field in clientDT:
    print ('''<input type = 'radio' name = 'sortBy'
      value = '%s' />''' % field)
    print (field)
    print ("<br />")

print ('''<br />Sort Order:<br />
      <input type = 'radio' name = 'sortOrder'
      value = 'ASC' checked = 'checked' />
      Ascending
      <input type = 'radio' name = 'sortOrder'
      value = 'DESC' />
      Descending
      <br /><br /><input type = 'submit' value = 'SORT' />
      </form><br />''')
 
print (time.ctime( time.time() ))
print (html5bottom)
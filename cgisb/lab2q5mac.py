#!/usr/local/bin/python3.8

import time
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
print (html5top.format(fname='lab2q5.py',title='Simple Billing Web Page',header='Customer Table'))

print(tableHeader)

for e in sorted(clientDL, key = lambda c: c['Name']):
    if e['Balance'] != 0:
        print ('<tr><td>'+e['Name']+'</td>'+
               '<td>'+e['Address']+'</td>'+
               '<td>'+str(e['Balance'])+'</td></tr>')

print('</table>')
print('<p />')

print (time.ctime( time.time() ))
print (html5bottom)

fileIn.close()

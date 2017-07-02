#!/usr/bin/env python
# coding: utf-8
# stringTest.py


import baseTools
from baseTools import *
print 
if 'win' in sys.platform:
  os.system('cls')
else:
  os.system('clear')

params = sys.argv[1]
print params
print "Numeric", params.isdigit()
print "Alpha  ", params.isalpha()
#print sys.argv
 


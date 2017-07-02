#!/bin/bash
# -*- codign:utf-8 -*-
# /baseTools/common/getVersion/getVer.py
# Coded by Richard Polk, Jr
#
#----------------------------------------------------

#
import baseTools
from baseTools import *
print
if 'win' in sys.platform:
  os.system('cls')
else:
  os.system('clear')

cmnd = "lsb_release -a"
os.system(cmnd)
print
P("Hit the <Enter> key to return to the menu.", validResponses=[13], echo=0)




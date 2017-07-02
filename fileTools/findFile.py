#!/bin/bash
# -*- codign:utf-8 -*-
import os
from string import split

def search_file(filename, search_path):
   """Given a search path, find file
   """
   file_found = 0
   #paths = string.split(search_path, pathsep)
   paths = search_path.split(os.pathsep)
   print paths
   for path in paths:
      if os.path.exists(os.path.join(path, filename)):
          file_found = 1
          break
   if file_found:
      return os.path.abspath(os.path.join(path, filename))
   else:
      return None

if __name__ == '___main__':
   search_path = '/bin' + os.pathsep + '/usr/bin'  # ; on windows, : on unix
   find_file = search_file('ls',search_path)
   if find_file:
      print "File found at %s" % find_file
   else:
      print "File not found"


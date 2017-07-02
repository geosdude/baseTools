#!/bin/bash
# -*- codign:utf-8 -*-
# baseTools.sysTools.getch
# Code modified by Richard Polk
#----------------------------------------------------

print '  |' + __name__ + '| ---'

class _Getch:
  # This class is a base class
  """Gets a single character from standard input. Does not echo to the screen."""
  def __init__(self):
    try:
      self.impl = _GetchWindows()
    except ImportError:
      self.impl = _GetchUnix()

  def __call__(self):
    return self.impl()

class _GetchUnix:
  def __init__(self):
    import tty, sys

  def __call__(self):
    import sys, tty, termios
    sys.stdout.write("Hit a key and see what happends!  ")
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    message = str(ord(ch)) + " "
    sys.stdout.write(message)
    return ch

class _GetchWindows:
  def __init__(self):
    import msvcrt

  def __call__(self):
    import msvcrt
    sys.stdout.write("Hit a key and see what happends!  ")
    message = str(ord(ch)) + " "
    sys.stdout.write(message)
    return msvcrt.getch()

if __name__ == '__main__': # a little test
   print 'Press a key'
   inkey = _Getch()
   import sys
   for i in xrange(sys.maxint):
      k=inkey()
      val = ord(k)
      if val == 27:
        print 'you pressed Escape.'
        break
      else:
        if val == 13:
          print 'you pressed Enter.'
        else:
          print 'you pressed ', k
        print val








#!/bin/bash
# -*- codign:utf-8 -*-
# baseTools.sysTools.term_Tools
# Coded by Richard Polk
#----------------------------------------------------

print '  |' + __name__ + '| ---'

class _Pause:
  # This class is a base class
  """Gets a single character from standard input. Does not echo to the screen."""
  def __init__(self):
    if os.name == 'posix':
      self.impl = _PauseUnix()
    elif os.name == 'nt':
      self.impl = _PauseWindows()
    else:
      self.impl = _PauseUnix()

  def __call__(self, farg='', **kwargs):
    """
    farg is the response query string.
    kwargs is a dictionary that contains the list of valid responses allowed.
    This list is passed in this format:
    validResponses=[110, 78, 121, 89, 2, 27, 13]
    and is added into the keyword list as:
    {'validResponses': [110, 78, 121, 89, 2, 27, 13]}

    Usage:
    P("Hit the <Enter> key to continue.", validResponses=[13])
    """
    message = farg

    if kwargs.has_key('validResponses'):
      self.validResponses = kwargs['validResponses']
    else:
      self.validResponses = [13]
    if kwargs.has_key('echo'):
      echo = kwargs['echo']
    else:
      echo = 0

    def processResponse(message):

      if isinstance(message, NoneType) or len(message) == 0:
        message = "Do you want to continue? "
      ch = self.impl(message)
      rch = repr(ch)
      val = ord(ch)
      info = str(val) + "\n"
      key = rch
      if val == 13:
        key = 'Enter'
      if echo:
        print 'You hit the', key + ' key.'
        print "It's number code is =", val
        print 'validResponses =', self.validResponses
      #sys.stdout.write(rch)
      #sys.stdout.write(":")
      #sys.stdout.write(info)
      if val in self.validResponses:
        if val == 27:
          print "Escape Encountered!  Leaving Python."
          os.system('clear')
          raise SystemExit
          return val
        elif val == 110 or val == 78:
          # raise LoopExit
          # I want break to be returned to the calling loop
          return 2
        elif val == 2:
          print "Break Encountered!  Exiting loop."
          return 'break'
        elif val == 121 or val == 89 or val == 13:
          return 1
        else:
          print "\nInvalid response entered."
          print "Valid responses are: 'n', 'N' to break from a loop, 'x', 'X' to quit Python, and 'y', 'Y' or 'Enter' to continue."
          return 0
      else:
        if val != 13:
          if val == 27:
            #print "Escape Encountered!  Leaving Python."
            os.system('clear')
            raise SystemExit
            return val
          else:
            print
            sys.stdout.write('You hit the ' + key + ' key.')
            print "\nkeycode(" + str(val) + ")\nYou must use the <Enter> key.\n"
            return 0
        else:
          return 1

    retval = processResponse(message)
    try:
      while retval == 0:
        retval = processResponse(message)

    except(StandardError):
      #? use Default_Output
      error = "\nOutput error.  Message redirected to stdout. ", message
      print error[0]
      import traceback
      #tb = str(traceback.format_exc())
      print traceback.format_exc()
      sys.exc_clear()

    return retval


class _PauseUnix:
  def __init__(self):
    import tty #, sys

  #def __call__(self):
  def __call__(self, farg='', **kwargs):
    import tty, termios
    #sys.stdout.write("Do you want to continue? ")
    sys.stdout.write(farg)
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    sys.stdout.write("\n")
    return ch

class _PauseWindows:
  def __init__(self):
    import msvcrt

  #def __call__(self):
  def __call__(self, farg='', **kwargs):
    import msvcrt
    #sys.stdout.write("Do you want to continue? ")
    sys.stdout.write(farg)
    ch = msvcrt.getch()
    return ord(ch)

class ResponseError(Exception):
    def __init__(self, value):
      self.value = value
    def __str__(self):
      return repr(self.value)








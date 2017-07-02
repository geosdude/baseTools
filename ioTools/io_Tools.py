#!/bin/bash
# -*- codign:utf-8 -*-
# io_Tools.py
# Coded by Richard Polk, Jr
#
#----------------------------------------------------

print '  |' + __name__ + '| ---'

class Pied_Piper:
    """This class is a base class and only needs __builtin__"""
    def __init__(self, stdin='', **kwargs):
      methodName = 'Common_Tools.__init__'
      try:
        echo    = methDct[methodName][0]
        verbose = methDct[methodName][1]
        message = methDct[methodName][2]
        option  = methDct[methodName][3]
        kw      = methDct[methodName][4]
      except StandardError:
        isEchoKey(methodName)
        echo    = methDct[methodName][0]
        verbose = methDct[methodName][1]
        message = methDct[methodName][2]
        option  = methDct[methodName][3]
        kw      = methDct[methodName][4]
      if kwargs:
        kw.update(kwargs)
        methDct[methodName][4] = kw
      if echo:
        M(Sk(), offset=20)
      if kw.has_key('cmdLst'):
        for command in kw['cmdLst']:
          exec(command)
      print '  |Pied_Piper| --->'
      self.stdin = stdin

    def triple_Pipe(self, command, inStr=''):
        # pass string for stdin input or set instance var <curArgStr>.

        #(pipe, pipe, pipe) = popen3(cmdstring, mode ) The result of this function is
        #3 pipes - the processes stdin, stdout and stderr

        self.setTkVar('fg_colorVar', 'red')
        self.announce("Processing. Please wait!")

        self.blankLine()
        if 'win' in sys.platform:
          self.stdin, pipeout, pipeerr = win32pipe.popen3(command, 't')
        else:
        	self.stdin, pipeout, pipeerr = os.popen3(command, 't')
        print str(type(pipeerr)), pipeerr.read()
        print str(type(pipeout)), pipeout.read()
        self.setTkVar('fg_colorVar', 'darkgreen')
        self.announce("Finished.")

    def singlePipe(self, command=None):
        #print "Redirecting singlePipe to single_Pipe"
        self.single_Pipe(command)

    def single_Pipe(self, command=None):
        if not command:
          error = "Command Error: single_Pipe did not recieve a command"
          return error
        else:
          #self.messFGC.set("red")
          #if self.echoVar.get() > 0:
          #    self.announce("Processing. Please wait!")
          #output = win32pipe.popen(command)
          #if self.echoVar.get() > 0:
          #    print win32pipe.popen(command).read()
          if 'win' in sys.platform:
            outLst = win32pipe.popen(command).readlines()
          else:
          	outLst = os.popen(command).readlines()
          #self.setTkVar('bg_colorVar', 'darkgreen')
          #self.setTkVar('fg_colorVar', 'white')
          #self.announce("Finished.")
          return outLst

    def spawnProcess(self, argStr):
      os.spawnv(os.P_DETACH, os.environ['PYFILE'], ('python', argStr))


    # Demo of creating two processes using the CreateProcess API,
    # then waiting for the processes to terminate.


    # Create a process specified by commandLine, and
    # The process' window should be at position rect
    # Returns the handle to the new process.
    def spawnWin32Process(self, commandLine, ):
        # Create a STARTUPINFO object
        si = win32process.STARTUPINFO()
        # Set the position in the startup info.
        si.dwX, si.dwY, si.dwXSize, si.dwYSize = rect
        # And indicate which of the items are valid.
        si.dwFlags = win32process.STARTF_USEPOSITION | \
                     win32process.STARTF_USESIZE
        # Rest of startup info is default, so we leave it alone.
        # Create the process.
        info = win32process.CreateProcess(
                              None, # AppName
                              commandLine, # Command line
                              None, # Process Security
                              None, # ThreadSecurity
                              0, # Inherit Handles?
                              win32process.NORMAL_PRIORITY_CLASS,
                              None, # New environment
                              None, # Current directory
                              si) # startup info.
        # Return the handle to the process.
        # Recall info is a tuple of (hProcess, hThread, processId, threadId)
        return info[0]

    def stderrRedirect(self):
      self.s('guiState', 1)
      #self.stderr = sys.stderr
      sys.stderr = self

    def stderrRestore(self):
      #This is not working
      self.s('guiState', 0)
      #self = sys.stderr
      sys.stderr = sys.__stderr__ #self.stderr

    def stdoutRedirect(self):
      self.s('stdoutFlag', 'GUI')
      #self.stdout = sys.stdout
      sys.stdout = self

    def stdoutRestore(self):
      self.s('stdoutFlag', 'Shell')
      #self = sys.stdout
      sys.stdout = sys.__stdout__ #self.stdout

    def restoreIO(self, *args, **kwargs):
      """ """
      methodName = Mn(Sk())
      try:
        echo    = echoDct[methodName][0]
        verbose = echoDct[methodName][1]
        message = echoDct[methodName][2]
        option  = echoDct[methodName][3]
        kw      = echoDct[methodName][4]
      except StandardError:
        self.isEchoKey(methodName)
        echo    = echoDct[methodName][0]
        verbose = echoDct[methodName][1]
        message = echoDct[methodName][2]
        option  = echoDct[methodName][3]
        kw      = echoDct[methodName][4]
      if kwargs:
        kwargs['args'] = args
        kw.update(kwargs)
        echoDct[methodName][4] = kw
      if echo:
        M(Sk(), offset=20)
      if kw.has_key('cmdLst'):
        for command in kw['cmdLst']:
          exec(command)
      self.stderrRestore()
      self.stdoutRestore()

    def redirectIO(self, *args, **kwargs):
      """ """
      methodName = Mn(Sk())
      try:
        echo    = echoDct[methodName][0]
        verbose = echoDct[methodName][1]
        message = echoDct[methodName][2]
        option  = echoDct[methodName][3]
        kw      = echoDct[methodName][4]
      except StandardError:
        self.isEchoKey(methodName)
        echo    = echoDct[methodName][0]
        verbose = echoDct[methodName][1]
        message = echoDct[methodName][2]
        option  = echoDct[methodName][3]
        kw      = echoDct[methodName][4]
      if kwargs:
        kwargs['args'] = args
        kw.update(kwargs)
        echoDct[methodName][4] = kw
      if echo:
        M(Sk(), offset=20)
      if kw.has_key('cmdLst'):
        for command in kw['cmdLst']:
          exec(command)
      self.stderrRedirect()
      self.stdoutRedirect()

#print ' |commonTools| ---'
'''endfile'''
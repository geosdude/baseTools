#!/bin/bash
# -*- codign:utf-8 -*-
# baseTools.common.common_Tools
# Coded by Richard Polk, Jr
#
#----------------------------------------------------
#import sys
#print __file__ + '\n'
#print sys.argv
#raw_input("Hit return to continue.")

print '  |' + __name__ + '| ---'

impLst = ["from baseTools.commonTools.common_Vars import Common_Vars",
          "from baseTools.sysTools.term_Tools import _Pause",
          "from baseTools.sysTools.getch import _Getch",
          ]

for command in impLst:
  try:
    #print '  |' + __name__ + '|', command
    exec(command)
  except ImportError:
    print  "ImportError! Failure of --> " + command + " <-- detected!"
print '  |' + __name__ + '| ---'

class Common_Tools(Common_Vars, _Getch, _Pause):

    def __init__(self, **kwargs):
      """  """
      #! If these lines are present at the top of a function, metadata
      #  on the function gets populated in the method dictionary.
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
      Common_Vars.__init__(self)
      self.Getch = _Getch
      self.Pause = _Pause
      #print '  |Common_Tools| --->'
      print '  |'+ methodName + '| --->'

    def blankDef(self, **kwargs):
      methodName = Mn(Sk())
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
        M(Sk(), verbose=1, offset=16)
      if kw.has_key('preCmdLst'):
        for command in kw['preCmdLst']:
          exec(command)
      # Insert the code between the lines
      #----------------------------------


      #----------------------------------
      if kw.has_key('postCmdLst'):
        for command in kw['postCmdLst']:
          exec(command)

    def eventHandler(self, event, *args, **kwargs):
      """Redefine elsewhere for GUI event handling."""
      methodName = Mn(Sk())
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

    def _callHandler(self, farg=None, *args, **kwargs):
        """
        This method assembles a function call with it's arguments as a string, then
        executes it.
        """
        #! Set this up where farg and *args are for this method.  Use **kwargs for the
        #! called method.
        print ('farg ' + str(farg) + ' ' + str(type(farg))) + '\n' + \
        ('*args ' + str(args) + ' ' + str(type(args))) + '\n' + \
        ('**kwargs ' + str(kwargs) + ' ' + str(type(kwargs))).strip()      #this strips off self. and () from the function string.
        #function = farg[5:(len(farg) - 2)]
        #strip off the trailing parenthesis.
        function = farg[0:(len(farg) - 1)]
        #print ('function ' + str(function)).strip()

        #command = function + str(args[0]) + ', "' + str(args[1]) + '")'
        #command = "Kurry(" + str(farg) + ', ' + str(args) + ")"
        #command = function + str(args) + ')'
        #command = function + str(kwargs) + ')'
        command = "Kurry(" + str(farg) + ', ' + str(kwargs) + ")"
        print 'command = ' + str(command)
        print type(command)

        com = Kurry(farg, kwargs)

        print 'com', type(com)
        print dir(com)
        print 'com.fn', type(com.fn)
        print com.fn

    def callHandler(self, function, **kwargs):
      """  """
      methodName = Mn(Sk())
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

      # If the function is an event instance, redirect to the event handler.
      if isinstance(function, InstanceType):
        event = function
        function = 'self.handleEvent(event)'
      # Strip out 'self.' and '() from the passed in function string.
      self.function = function[5:(len(function) - 2)]
      try:
          exec(function)
          self.err_exception = 0
      except StandardError:
          error = 'Error in ' + str(function)
          print error
          import traceback
          print traceback.format_exc()
          sys.exc_clear()
          self.err_exception = 1

      return self.err_exception

    def increment(self, cntVar='', cnt=None):
      if isinstance(cnt, NoneType):
        command = "self.s('" + cntVar + "', self." + cntVar + " + 1)"
      else:
        command = "self.s('" + cntVar + "', " + str(cnt) + ")"
      #print command
      exec(command)

    def decrement(self, cntVar='', cnt=None):
      if isinstance(cnt, NoneType):
        command = "self.s('" + cntVar + "', self." + cntVar + " - 1)"
      else:
        command = "self.s('" + cntVar + "', " + str(cnt) + ")"
      #print command
      exec(command)

    def clearProcLst(self):
      #self.writeLine('Clearing ', self.procLstFile, '...')
      ##self.blankOutFile(self.procLstFile)
      #fileobject = self.fileOpen(self.procLstFile, 'w')
      #fileobject.write(' ')
      #fileobject.close()
      #self.procLst = []
      self.set('procLst', [])

    def printProcList(self):
      #self.writeLine('procLst has ', str(len(self.procLst)), ' items.')
      for item in self.procLst:
        self.writeLine(item)
      #self.writeLine('procLst has ', str(len(self.procLst)), ' items.')
      self.blankLine()

    def setProcList(self, inLst):
      self.procLst = inLst
      self.procLst.sort()
      # neet to write out values to self.procLstFile

    def disabled(self):
      self.blankLine()
      try:
        self.announce('This tool is currently off-line!', 'red', 'black')
      except StandardError:
        self.write('This tool is currently off-line!')
      self.blankLine()

    def nullFunction(self, **kwargs):   # moved from gui_Tools.Context_Menu class.
      """ """
      # Automatically derive the method name with a call to Mn() while passing it the
      # stack returned from Sk()
      #methodName = Mn(Sk())
      #? why did I hardcode the methodName?
      methodName = "nullFunction" #Mn(Sk())
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

      return 0

    def callBailOut(self, message):
      try:
        raise BailOut(message)
      except BailOut as e:
        print e.value

class BailOut(Exception):
    def __init__(self, value):
      self.value = value
      #self.value = self.methInfo(0, value)
    def __str__(self):
      return repr(self.value)

#! various notes and experimental code.  Clean this up

#classLst = [Kurry] #File_Tools, String_Tools, Map_Tools, Pied_Piper,
            #TEST_Tools, Sys_Tools, User_Tools, XML_Class, dBase_Tools]

#for Cls in classLst:
#  mixIn(Common_Tools, Cls)

#dbClassLst = [SQL_Tools, Run_SQL, SDO_Tools, SDE_Tools]

#for Cls in dbClassLst:
#  mixIn(DB_Tools, Cls)

# """ Consider this when defining classes. """

# type( name, bases, dict)

# Return a new type object. This is essentially a dynamic form of the class statement.
# The name string is the class name and becomes the __name__ attribute; the bases tuple itemizes the base
# classes and becomes the __bases__ attribute; and the dict dictionary is the namespace containing definitions
# for class body and becomes the __dict__ attribute. For example, the following two statements create identical
# type objects:

#  >>> class X(object):
#  ...     a = 1
#  ...
#  >>> X = type('X', (object,), dict(a=1))

#print '|baseTools| ---'
'''endfile'''
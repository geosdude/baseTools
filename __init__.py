#!/bin/bash
# -*- codign:utf-8 -*-
# baseTools.__init__.py
# Coded by Richard Polk
#
#-----------------------------------------------------
# list the baseTools tree like this..  tree -d /usr/lib/python2.7/dist-packages/baseTools
#import sys, os, time
#os.system('clear screen')
#sys.stderr.write("\x1b[31;01mLoading Basetools " + " "*10 + " \x1b[0m\r")
#sys.stderr.write("\x1b[18C")
#for i in range(10):
#   time.sleep(.05)
#   sys.stderr.write('\x1b[31;01m.')
#sys.stderr.write('\x1b[0m\n')
#import sys
#print __file__ + '\n'
#print sys.argv
#raw_input("Hit return to continue.")

impLst = ["import os",
          "__builtins__['os'] = os",
          "import sys",
          "from types import *",
          "import types",
          "__builtins__['StringType'] = types.StringType",
          "__builtins__['NoneType'] = types.NoneType",
          "__builtins__['InstanceType'] = types.InstanceType",
          "import platform",
          "import baseTools",
          "from baseTools.mixer import MixIn, UnMix",
          "__builtins__['MixIn'] = MixIn",
          "__builtins__['UnMix'] = UnMix",
          "from baseTools.pickleTools.pickle_Tools import *",
          "__builtins__['saveDbase']  = saveDbase",
          "__builtins__['saveState']  = saveState",
          "__builtins__['pickleJar']  = pickleJar",
          "__builtins__['loadDbase']  = loadDbase",
          "__builtins__['pickOpt']    = pickOpt",
          "from threading import Timer",
          "from time import sleep",
          "from threading import Timer",
          "from time import sleep",
          "import site",
          "if 'win' in sys.platform: import win32api",
          "if 'win' in sys.platform: import win32com.client",
          "if 'win' in sys.platform: import win32pipe",
          "if 'win' in sys.platform: from win32com.client import Dispatch",
          "if 'win' in sys.platform: from win32clipboard import *",
          "import StringIO",
          "import random",
          "rand = random.Random()",
          "import Queue",
          "import inspect",
          "from operator import *",
          "import csv",
          "import string",
          "import cStringIO",
          "import cgi",
          "import pdb",
          "import stat",
          "import math",
          "import uuid",
          "import urllib2",
          "import htmllib",
          "import sgmllib",
          "import time",
          "import datetime",
          "from time import localtime, strftime",
          "from baseTools.fileTools.findFile import search_file", #"from findFile import search_file",
          "from stat import *",
          "from tkSimpleDialog import *",
          "from tkFileDialog import *",
          "from modulefinder import ModuleFinder",
          "from array import array",
          "from string import upper",
          "from inspect import stack as Sk",         # importing stack as S trips over Tk"s south string reference as 'S' 's' Error given is: <TypeError: 'str' object is not callable.>
          "from inspect import getframeinfo as FI",
          "import cStringIO",
          "from baseTools.commonTools.kurry import Kurry",
          "from baseTools.commonTools.common_Tools import Common_Tools",
          "from baseTools.threadTools.thread_Tools import ThreadedClient",
          ]

for command in impLst:
  try:
    #print '|' + __name__ + '|', command
    exec(command)
  except ImportError:
    import traceback
    print  "ImportError! --> " + command + " <-- Failed!"
    print traceback.format_exc()
    raw_input("Hit <Enter> to continue.")

__builtins__['basePath']   = basePath = os.path.split(__file__)[0]
__builtins__['confPath']   = confPath = os.path.join(basePath, 'conf')

methPF   = os.path.join(confPath, 'methPF')
envPF    = os.path.join(confPath, 'envPF')
echoPF   = os.path.join(confPath, 'echoPF')
stPF     = os.path.join(confPath, 'stPF')
ioPF     = os.path.join(confPath, 'ioPF')
envbakPF = os.path.join(confPath, 'envbakPF')

__builtins__['methPF']   = methPF
__builtins__['echoPF']   = echoPF
__builtins__['envPF']    = envPF
__builtins__['stPF']     = stPF
__builtins__['ioPF']     = ioPF
__builtins__['envbakPF'] = envbakPF

y = MixIn()
mixIn = y.mixIn
del y
del MixIn

z = UnMix()
unMix = z.unMix
del z
del UnMix

sys.path.append(basePath)

#mixIn(echo_Tools, saveState) This only works on classes.
#print echo_Tools.checkEchoKey


# Test the environment page file by reading the first line.
try:
  with open(envPF , 'rU') as f:
    line1 = f.readline()
except IOError:
  with open(envPF , 'w+') as f:
    line1 = f.readline()
  f.close()

# get length of the first line in the pagefile.  If it is 0, no state is preserved and we have
# to build the environment dictionary from nothing.

if len(line1) == 0:
  envDct = {}
else:
  envDct = pickleJar(envPF)


#envDct['noneFilterLst'] = ['echoThis', 'bypass']
#envDct['basePath'] = basePath
#envDct['confPath'] = confPath
envDct['listPath'] = os.path.join(basePath, 'lst')
envDct['logPath']  = os.path.join(confPath, 'log')
envDct['stdErrF']  = os.path.join(os.path.join(confPath, 'log'), 'error.log')

# Once we write back to the pickle file, delete the objects out of memory.

# stDct - application state dictionary
try:
  with open(stPF, 'rU') as f:
    line1 = f.readline()
except IOError:
  with open(stPF, 'w+') as f:
    line1 = f.readline()
  f.close()

if len(line1) == 0:
  # if the pickle file gets wacked, set some defaults so the dictionary can have some keys.
  stDct = {'debug': 0, 'test': 0, 'guiState': 0, 'verbose': 0}
else:
  stDct = pickleJar(stPF)

__builtins__['stDct']   = stDct
__builtins__['verbose'] = stDct['verbose']
__builtins__['debug']   = stDct['debug']
__builtins__['test']    = stDct['test']

saveState(stPF)


# echoDct
print 'echoPF', echoPF
try:
  with open(echoPF , 'rU') as f:
    line1 = f.readline()
except IOError:
  with open(echoPF , 'w+') as f:
    line1 = f.readline()
  f.close()

if len(line1) == 0:
  echoDct = {}
else:
  echoDct = pickleJar(echoPF)

__builtins__['echoDct'] = echoDct
saveState(echoPF)

# methDct
#print 'methPF', methPF
try:
  with open(methPF , 'rU') as f:
    line1 = f.readline()
except IOError:
  with open(methPF , 'w+') as f:
    line1 = f.readline()
  f.close()

if len(line1) == 0:
  methDct = {}
else:
  methDct = pickleJar(methPF)

__builtins__['methDct'] = methDct
saveState(methPF)

def isEchoKey(keyName):
  """
    echo            = methDct[methodName][0]
    verbose         = methDct[methodName][1]
    message         = methDct[methodName][2]
    option or debug = methDct[methodName][3]
    keyword Dict    = methDct[methodName][4]
  """
  if not methDct.has_key(keyName):
    methDct[keyName]=[0, 0, '', 0, {}]
  elif len(methDct[keyName]) < 5:
    methDct[keyName].append({})
  saveState(methPF)
__builtins__['isEchoKey'] = isEchoKey


class Default_IO:
    """ Default_IO
    This class is intended to be utilized by methods that call both pre and post GUI output
methods of the same name. Using these default output methods will eliminate the necessity
of defining seperate output handlers for pre-GUI output. GUI sub-classes may redefine them
to redirect output to a text based widget. """
    def __init__(self):
      print '  |' + 'baseTools.Default_IO' + '| ---'

      #! print '         |' +  __class__ + '|'
      #super(Default_IO, self).__init__()
      #print "At Default_IO.__init__"
    #! Breaks here
    def output(self, *args): # code print statement into loop and remove return statement
        t_string = ''

        for arg in args:
            if not isinstance(arg, StringType):
                if isinstance(arg, IntType):
                    arg = str(arg)
                elif isinstance(arg, IntType):
                    arg = str(arg)
                elif isinstance(arg, FloatType):
                    arg = str(arg)
                elif isinstance(arg, TupleType):
                    for i in range(len(arg)):
                        t_string = t_string + str(arg[i])
                elif isinstance(arg, ListType):
                    for i in range(len(arg)):
                        t_string = t_string + str(arg[i])
                elif isinstance(arg, DictType):
                    for key, value in arg.iteritems():
                        t_string = t_string + key + ' ' + str(value) + '\n'
            else:
                t_string = t_string + arg
            #t_string = t_string + str(arg)
        return '\n' + t_string + '\n'

        #return str(args)

    def announce(self, *args):
      try:
        print self.output(args)
      except TypeError:
        pass

    def write_exception(self):
      print "Unexpected error:", sys.exc_info()[0]
      raise

    def write(self, *args):
      print self.output(args)
      #try:
      #  print self.output(args)
      #except Exception, e:
      #  print "Somethin went wrong: " + str(e)

    def writeLine(self, *args):
      print self.output(args)
      #try:
      #  print self.output(args)
      #except Exception, e:
      #  print "Somethin went wrong: " + str(e)

    def writeLines(self, *args):
      print self.output(args)

    def write_exception():
      print "Unexpected error:", sys.exc_info()[0]
      raise

    def blanklines(self, repeat=1, char=None, pad=0):
      """ redirected miss spelled method call to blankLine."""
      BL(repeat, char, pad)

    def blankLine(self, repeat=1, char=None, pad=0, lfeed=1):
      """
      Usage(repeat, character, padding, lfeed)
      BL(4, "*", 120, 2)
      """
      line = ''
      while repeat > 0:
        if char:
          line = line + (char * pad) + ("\n" * lfeed)
        else:
          line = line + ("\n" * lfeed)
        repeat = repeat - 1
      return line

    def setMode(self, text=''):
      print text

    def setExcludeLst(self, exLst=[]):
      print exLst

    def read(self):
      pass

    def clearText(self):
      pass

class Counter:
    def __init__(self):
      self.valState = 0

    def up(self, num=0):
      self.valState = num + 1
      return self.valState

    def down(self, num=0):
      self.valState = num - 1
      return self.valState

class RepeatedTimer(object):
    """
Credit:
github.com/MestreLion

Usage:

from time import sleep

def hello(name):
    print 'Hello %s!' % name

print 'starting...'
rt = RepeatedTimer(1, hello, 'World') # it auto-starts, no need of rt.start()
try:
    sleep(5) # your long-running job goes here...
finally:
    rt.stop() # better in a try/finally block to make sure the program ends!

Features:

Standard library only, no external dependencies.

start() and stop() are safe to call multiple times even if the timer has already
started/stopped.
function to be called can have positional and named arguments.

You can change interval anytime, it will be effective after next run.
Same for args, kwargs and even function!
    """
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False



class IO_Class:
    """
      Build io file objects.
    """
    def __init__(self):
      print '  |' + 'baseTools.IO_Class' + '| ---'
    def stdErr(self):
      return open(stdErrF, 'rU')
      #return StringIO.StringIO()
    def stdIn(self):
      return StringIO.StringIO()
    def stdOut(self):
      return StringIO.StringIO()

#? This should be at the bottom of the class tree so
# other classes can inherit persistant variables.
# The problem is that some variables are defined using
# tools from classes higher up in the inheritance tree.
# This will have to be solved.  20 May 2013
class Env_Vars(Common_Tools):
    """ Base class to handle instance variables."""
    def __init__(self, debug=0, verbose=0, guiState=None, **kwargs):
      """ """
      methodName = 'Env_Vars.__init__'
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
      Common_Tools.__init__(self)
      #envPF    = os.path.join(os.path.join(os.environ['HOME'], 'conf'), 'envPF')
      #envBakPF = os.path.join(os.path.join(os.environ['HOME'], 'conf'), 'envPF.bak')
      # Stock abbreviations
      #stkPF    = os.path.join(os.path.join(os.environ['HOME'], 'lst'), 'stkAbbrPF')
      #Get gui state vars  #! get from gDct
      # Dont add verNo to envDct.  Set it at runtime.
      try:
        self.verNo    = sys.version.split()[0]
        self.verStr   = sys.version.split()[0].replace('.', '') # Python version number as string
      except StandardError:
        self.verNo = '2.6.5'
        self.verStr = '265'
      # build the path from scratch using the approiate os pathsep character.
      #! This stDct object creation is redundant.  It has been built already in base_Tools and should
      #! be inserted into the gDct or __builtins__

      self._break   = 0

      #P(L(Sk()) + 'filename = ' + str(filename) + ".  File Presence = " + str(self.checkFileObject(filename)))
      #tmpDct = self.pickleJar(filename, 'init_Env Line 72')
      #envDct = self.loadOtherVars(self.pickleJar(filename))
      #P(L(Sk()) + 'tmpDct =' + str(type(tmpDct)))
      #loadedVarsDct = self.loadOtherVars(tmpDct)
      #P(L(Sk()) + 'loadedVarsDct =' + str(type(loadedVarsDct)))
      #envDct = loadedVarsDct
      #P(L(Sk()) + 'envDct =' + str(type(self.envDct)))
      self.loadOtherVars()
      self.expandVars(envDct)
      #print '  |Env_Vars| --->'
      print '  |'+ methodName + '| --->'

    def loadOtherVars(self): #! redundant also in env_Vars
      members = inspect.getmembers(self)
      #print members, type(members), str(len(members))
      #tmpDct = {}
      for item in members:
        #print item[0], type(item[0])
        if isinstance(item[1], MethodType):
          pass
        elif isinstance(item[1], DictType):
          #print "Its a dictionary"
          envDct[item[0]] = item[1]
          #print item[0],':',
          #print item[1]
          #print
        elif isinstance(item[1], ListType):
          #print "Its a list"
          envDct[item[0]] = item[1]
          #print item[0],':',
          #print item[1]
          #print
        elif isinstance(item[1], StringType):
          #print "Its a string"
          envDct[str(item[0])] = item[1]
          #print item[0],':',
          #print item[1]
          #print
        elif isinstance(item[1], IntType):
          #print "Its a number"
          envDct[item[0]] = item[1]
          #print item[0],':',
          #print item[1]
          #print
        elif isinstance(item[1], TupleType):
          #print "Its a tuple"
          envDct[item[0]] = item[1]
          #print item[0],':',
          #print item[1]
          #print
      #! tempDct is redundant.  We write directly to the input Dictionary.
      #for k,v in tmpDct.iteritems():
      #  print 'k', k, type(k)
      #  print 'v', v, type(v)
      #  try:
      #    k = str(k)
      #    inDct[k] = v
      #  except TypeError:
      #    print "Exception fly-by!"
      #return inDct

    def expandVar(self, key, value):
      func_str = \
"""
def expandVariable(self, value):
  self.""" + key + """ = value
  if envDct['verbose'] == 1:
    self.write('From expandVariable ... setting Key self.""" + key + """ ', 'to ', str(value))
"""
      exec(func_str)
      f = locals()["expandVariable"]
      f(self, value)

    def formatString(self, max1, max2=0, inStr='', inVal='', tailStr='*'):

      tx = len(tailStr)
      ty = 30
      tz = 0
      x = len(str(inStr))
      y = 0
      z = 0

      while z <= max1:
        y = y + 1
        z = x + y
      else:
        a = len(str(inVal))
        b = 0
        c = 0
        while c <= max2:
          b = b + 1
          c = a + b

      if tailStr == '*':
        tailStr = str(type(inVal))
      else:
        tailLst = list(tailStr)
        #print 'tailStr', tailStr
        #print 'tx', tx
        #print
        while ty <= tx:
          #print 'ty', ty
          #print '-------------------------------------------'
          cnt   = 0
          tz    = ty
          cntLst = [cnt]
          s = tailLst[ty].isalnum()
          while s and tz < tx:
            # test one index up and down.  Insert the newline on the closest false.
            #print 's', s
            #print 'cntLst', cntLst
            #print '--------------'
            for i in cntLst:
              #print 'i', i
              tz = ty + i
              #print 'tz ', tz
              #print 'tx ', tx
              if tz >= tx:
                #print '--------------\n'
                break
              else:
                #print 'tailLst[tz]', tailLst[tz]
                s = tailLst[tz].isalnum()
            #print '--------------\n'
            cnt = cnt + 1
            cntLst = [neg(cnt), cnt]
          else:
            # if it is not a number or character, insert the newline else.
            pass
            #print 'Inserting a newline.\n'


          tailLst.insert(tz, ('\n' + " ".rjust(z+c+max1-1)))
          ty = ty + 30

        tailStr = ''.join(tailLst)
        #print 'tailStr', tailStr

      outStr = inStr + " ".rjust(y) + '= ' + inVal + " ".rjust(b-1) + '= ' + tailStr.strip()
      return outStr

    def expandVars(self, inDct):

      max0 = self.maxLen(inDct.keys())
      max1 = max0 + 5
      max2 = max0 + 9

      for k,v in inDct.iteritems():
        if isinstance(k, StringType):
          if k[-3:] != 'Var':
            prefix = "self." + k
            suffix = "inDct['" + k + "']"
            tail = str(inDct[k])
            command = prefix + " = " + suffix
            #command = "self." + k + " = inDct['" + k + "']"
            if stDct['verbose'] == 1:
              try:
              #self.formatString(max1, max2, prefix, suffix, tail)
                print "Executing this command: ", self.formatString(max1, max2, prefix, suffix, tail)
              except StandardError:
                print "Error"
                print "self.traceBack", sys.exc_info()[2]
                import traceback
                print traceback.print_exc()
            try:
              exec(command)
            except StandardError:
              print 'init_Env.py: BOINK Encountered!!!!!!'
              print 'Error setting ' + str(k) + ' to ' + str(v)
              print "self.traceBack", sys.exc_info()[2]
              import traceback
              print traceback.print_exc()
              #Kurry(command)

    def checkType(self, key, value):
      try:
        if key == 'bypass':
          return (key, int(value))
      except StandardError:
        pass

    def noneFilter(self, key, value):
      if key in self.noneFilterLst and value == None:
        print "Variable named <echoThis> can't be NoneType.  Setting it as a zero length string instead."
        if value == None:
          value == ''
      return (key, value)


    def setVar1(self, inDct, key, value):
      #! Need to pass in the dictionary in which the k,v pair is being set.
      #Need to add type checks based on variable suffix: i.e. procLst, envDct ect ... .
      #locals()["virtualFunction"](self)
                                 #  echoThis can't be NoneType.
            #? fold this into checkType
      prefix = inDct[:-3]
      PF = prefix + 'PF'
      inDct[key] = value
      #inDct = eval('self.' + str(inDct)) # the dictionary is in builtins now.
      inDct = eval('self.' + str(inDct))
      saveDbase(PF, inDct)


    def setVar2(self, **kwargs):
      #! Need to pass in the dictionary in which the k,v pair is being set.
      argDct = kwargs.copy()
      keyLst = argDct.keys()
      if len(keyLst) == 0:
        pass
      else:
        for k,v in argDct.iteritems():
          self.write('key = ', k, 'value = ', v)
          #self.setVar(k, v)

    def setVar(self, key, value):
      #! Need to pass in the dictionary in which the k,v pair is being set.
      #Need to add type checks based on variable suffix: i.e. procLst, envDct ect ... .
      #locals()["virtualFunction"](self)
      #  echoThis can't be NoneType.
            #? fold this into checkType

      if isinstance(value, StringType):
        key, value = self.noneFilter(key, value)
      if key == 'bypass':
        key, value = self.checkType(key, value)
      if key in stDct.keys():
        stDct[key] = value
      envDct[key] = value
      self.expandVar(key, value)
      saveState(envPF)

    def set(self, key, value):
      self.setVar(key, value)

    def s(self, key, value):
      self.setVar(key, value)

    def verifyVar(self, key, value):
      self.disabled()

    def getVar(self, dct, key):
      #value = dct.get(key, None)
      #print value
      return dct.get(key, None)

    def clearVar(self, key):
      envDct[key] = None
      self.expandVar(key, None)
      saveState(envPF)

    def removeVar(self, key):
      del envDct[key]
      saveState(envPF)

class Env_Tools(Env_Vars):
    """ Derived class """
    def __init__(self, **kwargs):
      """ """
      methodName = 'Env_Tools.__init__'
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
      #print '  |' + 'baseTools.Env_Tools' + '| ---'
      #
      Env_Vars.__init__(self)
      #print '  |Env_Tools| --->'
      print '  |'+ methodName + '| --->'

      #super(Env_Tools, self).__init__()  returns this: TypeError: must be type, not classobj
      #? What's the difference??
      #super(Env_Tools, self).__init__()
      #Env_Vars.__init__(self)
    def define(self, envFile, pass2envDct=0):  # Superceeded # Env dict is first created by instantiation of Env_Vars class above.
      #self.envFile = envFile  # Intended to be ran after Env_Vars to set changes.  After-the-fact redefinition of env dict.
      #self.lastDir = ''       # Need to modify to handle any type of environment dictionary from any conf file
      argLst = []
      #print '\nRunning env_Tools.Env_Class.define()\n'
      loopCnt = 0
      file = open(envFile, 'rU')
      for line in file.readlines():
          argLst.append(line.strip())
      file.close()
      tmpDct = self.defineDict(argLst)   # from Map_Class
      argLst = []
      for k, v in  tmpDct.iteritems():
        value = None
        if v.isdigit():
          value = int(v)
          command = 'self.' + k + ' = ' + str(value)
        else:
          value = str(v)
          command = 'self.' + k + ' = ' + "'" + str(value) + "'"

        if pass2envDct:
          if verbose:
            print 'Passing values to the Environment Dictionary.'
            print 'Creating instance variable.'
          envDct[k] = value # populate values into master environment dictionary if flag is true.
          exec(command) #create instance variable 'self.'

      return tmpDct # return

    def writeEnvironment(self):
      saveState(envPF)

    def setDriveLetter(self):

      self.write("Configuring PyLister path variables to use ", self.homeDrive, " as the root path.")
      keyLst = envDct.keys()
      keyLst.sort()
      for key in keyLst:
        #value = self.conCat("\n", inD
        value = str(envDct[key])
        key = str(key)
        if 'Path' in key or 'File' in key:
          self.write("Old path definition: ", key, ' ', value)
          tmpStr = os.path.splitdrive(value)[1]
          newValue = self.setSlash("F", os.path.join(self.homeDrive, value))
          self.write("New path definition: ", key, ' ', newValue)
          envDct[key] = newValue
          self.blankLine()

    def echoConfigDct(self, inDct, call=None):
      """echoConfigDct.  Returns formatted output to print.
Input requires a dictionary.
Args are: inDct, call=None
Return yeilds 1 output format as a concatenated (key, value, newline) string."""

      if isinstance(call, NoneType):
        pass
      else:
        self.announce('Called from ', call, "\n")  # code call to report module and line number.

      output  = ''  # Print key then value as a string on the next line followed by a blank line.

      keyLst = inDct.keys()  # What a no-brainer!  Returns sorted dictionary keys from a list instead of dict.iteritems() for k,v loop
                             # which returns unsorted keys.  You can use the sorted() method.
      keyLst.sort()
      for key in keyLst:
        #value = self.conCat("\n", inDct[key]) This writes blank lines to conf files which breaks them.
        value = inDct[key]
        output = output + key + '\n' + str(value) + '\n'

      return output

    def getKeyValue(self, key):
      if envDct.has_key(key):
        #print envDct.get(key), type(self.envDct.get(key))
        return  envDct.get(key)
      else:
        return None

    def maxLen(self, inLst=[]): # This one works on lists only.  String_Tools has one that will handle tups, dicts, lists, and strings.
      """Gets the maximum length of items in a list.
      Usage: BT.maxLen(inLst)
      inLst must be of type(list)"""
      procLst = []
      maxLen     = 0
      if len(inLst) == 0:
        procLst = self.curLst
      else:
        procLst = inLst
      for x in procLst:
        if isinstance(x, IntType):
          x = str(x)
        tmp = len(x)
        if tmp > maxLen:
          maxLen = tmp
      maxLen = maxLen + 1
      return maxLen

    def reloadMod(self, modName):
      reload(modName)

class _Getch:
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
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

class _GetchWindows:
  def __init__(self):
    import msvcrt

  def __call__(self):
    import msvcrt
    return msvcrt.getch()

class Stops_Class:   #my own pause class instance
    """
    Stops_Class
    A class that provides a pause method based on raw_input.
    """
    def __init__(self, debug=0, verbose=0, guiState=None):
      #! These aren't getting inherited.
      #! Need to use os.environ[STATE_FILE] for cross platform compatability.
      #! Naaa.  We would have to set too many system environment vars.  We can use
      #! one environment var for the root of the path.
      #! stDct needs to be inserted into __builtins__ or gDct to avoid redundancy
      self.inkey = _Getch()
      print '  |' + 'baseTools.Stops_Class' + '| ---'

      try:
        self.debug    = stDct['debug']
      except KeyError:
        stDct['debug'] = 0
        saveState(stPF)

      try:
        self.verbose  = stDct['verbose']
      except KeyError:
        stDct['verbose'] = 0
        saveState(stPF)

      try:
        self.guiState = stDct['guiState']
      except KeyError:
        stDct['guiState'] = 0
        saveState(stPF)

      self._break   = 0

      # Echo back some stuff for debug or verification
      #self.blankLine = BL #envDct ['blankLine'] = Default_IO().blankLine
      #envDct ['write'] = Default_IO().write
      #print self.blankLine
      #print self.blankLine(1, '+', 120)
      #print

    #def s(self, **kwargs):
    #  # Maybe Roll this into stop1
    #  try:
    #    response = raw_input(message)
    #    if len(kwargs.keys()) > 0:
    #      for k, v in kwargs.iteritems():
    #        command = 'self.' + k + ' = ' + str(v)
    #        exec(command)
    #  except(StandardError):
    #    print "Unexpected error:", sys.exc_info()[0]

    def lineNBR(self, stack):
      """
      Return the method's line number.
      Params = stack()[0] from inspect.stack()
      """
      return "Line: " + str(stack[0][2]) + "\n"

    def lineNBR2(self, stack):
      """
      Return the method's line number.
      Params = stack()[0] from inspect.stack()
      """
      return str(stack[0][2])

#!  Killer Function!!
#?  Need to write this to a log file.  logPF.
    def modInfo(self, stack, inStr=None, *args, **kwargs):
      """
From base_Tools.py Stops_Class.modInfo
Saved as M in __builtins__
Passed in args are: modInfo(stack, inStr, *args, **kwargs)

Usage examples:
print M(Sk(), 'This Method is Obsolete!')
Returns the calling and called module/line/method and the calling line of code!

Example output returned from an obsolete method which is still referenced in code but has been slated
for deprication:

  deff concatWRT(self, rtChar='', *args):  # this is an obsolete method replaced by self.conCat(args)
    M(Sk(), ': This method has been deprecated!  Use conCat instead!')
    return self.conCat(*args)

The call to concatWRT returns this and then passes its args to the new method conCat:

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-Caller-
Module : /home/user/lib/dbase/cxOraTools/cxOra_Vars.py
Method : cxOra_Vars.__init__
Line   : 36

-Called-
Module : /home/user/lib/stringTools/string_Tools.py
Method : string_Tools.Concat
Line   : 400

-Alert!!!
This method has been deprecated.  Use conCat instead.
------------------------------------------------------------------------------------------------------------------------


It is handy when you don't know from where you have called the depreciated method.

Params:
 stack()[0] - from inspect.stack()
 inStr      - pass in a message to be returned when the method is called.

      """
      if 'offset' in kwargs.keys():
        offset = int(kwargs['offset'])
      else:
        offset = 0
      if 'verbose' in kwargs.keys():
        verbose = 1
      else:
        verbose = 0
      #! Make inStr dynamic by setting it's value to be taken from the envDct
      #! which can be changed from the GUI's command line.

      stack = list(stack)
      length = len(stack)
      L = length - 1
      stkSpan = range(length)
      stkDct = {}

      for i in stkSpan:

        stkDct[i] = {}
        stack[i] = list(stack[i])
        stkDct[i]['stack']   = stack[i][1:length]
        stkDct[i]['cldPath'] = stack[i][1]
        stkDct[i]['cldMod']  = os.path.splitext(os.path.split(stack[i][1])[1])[0]
        stkDct[i]['cldLine'] = stack[i][2] - offset
        stkDct[i]['cldMthd'] = str(stkDct[i]['cldMod']) + '.' + str(stack[i][3])
        try:
          stkDct[i]['cldCode'] = str(stack[i][4][0]).strip()
        except:
          stkDct[i]['cldCode'] = ''
        stkDct[i]['clrPath'] = ''
        stkDct[i]['clrMod']  = ''
        stkDct[i]['clrMthd'] = ''
        stkDct[i]['clrLine'] = ''

      for i in stkSpan:
        if i == L:
          stkDct[i]['clrPath'] = stkDct[i]['cldPath']
          stkDct[i]['cldMthd'] = stkDct[i - 1]['cldMthd']
          stkDct[i]['clrMthd'] = str(stack[i][3])
        else:
          stkDct[i]['clrPath'] = stkDct[i + 1]['cldPath']
          stkDct[i]['clrMod']  = stkDct[i + 1]['cldMod']
          stkDct[i]['clrMthd'] = stkDct[i + 1]['cldMthd']
          stkDct[i]['clrLine'] = stkDct[i + 1]['cldLine']


      inLoop = ''
      if verbose:
        stkMess = ''
        for i in stkSpan:
          k = str(i)
          stkMess = stkMess + '\n' + str(BL(1, '=', 120)).strip()          +\
          "\n" + k                                                         +\
          '\n-Caller- '     + inLoop                                       +\
          "\nstkDct["+k+"]['clrPath']:" + ' ' + str(stkDct[i]['clrPath'])  +\
          "\nstkDct["+k+"]['clrMthd']:" + ' ' + str(stkDct[i]['clrMthd'])  +\
          "\nstkDct["+k+"]['clrLine']:" + ' ' + str(stkDct[i]['clrLine'])  +\
          '\n\n-Called- '                                                  +\
          "\nstkDct["+k+"]['cldPath']:" + ' ' + str(stkDct[i]['cldPath'])  +\
          "\nstkDct["+k+"]['cldMthd']:" + ' ' + str(stkDct[i]['cldMthd'])  +\
          "\nstkDct["+k+"]['cldLine']:" + ' ' + str(stkDct[i]['cldLine'])  +\
          "\nstkDct["+k+"]['cldCode']:" + ' ' + str(stkDct[i]['cldCode'])  +\
          '\n' + str(BL(1, '+', 120))
          #"stkDct["+str(i)+"]['clrMod'] " + ' ' + str(stkDct[i]['clrMod'])  +\
        print stkMess + '\n'
      if isinstance(inStr, NoneType):
        message = str(BL(1, '+', 120)).strip()            +\
          '\n-Caller- '     + inLoop                      +\
            '\nModule : '   + str(stkDct[0]['clrPath'])   +\
            '\nMethod : '   + str(stkDct[0]['clrMthd'])   +\
            '\nLine   : '   + str(stkDct[0]['clrLine'])   +\
          '\n\n-Called- '                                 +\
            '\nModule : '   + str(stkDct[0]['cldPath'])   +\
            '\nMethod : '   + str(stkDct[0]['cldMthd'])   +\
            '\nLine   : '   + str(stkDct[0]['cldLine'])   +\
            '\n' + str(BL(1, '-', 120)).strip()
            #'\nCode   : '   + str(stkDct[0]['cldCode'])   +\
      else:
        message = str(BL(1, '+', 120)).strip()            +\
          '\n-Caller- '     + inLoop                      +\
            '\nModule : '   + str(stkDct[0]['clrPath'])   +\
            '\nMethod : '   + str(stkDct[0]['clrMthd'])   +\
            '\nLine   : '   + str(stkDct[0]['clrLine'])   +\
          '\n\n-Called- '                                 +\
            '\nModule : '   + str(stkDct[0]['cldPath'])   +\
            '\nMethod : '   + str(stkDct[0]['cldMthd'])   +\
            '\nLine   : '   + str(stkDct[0]['cldLine'])   +\
          '\n\n-Alert!!!  '                               +\
            '\n'+ inStr                                   +\
            '\n' + str(BL(1, '-', 120)).strip()
      print message

    def getMethodName(self, stack):
      """
      Returns the called method or function name.
      Params = Sk() from inspect import stack as Sk
      """
      return stack[0][3]

    def stackInfo(self, stack):
      """
      Return stack info
      Params = Sk()[0] from inspect import stack as Sk
      """
      message = ''
      for item in stack:
        for i, v in enumerate(item):
          message = message + str(i) + ' ' + str(v) + ' ' + '\n'
        message = message + '\n'
      print message

    def this_fails(self):
      x = 1/0

    def failError(self):
      try:
        self.this_fails()
      except StandardError as detail:
        print 'Handling run-time error:', detail

    def error(self, methodName=None, command=None, exeInfo=None):
      import traceback
      if isinstance(command, NoneType):
        pass
      else:
        print "Error in executing command: ", command
      if isinstance(methodName, NoneType):
        pass #print "Error TraceBack:", exeInfo[2]
      else:
        print methodName + " Error TraceBack:", exeInfo
      #print traceback.print_exc()
      print traceback.format_exc()
      #sys.exc_clear()
      #self.stop()

    def errStop(self):
      import traceback
      tbk = str(traceback.format_exc())
      #print traceback.format_exc()
      sys.exc_clear()
      response = raw_input(tbk)

    def stop(self, farg='', **kwargs):
      """ Superceeded by .baseTools.sysTools.term_Tools._Pause
      builtin pause function:
      Usage P('some message', condition=27)
      condition is returned if it isn't NoneType
      If the user pressed the escape key, 27 is returned by default and can be used as a conditional statement
      to bypass loops or method calls.
      The condition keyword arg is for controlling the return value of the method and is intended.
      """
      if farg == None:
        farg = '  '
      if 'verbose' in kwargs.keys():
        verbose = kwargs['verbose']
      else:
        verbose = 0

      if 'condition' in kwargs.keys():
        condition = kwargs['condition']
      else:
        condition = None

      message = ''
      retval = 0
      def processResponse():
        if self.guiState:
          message = '\n' + str(farg) + "\nDo you want to continue? "
        else:
          message = str(farg) + "\nDo you want to continue? "
        try:
          response = raw_input(message) #Pause program and wait for user input.
        except (EOFError):
          response = "Y"
        #response = raw_input(message) #Pause program and wait for user input.
        _response = response
        messLen = len(response)
        if messLen == 0:
          response = "Y"
          messLen = 1

        if messLen == 1:
          condition = ord(response)
          print "ord value", condition
          if condition == 27:
            print "Escape sequence encountered."
            return condition
          response = string.upper(response)

          if response == "N":
            # raise LoopExit
            # I want break to be returned to the calling loop
            return 2
          elif response == "X":
            print "SystemExit Encountered!  Leaving Python."
            os.system('clear')
            raise SystemExit
          elif response == "Y":
            return 1
          else:
            print "\nInvalid response '" + str(_response) + "' entered."
            print "Valid responses are: 'n' to break from a loop, 'x' to quit Python, and 'y' or 'Enter' to continue."
            return 0
        else:
          print "\nInvalid response '" + str(response) + "' entered."
          print "Valid responses are: 'n' to break from a loop, 'x' to quit Python, and 'y' or 'Enter' to continue."
          #response = raw_input(message)
          return 0

      retval = processResponse()
      print retval
      try:
        while retval == 0:
          retval = processResponse()

      except(StandardError):
        #? use Default_Output
        error = "\nOutput error.  Message redirected to stdout. ", message
        print error[0]
        import traceback
        #tb = str(traceback.format_exc())
        print traceback.format_exc()
        sys.exc_clear()

      return condition

        #return retval

class write_Globals:
  """Write input dictionary keys and values to the globals namespace."""
  print '  |' + 'baseTools.write_Globals' + '| ---'
  def translate_Vars(self, inDct={}):
    globals()[str(inDct)] = inDct
    for k, v in inDct.iteritems():
      globals()[str(k)] = v


# ==============================================================================
# Begin echo functionality


#def em(meth=None):
#  #! obsolete.  replaced with echo.
#  """
#  Set the method or function to echo some basic information about itslef.
#  args: method name.
#  """
#  if not isinstance(meth, NoneType):
#    methDct[meth]=1
#
#def xem(meth=None):
#  #! obsolete.  replaced with echo.
#  """Turn em off."""
#  if methDct.haskey(meth):
#    del methDct[meth]

class Echo_Tools:
    '''This class is a base class'''
    def __init__(self):
      self.isEchoKey = isEchoKey
      self.isEchoKey('modInfo')
      print '  |' + 'Echo_Tools' + '| ---'


    def silence(self, object):
      """Individually hide a passed in name from verbose mode"""
      if not methDct['silentDct'].has_key(object):
        # set a default of 1
        methDct['silentDct'][object] = 1
      elif methDct['silentDct'].has_key(object) and methDct['silentDct'][object] == 1:
        methDct['silentDct'][object] = 0
      elif methDct['silentDct'].has_key(object) and methDct['silentDct'][object] == 0:
        methDct['silentDct'][object] = 1
      else:
        methDct['silentDct'][object] = 0

    def silent(self, object):
      if not methDct['silentDct'].has_key(object):
        # set a default of 0
        methDct['silentDct'][object] = 0
      return methDct['silentDct'][object]

    #def keyword(self, methodName, key=None, val=None):
    # Experimental
    #  """Toggles option mode for a passed in method name"""
    #  if not methDct.has_key(methodName):
    #    methDct[methodName]=[0, 0, '', 0, {}]
    #  elif methDct.has_key(methodName) and methDct[methodName][4] >= mode:
    #    methDct[methodName][3] = 0
    #  elif methDct.has_key(methodName) and methDct[methodName][3] == 0:
    #    methDct[methodName][3] = mode
    #  else:
    #    methDct[methodName][3] = 0
    #  saveState(emethPF)
    #  self.eeMeth(methodName)
    #  return methDct[methodName]

    def option(self, methodName, mode=0):
      """Sets option mode to a specific value for a passed in method name"""
      mode = int(mode)
      if not methDct.has_key(methodName):
        methDct[methodName]=[0, 0, '', mode, {}]
      else:
        methDct[methodName][3] = mode
      saveState(methPF)
      self.eeMeth(methodName)
      return methDct[methodName]

    def toggleOption(self, methodName, mode=1):
      """Toggles option mode for a passed in method name"""
      mode = int(mode)
      if not methDct.has_key(methodName):
        methDct[methodName]=[0, 0, '', mode, {}]
      elif methDct.has_key(methodName) and methDct[methodName][3] >= mode:
        methDct[methodName][3] = 0
      elif methDct.has_key(methodName) and methDct[methodName][3] == 0:
        methDct[methodName][3] = mode
      else:
        methDct[methodName][3] = 0
      saveState(methPF)
      self.eeMeth(methodName)
      return methDct[methodName]

    def message(self, methodName, message=''):
      """
      Toggles or sets a message for a passed in method name.
      Defaults to a zero length string.
      """
      if not methDct.has_key(methodName):
        methDct[methodName]=[0, 0, message, 0, {}]
      else:
        if methDct[methodName][3]:
          methDct[methodName][2] = methDct[methodName][2] + ' ' + message
        else:
          methDct[methodName][2] = message
      saveState(methPF)
      self.eeMeth(methodName)
      return methDct[methodName]

    def verbo(self, methodName, mode=1):
      """
      Toggles verbose mode for a passed in method name
      Usage:  verbo someMethod
      """
      mode = int(mode)
      if not methDct.has_key(methodName):
        methDct[methodName]=[0, mode, '', 0, {}]
      elif methDct.has_key(methodName) and methDct[methodName][1] >= mode:
        methDct[methodName][1] = 0
      elif methDct.has_key(methodName) and methDct[methodName][1] == 0:
        methDct[methodName][1] = mode
      else:
        methDct[methodName][1] = 0
      saveState(methPF)
      self.eeMeth(methodName)
      return methDct[methodName]

    def echoOn(self):
      __builtins__['verbose'] = stDct['verbose'] = 1
      saveState(stPF)
      print "Echo mode on."

    def echoOff(self):
      __builtins__['verbose'] = stDct['verbose'] = 0
      saveState(stPF)
      print "Echo mode off."

    def debugOn(self):
      __builtins__['debug'] = stDct['debug'] = 1
      saveState(stPF)
      print "Debug mode on."

    def debugOff(self):
      __builtins__['debug'] = stDct['debug'] = 0
      saveState(stPF)
      print "Debug mode off."

    def testOn(self):
      __builtins__['test'] = stDct['test'] = 1
      saveState(stPF)
      print "Test mode on."

    def testOff(self):
      __builtins__['test'] = stDct['test'] = 0
      saveState(stPF)
      print "Test mode off."

    def echo(self, methodName):
      """
      Toggles echo mode for a passed in method name.
      Usage:  echo someMethod
      """
      if not methDct.has_key(methodName):
        methDct[methodName]=[1, 0, '', 0, {}]
      elif methDct.has_key(methodName) and methDct[methodName][0] == 1:
        methDct[methodName][0] = 0
      elif methDct.has_key(methodName) and methDct[methodName][0] == 0:
        methDct[methodName][0] = 1
      else:
        methDct[methodName][0] = 0
      saveState(methPF)
      self.eeMeth(methodName)
      return methDct[methodName]

    def egDict(self):
      __builtins__['clearText']()
      print self.echoDict(guiDct)[3]

    def eeMeth(self, methodName):
      __builtins__['clearText']()
      message = methodName + '\n'
      for x in range(len(methDct[methodName])):
        if x == 0:
          message = message + "  echo:    " + str(methDct[methodName][0]) + "\n"
        if x == 1:
          message = message + "  verbose: " + str(methDct[methodName][1]) + "\n"
        if x == 2:
          message = message + "  message: " + str(methDct[methodName][2]) + "\n"
        if x == 3:
          message = message + "  option:  " + str(methDct[methodName][3]) + "\n"
        if x == 4:
          if len(methDct[methodName][4].keys()) == 0:
            message = message + "  kwds:    " + str(methDct[methodName][4]) + "\n"
          else:
            # this one is borked and freezes up the package.
            #message = message + "  kwds:    " + self.echo_Dict(methDct[methodName][4], sort=1, option=3, pad=1) + "\n"
            message = message + "  kwds:    \n" + str(self.echoDict(methDct[methodName][4], subpad=4, sort=1)[3]) + "\n"
            #message = 'Damn it! That hurt.'
      print message
      # Echo some stuff for verification
      #print methodName + " = " + str(methDct[methodName])
      # print self.echo_Dict(methDct['modePoll'][4], sort=1, option=3, pad=1)

    def eeDict(self, eDct=None, clrTxt=1):
      """
Echo a dictionary's keys and values in a nice format.
Args passed are: <the dictionary to echo>, <clear off previous text, 1=yes, 0=no>
The defaults are to echo the global echo dictionary (eDct) and clear off the previous text.
Instance Usage: self.eeDict(myDict, 0)
Global Usage:   ed(myDict, 0)
CmdLn Usage: ed myDict 0
      """
      if clrTxt:
        __builtins__['clearText']()
      if isinstance(eDct, NoneType):
        eDct = methDct
      print self.echoDict(eDct, sort=1)[3]

    def esDict(self, clrTxt=0):
      """
Echo the silent dictionary keys and values in a nice format.
Args passed are: <clear off previous text, 1=yes, 0=no>
This method echos methDct['silenceDct'] and defaults to keep previous text.
Instance Usage: self.esDict(1) or self.esDict()
Global Usage:   es(1) or es()
CmdLn Usage: es 0
      """
      if clrTxt:
        __builtins__['clearText']()
      #if isinstance(esDct, NoneType):
      if 'silenceDct' in methDct:
        esDct = methDct['silenceDct']
      else:
        esDct = None
      print self.echoDict(esDct, sort=1)[3]

    def sortList(self, inLst=[]):
      sortLst = []
      tmpLst  = []
      sortDct = {}

      for x in inLst:
        if isinstance(x, IntType):
          sortDct[x] = x
        else:
          sortDct[string.lower(x)] = x
      tmpLst = sortDct.keys()
      tmpLst.sort()
      for i in tmpLst:
        sortLst.append(sortDct[i])
      return sortLst

    def getMaxLen(self, intake, inMax=0):
        if inMax > 0:
          inMax = inMax - 1
        maxLen = inMax
        if isinstance(intake, DictType):
          for key in intake.keys():
            if isinstance(key, IntType):
              temp = len(str(key))
            else:
              temp = len(key)
            if temp > maxLen:
              maxLen = temp
        else:
          for item in intake:
            temp = len(str(item))
            if temp > maxLen:
              maxLen = temp
        maxLen = maxLen + 1
        #self.maxLen = maxLen
        return maxLen

    def echoMap(self, intake, pad=0, inMax=0, sort=1, call=None):
      output = ''
      if isinstance(call, NoneType):
        pass
      else:
        self.write('Called from', call)

      if isinstance(intake, DictType):
        output = self.echoDict(intake)[3]
      elif isinstance(intake, ListType):
        output = self.echoLst(intake, pad, inMax, sort)
      elif isinstance(intake, TupleType):
        output = self.echoTup(intake, pad, inMax, sort)

      return output

    def echoTup(self, intake, pad=0, inMax=0, sort=1, call=None):  # need to code typetool class

      padding = ' ' * pad

      tmp = ''
      output = ''
      if inMax == 0:
        maxLen = self.getMaxLen(argTup)
        if maxLen == 0:
          maxLen = 5
      for item in argTup:
        tmp = tmp.strip() + padding  + str(item)
      output = output + tmp
      tmp = ''
      return output

    def echoList(self, inLst, *args, **kwargs):
      """ """
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
        M(Sk(), verbose=1, offset=20)

      if 'pad' in kwargs.keys():
        pad = int(kwargs['pad'])
      else:
        pad = 1

      if "maxLen" in kwargs.keys():
        maxLen = kwargs["maxLen"]
      else:
        maxLen = self.getMaxLen(inLst)  # Pass in previous maxLen var <lenMax> for length carry over from previous call.

      if "sort" in kwargs.keys():
        inLst = self.sortList(inLst)

      if "sepChar" in kwargs.keys():
        sepChar = kwargs["sepChar"]
      else:
        sepChar = '= '

      padding = ' ' * pad

      tmp = ''
      tmp2 = ''
      output = ''
      cnt = 1
      for item in inLst:
        if isinstance(item, TupleType):
          l = len(item)
          item = tmp2
        if cnt == 1:
          tmp = tmp.strip()  + padding  + str(item) + '\n'
        else:
          tmp = tmp + padding  + str(item) + '\n'
        cnt = cnt + 1
      tmp = tmp + '\n'
      output = output + tmp + '\n'
      tmp = ''

      return output

    def echoLst(self, argLst, pad=1, inMax=0, sort=1, call=None):
      M(Sk(), 'This method has been deprecated.  Use echoList instead.')
      if isinstance(call, NoneType):
        pass
      else:
        print 'Called from', call

      padding = ' ' * pad

      tmp = ''
      tmp2 = ''
      output = ''
      maxLen = self.getMaxLen(argLst)
      cnt = 1
      for item in argLst:
        if isinstance(item, TupleType):
          l = len(item)
          # debug verify output
          #for x in range(len(item)):
            #print item[x]
            #if not isinstance(item[x], StringType):
            #  tmp2 = tmp2 + str(item[x]) + padding + '/n'
            #else:
            #  tmp2 = tmp2 + item[x] + padding + '/n'
          item = tmp2
        if cnt == 1:
          tmp = tmp.strip()  + padding  + str(item) + '\n'
        else:
          tmp = tmp + padding  + str(item) + '\n'
        cnt = cnt + 1
      tmp = tmp + '\n'
      output = output + tmp + '\n'
      tmp = ''

      return output

    def padding(self, inTxt):
      spacer = ' ' * (self.maxLen - len(inTxt))
      return spacer

    def echoDictVals(self, inDct, val):
      self.announce(inDct[val])
      return inDct[val]

    def echo_Dict(self, inDct, *args, **kwargs):
      """
      This one is freezing the app for some reason when option 3 is set.
      """
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
        M(Sk(), verbose=1, offset=20)
        ed(kw)

      for k in kw.keys():
        if not k in ["option", "spacer", "pad", "subpad", "sort"]:
          del kw[k]

      if "option" in kw.keys():
        option = int(kw["option"])
      else:
        option = 3

      if "spacer" in kw.keys():
        spacer = kw["spacer"]
      else:
        spacer = ""

      if "pad" in kw.keys():
        pad = int(kw["pad"])
      else:
        pad = 1

      if "sort" in kw.keys():
        keyLst = self.sortList(inDct.keys())
      else:
        keyLst = inDct.keys()

      #! max_Len is getting set in a preserved state object.
      maxLen = self.getMaxLen(inDct, 0)  # Pass in previous maxLen var <lenMax> for length carry over from previous call.

      if "sepChar" in kw.keys():
        sepChar = kw["sepChar"]
      else:
        sepChar = "= "
      outStr = ""
      padding = pad * spacer
      tmp     = ""
      outPut  = ""
      message = str(kw)

      # em ct_Scroll
      for key in keyLst:
        value  = inDct[key]
        if isinstance(key, IntType):
          key = str(key)
        factor = (maxLen - int(len(key)))
        #print 'factor', factor
        spacing = spacer * factor
        #print 'len spacing', len(spacing)
        outStr = padding + key + spacing
        #print 'len outStr', len(outStr)
        if option == 0:
          #(String):     Print key then value on the next line followed by a blank line.
          outPut = outPut + key + "\n" + str(value) + "\n"
        elif option == 1:
          #(String):     Print key then value.
          outPut = outPut + key + str(value)
        elif option == 2:
          #(String):     Print key, spacer, =, padding, value
          outPut = outPut + key + spacing + padding + str(type(value)) + " = " + str(value) + "\n"
        elif option == 3:
          if spacer == "":
            spacer = " "
            spacing = spacer * factor
          outPut = outPut + key + sepChar + spacing + str(value) + "\n"
          #outPut = outPut + str(value) + '\n'
          #'borked'
          #(Dict, List):  Print key, spacer, padding, sep char, value
          #if isinstance(value, DictType):
            #outPut = outPut + self.echoDict(value, sort=1)[3] + padding + sepChar
          #elif isinstance(value, ListType):
            #outPut = outPut + self.echoList(value, sort=1) + padding + sepChar
        elif option == 4:
          # Print key, spacer, padding, sep char, value
          outPut = outPut + padding + key + spacing + sepChar + str(value) + "\n"
        elif option == 5:
          #(String):     value, ','
          outPut = outPut + str(value) + ","
        elif option == 6:
          outPut = outPut + key + ","
        elif option == 7:
          outPut = outPut + key  + ";'" + str(value) + "'\n"
        elif option == 8:
          outPut = outPut + key  + "= " + str(value) + "<BR>"
        elif option == 9:
          outPut = outPut + (key.strip() + """ """ + "= '" + str(value)).strip() + "\n"
        elif option == 10:
          outPut.append((key.strip() + " = " + str(value)).strip())
        elif option == 11:
          outPut.append((key.strip() + spacer + padding + "= " + str(value)).strip())
        elif option == 12:
          outPut.append((key.strip() + spacer + padding + """  """ + str(value)).strip())

      return outPut

    def echoDict(self, inDct, **kwargs):
      print "This method is obsolete.  Use echo_Dict instead."

def testEcho(methodName=None):
  if isinstance(methodName, NoneType):
    methodName=Mn(Sk())
  if methDct.has_key(methodName):
    if methDct[methodName]:
      M(Sk())
  else:
    methDct[methodName] = 0
    saveState(methPF)


# Experimental class not implimented yet.
#class Tool_Box:
#  io = IO_Class()                  # Create IO_Class instance
#  stdin  = io.stdIn                # build IO file like objects
#  stdout = io.stdOut
#  stderr = io.stdErr
#  del io                           # drop IO_Class instance
#
#  x = Stops_Class()                # Create an instance of Stops_Class.
#
#  P = x.stop1                      # redefine Stops_Class.stop1 as P.  Call it as:
#                                   # P()
#                                   # or:
#                                   # P('Jump up and down while patting your head to continue')
#  M   = x.modInfo                  # This returns formatted info from the trace stack.
#  Mn  = x.getMethodName
#  Err = x.error
#  Ers = x.errStop
#  Fe  = x.failError
#
#  T = x.stackInfo                  # This returns the entire trace stack.
#  L = x.lineNBR                    # This return a modules line number from the calling line.  Params = stack()[0]
#  Ln = x.lineNBR2                  # This return a modules line number as an integer
#
#  BL = x.blankLine                 # A blank line or seperator tool
#
#  del x

# Experimental instantiation not implimented yet.
#DB_Tools.__init__(self)

class Base_Tools(Env_Tools, Default_IO):

  """ Derived class """
  def __init__(self, **kwargs):
    """ """
    methodName = 'Base_Tools.__init__'
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
    #? Vain attempts whose code is left upon which to ponder why it is still here.
    #?Echo_Tools.__init__(self)
    #?__builtins__['Echo_Tools'] = Echo_Tools()
    Env_Tools.__init__(self)
    print '  |Base_Tools| ---'

#-----------------------------------------------------
# Set runtime variables and objects


IO     = IO_Class()              # Create IO_Class instance
stdin  = IO.stdIn                # build IO file like objects
stdout = IO.stdOut
stderr = IO.stdErr
del IO                           # drop IO_Class instance

wgbls = write_Globals()          # Write gDct to globals
Gbls = wgbls.translate_Vars

w  = Default_IO()
BL = w.blankLine                # A blank line or seperator tool
clearText = w.clearText
write = w.write
del w

x = Stops_Class()                # Create an instance of Stops_Class.

Stop = x.stop                       # redefine Stops_Class.stop1 as P.  Call it as:
                                 # P()
                                 # or:
                                 # P('Jump up and down while patting your head to continue')
M   = x.modInfo                  # This returns formatted info from the trace stack.
Mn  = x.getMethodName
Err = x.error
Ers = x.errStop
Fe  = x.failError

T = x.stackInfo                  # This returns the entire trace stack.
L = x.lineNBR                    # This return a modules line number from the calling line.  Params = stack()[0]
Ln = x.lineNBR2                  # This return a modules line number as an integer
del x

e  = Echo_Tools()
echoDict = e.echo_Dict #echoDict is a method.  echoDct is a dictionary
ed = e.eeDict          # A tool to list the methods set in the methDct to echo themselves at runtime.
es = e.esDict
em = e.eeMeth
sortList = e.sortList
echoOn = e.echoOn
echoOff = e.echoOff
debugOn = e.debugOn
debugOff = e.debugOff
testOn = e.testOn
testOff = e.testOff
echo  = e.echo
verbo = e.verbo
opti = e.option
mess = e.message
silence = e.silence
del e

# Modify the __builtins__ dict.
#! Put some of these in the envDct  to avoid corrupting __builtins__
#__builtins__['Gbls']      = Gbls rethink this

__builtins__['string']     = string
__builtins__['types']      = types
__builtins__['sys']        = sys
__builtins__['Stop']       = Stop
__builtins__['BL']         = BL
__builtins__['Sk']         = Sk
__builtins__['M']          = M
__builtins__['Mn']         = Mn
__builtins__['Fe']         = Fe
__builtins__['Err']        = Err
__builtins__['Ers']        = Ers
__builtins__['Queue']      = Queue
__builtins__['clearText']  = clearText
__builtins__['Default_IO'] = Default_IO
__builtins__['echo']       = echo
__builtins__['echoDict']   = echoDict
__builtins__['verbo']      = verbo
__builtins__['echoOn']     = echoOn
__builtins__['echoOff']    = echoOff
__builtins__['debugOn']    = debugOn
__builtins__['debugOff']   = debugOff
__builtins__['testOff']    = testOff
__builtins__['testOn']     = testOn
__builtins__['opti']       = opti
__builtins__['mess']       = mess
__builtins__['em']         = em
__builtins__['silence']    = silence
#__builtins__['em']        = em
#__builtins__['xem']       = xem
__builtins__['ed']         = ed
__builtins__['es']         = es

envDct['stdin']            = globals()['stdin']
envDct['stdout']           = globals()['stdout']
envDct['stderr']           = globals()['stderr']

#! Write envDct to a picke file to establish a persistant state.

__builtins__['envDct'] = envDct
envDct['envPF'] = envPF
saveState(envPF)

#? Why not use typesLst = dir(types)
#typesLst = [name for name in dir(types) if not name.startswith('__')]

typeLst = ['BooleanType', 'BufferType', 'BuiltinFunctionType', 'BuiltinMethodType', 'ClassType',
           'CodeType', 'ComplexType', 'DictProxyType', 'DictType', 'DictionaryType', 'EllipsisType',
           'FileType', 'FloatType', 'FrameType', 'FunctionType', 'GeneratorType',
           'GetSetDescriptorType', 'InstanceType', 'IntType', 'LambdaType', 'ListType',
           'LongType', 'MemberDescriptorType', 'MethodType', 'ModuleType', 'NoneType',
           'NotImplementedType', 'ObjectType', 'SliceType', 'StringType', 'StringTypes',
           'TracebackType', 'TupleType', 'TypeType', 'UnboundMethodType', 'UnicodeType',
           'XRangeType']

# Upper case is a class.  lower case is a method

__builtins__['bt'] = baseTools
__builtins__['BT'] = Base_Tools()
__builtins__['CT'] = Common_Tools()
__builtins__['ET'] = Env_Tools()
#__builtins__['TC'] = ThreadedClient #2012 this gets instanciated elsewhere ... 2017 Why
__builtins__['TC'] = ThreadedClient()
__builtins__['P'] = BT.Pause()
__builtins__['G'] = BT.Getch()
#__builtins__['HM'] = BT.HookManager()

#perform an experimental instantiation of the class
#Base_Tools()

'''
When a line of code asks for the value of a variable x, Python will search for that variable in all the available namespaces, in order:

1. local namespace - specific to the current function or class method. If the function defines a local variable x, or has an argument x, Python will use this and stop searching.
2. global namespace - specific to the current module. If the module has defined a variable, function, or class called x, Python will use that and stop searching.
3. built-in namespace - global to all modules. As a last resort, Python will assume that x is the name of built-in function or variable.
'''

'''endfile'''
# pass some args
1, "*", 120, 2

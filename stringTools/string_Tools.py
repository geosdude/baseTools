#!/bin/bash
# -*- codign:utf-8 -*-
# baseTools.string_Tools.string_Tools.py
# Coded by Richard Polk
#----------------------------------------------------

impLst = ['import rfc822', 'from types import *']

for command in impLst:
  try:
    #print '          |' + __name__ + '|', command
    exec(command)
  except ImportError:
    print  "ImportError! Failure of --> " + command + " <-- detected!"
print '  |' + __name__ + '| ---'

class String_Tools:
    '''This class is a base class'''
    def __init__(self, **kwargs):
      """ """
      methodName = 'String_Tools.__init__'
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
      print '          |String_Tools| ---'
      #! Add some bound methods to this module's global table.
      # They are created after the fact in base_Tools before String_Tools gets instantiated.
      self.curLst     = []
      self.charDct    = {}
      for x in range(33, 126):
        self.charDct[x] = chr(x)

    def docStringer(self, inStr = ''):
      # Obsolete
      outStr = '"""\n' + inStr.strip() + '\n"""'
      return outStr

    def quoteStr(self, inStr='', qt=0):
      """
      Return a string with various styles of quotes.
      Usage self.quoteStr( inStr, qt )
      where inStr = input string to be quoted and qt is a flag to chose
      the quote type.
      qt 0 = No quotes
      qt 1 = Single quotes
      qt 2 = Double quotes
      qt 3 = Back quote
      qt 4 = Triple single quotes
      qt 5 = Triple double quotes
      """
      #print 'farg', farg
      inStr = rfc822.unquote(inStr)
      #print 'inStr before', inStr
      if qt == 0:
        return inStr
      elif qt == 1:
        inStr = repr(inStr)
      elif qt == 2:
        inStr = '"' + inStr + '"'
      elif qt == 3:
        inStr = '`' + inStr + '`'
      elif qt == 4:
        inStr = "'''" + inStr + "'''"
      elif qt == 5:
        inStr = '"""' + inStr + '"""'

      #debug code.
      #print 'inStr after', inStr
      return inStr

    def deQuote(self, inStr):
      inStr = (inStr.replace("'", "")).replace('"', '')
      return inStr

    def deSpace(self, inStr):
      inStr = inStr.replace(" ", "")
      return inStr

    def formatLst(self, list):
        return (' ' + string.join(list, ',\n'))

    def splitPth(self, pathstring):
        pathlist = string.split(pathstring, os.pathsep)
        return self.formatLst(pathlist)

    def wrapString(self, inStr):
        inArray = array('c', inStr)
        cnt = 0
        for x in range(len(inArray)):
          x = x * 1.0000
          mod = x % 125.0000    # I am assuming a text object size of 125 characters.  Write code for variable text object resizing.
          quotent = x / 125.0000

          if x > 124:
            if mod == 0.0:
              #print 'x', x, 'mod', mod, 'quotent', quotent
              i = int(x)
              try:
                while inArray[i] != ';':
                  i = i - 1
                inArray.insert((i + 1), '\n')
              except IndexError:
                pass
        return inArray.tostring()

    def setWinClip(self, text): # copy to Windows clipboard.
        OpenClipboard()
        EmptyClipboard()
        SetClipboardText(text)
        CloseClipboard()

    def getWinClip(self):  # copy from windows clipboard.
        text = ''
        OpenClipboard()
        text = GetClipboardData()
        CloseClipboard()
        return text

    def strComp(self, str1='', str2=''):
        return cmp(str1, str2)

    def compare(self, str1, str2):
        """
           Usage: Pass in two strings to compare and get 1 or 0 as a returned result.
           results = self.compare('str1', 'str2')
           0 is False - they do not match
           1 is True - they match
        """
        # this form first makes sure that negative 1 isn't returned.
        # secondly, it reverses the values so that it matches what one would expect from binary results
        # with zero as false and one as true
        return abs(abs(cmp(str(str1), str(str2))) - 1)

    def maxLen(self, inLst=[]): # This one works on lists only.  code *args to process tups, dicts, lists, strings like cat methods below.
        procLst = []
        maxLen     = 0
        if len(inLst) == 0:
          procLst = self.curLst
        else:
          procLst = inLst
        for x in procLst:
            tmp = len(x)
            if tmp > maxLen:
                maxLen = tmp
        maxLen = maxLen + 1
        return maxLen

    def setMaxX(self, inStr='', maxX=0): # This one works on strings only. Replace with modified method above --- once it is actually modified.
        temp = len(inStr)                # Either or.  Return the greatest value.
        if temp > maxX:
            maxX = temp
            return maxX
        else:
            return temp

    def convStr2Lst(self, inStr):
        repLst = ["(", ")", "'", "[", "]", ","]   # create function to handle string conversion to list.
        tmpStr = inStr
        for item in repLst:
            if item in tmpStr:
                tmpStr = tmpStr.replace(item, "")
        tmpLst = tmpStr.split()
        return (tmpLst, tmpStr)

    def reverseLst(self, inLst):
        outLst = []
        for item in inLst:
          outLst.insert(0, item.strip())
        return outLst

    def padStrings(self):
        self.disabled()

    def sortText(self, inStr):
        tmpLst = []
        tmpStr = ''
        #self.writeLine(inStr)
        if len(inStr) > 0:
            tmpLst = inStr.split('\n')
            tmpLst.sort()
            for item in tmpLst:
                tmpStr = self.concatWSP(tmpStr, item, '\n')
        #self.writeLine(tmpStr)
        return tmpStr

    def charCount(self, inStr):
        charDct = {}
        for char in inStr:
          charDct[char] = charDct.get(char, 0) + 1
        print charDct


    def getCnt(self, counter=0):
        self.cnt.set(self.cnt.get() + counter)
        return self.cnt.get()

    #def getMaxLen(self, inDct):     #! Moved to map_Tools.Map_Class.  Maybe use **kwargs instead of inDct
    #    maxLen = 0
    #    for key in inDct.keys():
    #        temp = len(key)
    #        if temp > maxLen:
    #            maxLen = temp
    #    maxLen = maxLen + 1
    #    return maxLen

    def setString(self):
        inStr = self.askString('Set a string.', 'Enter a substring value.')
        return inStr

    def askString(self, tool, query, initial=None):
        inStr = askstring(tool, query, initialvalue=initial)
        return inStr

    def setSlash(self, option='F', inStr=''):
        #Filter out unicode types.
        if not isinstance(inStr, StringType):
          inStr = str(inStr)

        if option == 'B':
            if '/' in inStr:
               inStr = inStr.replace('/', os.sep)
        elif option == 'F':
            if os.sep in inStr:
                inStr = inStr.replace(os.sep, '/')
        return inStr

    def concatWRT(self, rtChar='', *args):  # this is an obsolete method replaced by self.conCat(args)
        M(Sk(), ': This method has been deprecated!  Use conCat instead!')
        return self.conCat(*args)
        # old code slated to be axed
        #args = list(args)
        #t_string = ''
        #
        #for x in range(len(args)):
        #
        #    if not isinstance(args[x], ):
        #        if isinstance(args[x], IntType):
        #            args[x] = str(args[x])
        #        elif isinstance(args[x], IntType):
        #            args[x] = str(args[x])
        #        elif isinstance(args[x], TupleType):
        #            for i in range(len(args[x])):
        #                t_string = t_string + str(args[x][i])
        #        elif isinstance(args[x], ListType):
        #            for i in range(len(args[x])):
        #                t_string = t_string + str(args[x][i])
        #        elif isinstance(args[x], DictType):
        #            for key, value in args[x].iteritems():
        #                t_string = t_string + key + ' ' + str(value) + '\n'
        #    else: # replace the passed in flagged character with a '\n' return character
        #        if args[x] == rtChar:
        #            args[x] = '\n'
        #        elif args[x] == '':
        #            args[x] = 'null' # if it is null, speak the truth.
        #        t_string = t_string + args[x]
        #
        #return t_string

    def addWhiteSpaces(self, *args):
        t_lst = []
        for arg in args:
          arg = arg + ' '
          t_lst.append(arg)
        return tuple(t_lst)

    def conCatWSP(self, *args):
        #M(Sk(), 'This method has been deprecated.  Use conCat instead.')
        return self.conCat(self.addWhiteSpaces(*args))

    def concatNSP(self, *args):
        #M(Sk(), 'This method has been deprecated.  Use conCat instead.')
        return self.conCat(*args)

    def conCat(self, *args, **kwargs):
      """
      kwargs are: qt=0, sp='', where:
      qt is a flag indicating the type of quote to use and
      sp is a spacer character.
      verbose overrides self.verbose
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
        kwargs['args'] = args
        kw.update(kwargs)
      if echo:
        M(Sk(), offset=26)
      if kw.has_key('cmdLst'):
        for command in kw['cmdLst']:
          exec(command)

      # set up a default kwargs dictionary
      if not 'qt' in kwargs.keys():
        kwargs['qt'] = 0
      if not 'sp' in kwargs.keys():
        kwargs['sp'] = ""
      kw.update(kwargs)
      methDct[methodName][4] = kw

      if verbose:
        #'args: ' + str(args)
        'kwargs: ' + str(kwargs)
        for key in kwargs:
          print "Keyword arg %s=%s" % (key, kwargs[key])

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
              t_string = t_string + key + str(kwargs['sp']) + str(value) + '\n'
        else:
          t_string = t_string + str(kwargs['sp']) + arg
      #P(L(S()[0]) + self.quoteStr(int(kwargs['qt']), rfc822.quote(t_string)))
      return (self.quoteStr(rfc822.quote(t_string), int(kwargs['qt']))).strip()

    def formatString(self, cnt, maxX, maxX2=0, inStr='', inVal=''):
      x = len(str(inStr))
      y = 0
      z = 0
      while z <= maxX:
          y = y + 1
          z = x + y
      if len(str(inVal)) < 1:
          if cnt > 9:
              op = '='
          else:
              op = ' ='
          #print 'Arg', cnt, op, inStr, " ".rjust(y), type(inStr)
      else:
          a = len(str(inVal))
          b = 0
          c = 0
          while c <= maxX2:
              b = b + 1
              c = a + b
          outStr = self.conCat(inStr, " ".rjust(y), '=', inVal, " ".rjust(b), type(inVal))
          return outStr

    def formatNumberedString(self, number, inStr):
      """Starts with a base of five spaces."""
      sn = 5
      spacer = ' ' * (sn - len(number))
      outStr = self.concatNSP(number, spacer, inStr)
      return outStr

    def getModulo(self, inVal):
      if inVal % 2:
        return 1
      else:
        return 0

    def getCntInterval(self, inVal):
      interval = inVal / 50
      return getModulo(interval)

    def cvsString(self, *args):
      t_string = ''
      for arg in args:
        if not isinstance(arg, StringType):
          if isinstance(arg, IntType):
            arg = str(arg)
          elif isinstance(arg, IntType):
            arg = str(arg)
          elif isinstance(arg, TupleType):
            for i in range(len(arg)):
              t_string = t_string + str(arg[i]) + ','
          elif isinstance(arg, ListType):
            for i in range(len(arg)):
              t_string = t_string + str(arg[i]) + ','
          elif isinstance(arg, DictType):
            for key, value in arg.iteritems():
              t_string = t_string + key + ',' + str(value) + '\n'
        else:
            t_string = t_string + arg
      return t_string

# This gets done from Base_Tools now.
#__builtins__['st'] = String_Tools()

'''endfile'''
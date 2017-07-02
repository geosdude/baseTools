#!/bin/bash
# -*- codign:utf-8 -*-
# baseTools.file_Tools.file_Tools
# Coded by Richard Polk
#----------------------------------------------------

impLst = ["from tkSimpleDialog import *",
          "from tkFileDialog import *",
          "from tkMessageBox import *",
          "from baseTools.stringTools.string_Tools import String_Tools",
          ]

for command in impLst:
  try:
    #print '        |' + __name__ + '|', command
    exec(command)
  except ImportError:
    print  "ImportError! Failure of --> " + command + " <-- detected!"
print '  |' + __name__ + '| ---'


class File_Tools(String_Tools):

    def __init__(self, **kwargs):
      """  """
      methodName = 'File_Tools.__init__'
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
      String_Tools.__init__(self)
      print '        |File_Tools| ---'
      self.maxfileload    = 100000
      self.blksize        = 1024 * 8

    def filter_files(name, function):        # filter file through function
      input  = open(name, 'rU')              # create file objects
      output = open(name + '.out', 'wU')     # explicit output file too
      for line in input.readlines():
          output.write(function(line))       # write the modified line
      input.close()
      output.close()                         # output has a '.out' suffix

    def askFileName(self, inStr="Select a file.", ftype="lst"):
      file_Types = []
      fStr = ''
      if '.' in ftype:
        pass
      else:
        ftype = '.' + ftype
      fStr = string.upper(ftype.strip('.')) + ' files'
      file_Types.append((fStr, string.upper(ftype)))
      fStr = string.lower(ftype.strip('.')) + ' files'
      file_Types.append((fStr, string.lower(ftype)))
      file_Types.append(('All files', '*'))
      filename = askopenfilename(title=inStr, initialfile=self.lastFile, initialdir=self.lastDir, filetypes=file_Types)
      self.setPathHistory(os.path.dirname(filename))
      return filename

    def checkFileObject(self, filename='', **kwargs):
      methodName = Mn(Sk())
      isEchoKey(methodName)
      echo    = methDct[methodName][0]
      verbose = methDct[methodName][1]
      message = methDct[methodName][2]
      try:
        flashEcho = int(kwargs['flashEcho'])
      except:
        flashEcho = 0
      if flashEcho:
        M(Sk(), offset=11)
      if echo and not flashEcho:
        M(Sk(), offset=13)
      # this had better be executed with the 'r' option else it will blank out
      # the tested file.
      fileobject = self.fileOpen(filename, 'rU')
      flag = isinstance(fileobject, FileType)
      if flag:
        fileobject.close()
        if verbose:
          # if it is sucessfull, just open it. Be quit otherwise.
          self.write("File Existance Status:  --Success-- <", flag, ">")
      else:
        self.write("File Existance Status:  --Failure-- <", flag, ">")
      return flag

    def fileCreate(self, filename):
      self.blankOutFile(filename)

    def fileOpen(self, filename, mode='rU'):
      if mode == 'rU':
        if os.path.isfile(filename):
          try:
            fileObject = open(filename, mode)
            return fileObject
          except IOError:
            pass
      elif mode == 'w':
          try:
            fileObject = open(filename, mode)
            return fileObject
          except IOError:
            pass

    def getFileAsString(self, filename='', caption="Select a file.", ext="py"):
      if len(filename) == 0:
        filename = self.askFileName(caption, ext)

      fileObject = self.fileOpen(filename)
      if debug == 1:
        BL()
        message = self.concat('getFileAsString- fileObject = ', str(fileObject))

      if not isinstance(fileObject, NoneType):
        # read method returns fileobject as a string.
        stringObject = fileObject.read()
        fileObject.close()
        if debug == 1:
          BL()
          message = self.concat('getFileAsString- ', str(fileObject), stringObject)
        return stringObject
      else:
        self.write("File read error:  NoneType encountered or user canceled the operation. ")

    def getFileAsList(self, filename='', caption="Select a list file.", ext="lst", **kwargs):
      '''Read a file and return it as a list.

      Returns a tuple of list and filename.
      If the filename is not passed in as an arg, it is asked for and returned to the caller
      as a convienence.
      '''
      methodName = Mn(Sk())
      isEchoKey(methodName)
      echo    = methDct[methodName][0]
      verbose = methDct[methodName][1]
      message = methDct[methodName][2]
      try:
        flashEcho = kwargs['flashEcho']
      except:
        flashEcho = 0
      if flashEcho:
        M(Sk(), offset=17)
      if echo and not flashEcho:
        M(Sk(), offset=19)

      if len(filename) == 0:
        filename = self.askFileName(caption, ext)

      fileObject = self.fileOpen(filename)
      if debug == 1:
        BL()
        message = self.concat('getFileAsList- fileObject = ', str(fileObject))

      if not isinstance(fileObject, NoneType):
        # readlines method returns fileobject as list
        #! breaks on large files.  Need to use readline and
        # process a line at a time.
        listObject = fileObject.readlines()
        fileObject.close()
        if debug == 1:
          BL()
          message = self.concat('getFileAsList- ', str(fileObject), '\n\n', listObject)
        procLst = []
        cnt = 0
        for item in listObject: #Process out nulls or the remark character.
          if item[0].isspace() or item[0] == "#":
            pass
          else:
            procLst.insert(cnt, item.strip())
            cnt = cnt + 1 # insert in order of call
        return procLst, str(filename)

      else:
        self.write("File read error:  NoneType encountered. ")  #Returns this error.  AttributeError: Base_Tools instance has no attribute 'write'
        #print "File read error:  NoneType encountered. "


    def writeDct2File(self, filename):
      fileobject = self.fileOpen(filename, 'w')

    def blankOutFile(self, filename):
      fileobject = self.fileOpen(filename, 'w')
      fileobject.write('')
      fileobject.close()

    def fileWriteList(self, filename, inLst, mode='w'):         # writeToFile redirect
      methodName = Mn(Sk())
      isEchoKey(methodName)
      echo    = methDct[methodName][0]
      verbose = methDct[methodName][1]
      message = methDct[methodName][2]
      if echo:
        M(Sk(), offset=7)
      file = self.fileOpen(filename, mode)
      for line in inLst:
          text = line + '\n'
          file.write(text)
      file.close()

    def writeConfigFile(self, filename, text, mode='w'):
      methodName = Mn(Sk())
      isEchoKey(methodName)
      echo    = methDct[methodName][0]
      verbose = methDct[methodName][1]
      message = methDct[methodName][2]
      if echo:
        M(Sk(), offset=7)
      filename = os.path.join(envDct['confPath'], filename)
      self.writeToFile(filename, text, 'w')

    def writeToFile(self, filename, text, mode='w', runCnt=0):
      methodName = Mn(Sk())
      isEchoKey(methodName)
      echo    = methDct[methodName][0]
      verbose = methDct[methodName][1]
      message = methDct[methodName][2]
      if echo:
        M(Sk(), offset=7)
      #if '\\' in filename:
          #filename = self.setSlash('F', filename)
      try:
          if verbose:
            #if runCnt > 1:
            print 'Writing to file: ', filename
            print 'text', text
          fileObject = self.fileOpen(filename, mode)
          fileObject.write(text)
          fileObject.close()
          #file.flush()
      except: AttributeError

    def setFileHistory(self, filename=' '):
      if len(filename) > 0:
          envDct['lastFile'] = filename
          self.lastFile = filename
         # text = self.lastfile + '\n'                   enable this.
         # self.writeToFile(self.pathHistFile, text, 'a')

    def getFileDictKeys(self):
      tmpLst = []
      dupLst = []
      tmpStr = ''
      for k, v in self.fileDct.iteritems():
          self.writeLine('File Dictionary ', k, ' present.')
          tmpLst.append(os.path.basename(v))
      for item in tmpLst.sort():
          if item == tmpStr:
              dubLst.append(item)
          tmpStr = item
      for item in dupLst:
          self.writeLine(item, ' is duplicated.')

'''endfile'''



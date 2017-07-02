#!/bin/bash
# -*- codign:utf-8 -*-
# baseTools.pathTools.path_Tools
# Coded by Richard Polk
#----------------------------------------------------

impLst = ["from baseTools.fileTools.file_Tools import File_Tools"]

for command in impLst:
  try:
    #print '      |' + __name__ + '|', command
    exec(command)
  except ImportError:
    print  "ImportError! Failure of --> " + command + " <-- detected!"
print '  |' + __name__ + '| ---'

class Path_Tools(File_Tools):

    def __init__(self, **kwargs):
      """  """
      methodName = 'Path_Tools.__init__'
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
      File_Tools.__init__(self)
      print '      |Path_Tools| ---'

      pthPF = os.path.join(confPath, 'pthPF')
      __builtins__['pthPF'] = pthPF

      # pthDct - path history dictionary
      try:
        with open(pthPF, 'rU') as f:
          line1 = f.readline()
      except IOError:
        with open(pthPF, 'w+') as f:
          line1 = f.readline()
        f.close()

      if len(line1) == 0:
        # if the pickle file gets wacked, set some defaults so the dictionary can have some keys.
        pthDct = {'source': '', 'distination': '', 'curDir': '', 'lastDir': '', 'pthCnt': 0}
      else:
        pthDct = pickleJar(pthPF)

      # Get these from a pickled dictionary.

      #self.source         = ''
      #self.distination    = ''
      #self.curDir         = os.getcwd() # Should be passed in.
      #self.maxfileload    = 100000
      #self.blksize        = 1024 * 8

      #self.pathHistLst    = []
      #self.extHistLst     = []
      #self.pathLst        = []
      #self.lastDir        = ''
      #self.excludeLst     = ['RECYCLER', 'tmp', 'TMP', 'Tmp', 'temp', 'TEMP', 'Temp', 'Local Settings', '.qgis', 'dev',
      #                       'OpenOffice.org 2.4', 'OpenOffice.org 3', 'Quantum GIS', 'Documents and Settings',
      #                       'download', 'Python27']
      #

    def askPath(self, inTitle, initialPath=os.getcwd()):
       #! Borked - will not work on network mapped drives.
       pathname = askdirectory(title=inTitle, initialdir=initialPath)
       # tried  os.path.exists(pathname) and did not work except on local
       try:
         if self.pathCheck(pathname):
           self.setCwd(pathname)
           self.setPathHistory(pathname)
           return pathname
       except StandardError:
         self.write_exception
         return None

    def pathCheck(self, path):
        # need to announce instead of write
        pathname = os.path.normpath(path)
        #self.write(self.conCat("Verifying path existance: ", path))
        try:
          statLst = os.stat(path)
          #print statLst
          mode = os.stat(path)[ST_MODE]
          if S_ISDIR(mode):
            #self.write("Verification Succeeded.")
            #self.blankLine(1, "*", 50)
            return 1
          else:
            #self.write(self.conCat(("Path Verification Failed. ", path)))
            #self.blankLine(1, "*", 50)
            return 0
        except:
          self.write_exception
        #! added this because the above code fails in linux.
        finally:
          #! this fails in windows.  Need to code an os switch.
          return os.path.isdir(path)

    def setCwd(self, path=''):
        # Record the current directory to history then reset the current
        # directory to the new path.

        if len(path) == 0:
            self.curDir = self.lastDir
        else:
            self.curDir = path
        self.setPathHistory(self.curDir)
        self.curDir = self.setSlash('F', self.curDir) # Set path seps as forward slash.
        os.chdir(self.curDir)
        envDct['curDir'] = self.curDir

    def goBack(self):
        self.clearLists()
        length = len(self.pathHistLst) - self.clickCount()
        self.setCwd(self.setSlash('F', self.pathHistLst[length]))
        for subdir in os.listdir(self.curDir):
            if os.path.isdir(subdir):
                if isinstance(self.l_listbox):
                    self.l_listbox.insert(END, subdir)
            else:
                if isinstance(self.r_listbox):
                    self.r_listbox.insert(END, subdir)

    def setPathHistory(self, path=' '):
      methodName = Mn(Sk())
      isEchoKey(methodName)
      echo    = methDct[methodName][0]
      verbose = methDct[methodName][1]
      message = methDct[methodName][2]
      if echo == 1:
      # removed tkVar May 20 2013.  Were in a package now.
      # if echo or self.echoVar.get() == self.echoLevel:
        if self.bypass == 0:
          self.clearText()
        M(Sk())

      pthDct['pthCnt'] = len(pthDct.keys())
      self.increment('pathHistCnt')

      try:
        if len(path) > 1:
          #self.pathHistLst.append(path) obsolete, should build from pathHist file on init.
          # replaced with self.setVar
          # envDct['lastDir'] = self.lastDir
          self.s('lastDir', path)
          text = path + '\n'
          if envDct['debug'] > 1:
            self.write(text)
          # write to pickle file.
          pthDct['pthCnt'] = path
          #saveDbase(envDct['pthPF'], pthDct)
          saveState(pthPF)
      except StandardError:
        M(Sk())
        Err()

    def getPathHistory(self):
        self.histFileObject = open(envDct['pathHistFile'], 'r')
        self.pathHistLst = self.histFileObject.readlines()
        self.histFileObject.close()
        length = len(self.pathHistLst) - 1
        self.lastDir = self.pathHistLst[length].strip()
        if not os.path.isdir(self.lastDir):
            self.lastDir = os.getcwd()
        envDct['lastDir'] = self.lastDir
        self.curDir = self.lastDir

    def setHistory(self, mode=1):
        inStr = ''
        if mode == 1:
         if len(self.extVar.get()) > 1:
             # self.extHistLst.append(ext)  obsolete, should build from pathHist file on init.
             self.s('lastExt', self.extVar.get())
             inStr = self.extVar.get() + '\n'
             if self.debug > 1:
               self.write(inStr)
             self.writeToFile(self.extHistFile, inStr, 'a')
        else:
          self.s('lastKword', self.kwVar.get())

    def setPathLst(self):
        self.disabled()

    def setSource(self, initPath='', titleStr='Select a source directory.'):
        if len(initPath) == 0:
          initPath = self.source
        source = self.setSlash("F", askdirectory(title=titleStr, initialdir=initPath))
        if self.pathCheck(source):
          message = 'Source directory is: ' + source
          self.write(message)
          self.s('source', source)
          return source
        else:
          return os.getcwd()

    def setDistination(self, initPath='', titleStr='Select a distination directory.'):
        if len(initPath) == 0:
          initPath = self.distination
        distination = self.setSlash('F', askdirectory(title=titleStr, initialdir=initPath))
        if self.pathCheck(distination):
          message = 'Distination directory is: ' + self.distination
          self.write(message)
          self.s('distination', distination)
          return distination
        else:
          return os.getcwd()

    def checkPathValidity(self, inPath):
        print 'Testing the path validity: ', inPath
        statinfo = os.stat(inPath)
        mode = statinfo.st_mode
        uid  = statinfo.st_gid
        if S_ISDIR(mode):
          print 'Validity test returned:  True'
          return 'True'
        else:
          print 'Validity test returned:  False'
          return 'False'

class Tree_Walker(Path_Tools):
  def __init__(self, top='', out='', exclude='*', dryrun=1, verbose=0, debug=0):

    self.exclude = exclude
    self.dryrun = int(dryrun)
    self.verbose = int(verbose)
    self.debug = int(debug)

    self.pathDct = {}
    self.in_outDct = {}
    self.srcPathLst = []
    self.treeCmdDct = {}
    self.projectedSize = 0
    if __name__ == '__main__':
      print __name__
      P("Running from __main__ with these args:  ", sys.argv)
      self.top = top
      self.out = out
      self.climbTree()
    else:
      self.top = self.lastSource
      self.out = self.lastDistination

  def climbTree(self):
    self.textVar.set(__name__)
    if __name__ == 'path_Tools':
      self.top = self.setSource()
      self.out = self.setDistination()

    #self.walkBranches(self.top)
    #self.processTree()
    #self.estimateSize()
    #self.processCmdLst()
    #if self.debug:
    #  self.echoDictionaries()
  #! Why are these here instead of in common_Vars or user_Vars?
  def bit(self, bytes):
    return bytes * 8

  def kilo(self, bytes):
    return round(bytes / (math.pow(2, 10)), 4)

  def mega(self, bytes):
    return round(bytes / (math.pow(2, 20)), 4)

  def giga(self, bytes):
    return round(bytes / (math.pow(2, 30)), 4)

  def tera(self, bytes):
    return round(bytes / (math.pow(2, 40)), 4)

  def peta(self, bytes):
    return round(bytes / (math.pow(2, 50)), 4)

  def exa(self, bytes):
    return round(bytes / (math.pow(2, 60)), 4)

  def zetta(self, bytes):
    return round(bytes / (math.pow(2, 70)), 4)

  def yotta(self, bytes):
    return round(bytes / (math.pow(2, 80)), 4)

  def walkBranches(self, top):
      '''recursively descend the directory tree rooted at top,
         calling the callback function for each regular file'''

      for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname)[ST_MODE]
        octal = int(oct(stat.S_IMODE(os.stat(pathname).st_mode)))
        #st_size  = statinfo[6] (size of file, in bytes)
        #print octal, mode, os.access(pathname, mode), S_ISDIR(os.stat(pathname)[ST_MODE]), pathname
        if S_ISDIR(mode):
          # It's a directory, recurse into it
          self.processDirs(pathname)
          self.walkBranches(pathname)
        elif S_ISREG(mode):
          # It's a file
          # Filter the pathname based on criteria included in self.exclude
          if not os.path.splitext(f)[1] == self.exclude:
            # call the callback function
            size = os.stat(pathname)[ST_SIZE]
            self.projectedSize = self.projectedSize + size
            #print 'file      bytes:', size
            #print 'total     bytes:', self.projectedSize
            #print 'total kilobytes:', self.kilo(self.projectedSize)
            #print 'total megabytes:', self.mega(self.projectedSize)
            #print 'total gigabytes:', self.giga(self.projectedSize)
            #P()
            self.processfiles(pathname, octal, size)
        else:
          # Unknown file type, print a message
          print 'Skipping %s' % pathname

  def filterPath(self, path):
      path = path.replace('\\', '/')
      return path

  def processDirs(self, path):
      #p = os.path.join(self.out, os.path.splitdrive(os.path.split(file)[0])[1])
      path = path
      p1 = path
      p2 = os.path.join(self.out, os.path.splitdrive(path)[1])
      self.in_outDct[p1] = p2
      #print self.in_outDct[p1]

  def processfiles(self, file, octal, size):
      p1 = os.path.split(file)[0]
      p2 = os.path.join(self.out, os.path.splitdrive(os.path.split(file)[0])[1])
      f  = os.path.split(file)[1]
      if not self.pathDct.has_key(p1):
        self.pathDct[p1] = {}
      self.pathDct[p1][p1] = []
      self.pathDct[p1][p1].insert(0, f)
      self.pathDct[p1][p1].insert(1, octal)
      self.pathDct[p1][p1].insert(2, size)

  def processTree(self):
      command = ''
      self.srcPathLst = self.in_outDct.keys()
      self.srcPathLst.sort()
      for item in self.srcPathLst:
        command = 'mkdir ' + '"' + self.in_outDct[item] + '"'
        if not self.treeCmdDct.has_key('mkdir'):
          self.treeCmdDct['mkdir']= []
        self.treeCmdDct['mkdir'].append(command)
      for k,v in self.pathDct.iteritems():
        for x,y in v.iteritems():
          if self.in_outDct.has_key(k):
            f = self.pathDct[k][k][0]
            src = os.path.join(k, f)
            dst = os.path.join(self.in_outDct[k], f)
            command = 'copy ' + '"' + src + '" ' + '"' + dst + '"'
            if not self.treeCmdDct.has_key('copy'):
              self.treeCmdDct['copy']= []
            self.treeCmdDct['copy'].append(command)

  def processCmdLst(self):

      treeCmdLst1 = self.treeCmdDct['mkdir']
      treeCmdLst2 = self.treeCmdDct['copy']

      treeCmdLst1.sort()
      treeCmdLst2.sort()

      for command in treeCmdLst1:
        if self.dryrun:
          if self.verbose:
            print command
        else:
          if self.verbose:
            print command
          try:
            os.system(command)
          except StandardError:
            print 'Error in processing...'

      for command in treeCmdLst2:
        if self.dryrun:
          if self.verbose:
            print command
        else:
          if self.verbose:
            print command
          try:
            os.system(command)
          except StandardError:
            print 'Error in processing...'

  def echoDictionaries(self):
    #? redundant??
    for k, v in self.pathDct.iteritems():
      print k, v

  def estimateSize(self):
    print '\n\n===================Stats==========================\n'
    print 'total kilobytes:', self.kilo(self.projectedSize)
    print 'total megabytes:', self.mega(self.projectedSize)
    print 'total gigabytes:', self.giga(self.projectedSize)
    print 'total terabytes:', self.tera(self.projectedSize)
    print 'total petabytes:', self.peta(self.projectedSize)
    print '\n==================================================\n\n'

if __name__ == '__main__':
    tw = Tree_Walker(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

    #st_mode  = statinfo[0] (protection bits)
    #st_ino   = statinfo[1] (inode number)
    #st_dev   = statinfo[2] (device)
    #st_nlink = statinfo[3] (number of hard links)
    #st_uid   = statinfo[4] (user ID of owner)
    #st_gid   = statinfo[5] (group ID of owner)
    #st_size  = statinfo[6] (size of file, in bytes)
    #st_atime = statinfo[7] (time of most recent access)
    #st_mtime = statinfo[8] (time of most recent content modification)
    #st_ctime = statinfo[9] (time of creation)

'''endfile'''
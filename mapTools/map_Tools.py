#!/bin/bash
# -*- codign:utf-8 -*-
# baseTools.mapTools.map_Tools
# Coded by Richard Polk
#----------------------------------------------------

impLst = ["from baseTools.pathTools.path_Tools import Path_Tools"]

for command in impLst:
  try:
    #print '    |' + __name__ + '|', command
    exec(command)
  except ImportError:
    print  "ImportError! Failure of --> " + command + " <-- detected!"
print '  |' + __name__ + '| ---'

class Map_Tools(Path_Tools):

    def __init__(self, **kwargs):
      """  """
      methodName = 'Map_Tools.__init__'
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
      Path_Tools.__init__(self)
      print '    |Map_Tools| --->'

    def remKey(self, inDct, inKey):
      if inKey in inDct:
        del inDct[inKey]

    def defineDict(self, kvLst):
      argDct = self.dictFromList(kvLst)
      return argDct

    def dictFromList(self, kvLst):

      # Create a dictionary from a list of alternating keys and values.
      # Pairwise is faster, if it works.
      # ---------------------------------------------------------------------------------------

      inLst = zip(kvLst[::2], kvLst[1::2])
      outLst = []
      for i in range(len(inLst)):
        #item is a tuple of strings at this point
        k = inLst[i][0]
        v = inLst[i][1]
        v = (v.replace("'", "")).replace('"', '') # dequote from String_Tools class
        if v.isdigit():
          v = int(v)
        #print k, ': ', v, ' ', type(v)
        if k[-3:] == "Lst":
          v = ((v[1:-1]).replace(' ', '')).split(',')
          for x in v:
            if x.isdigit():

              x = int(x)
            #print x, type(x)
          #print v, type(v)
        if k[-3:] == "Dct":
          #print v, type(v), len(v)
          v = ((v[1:-1]).replace(':', ',')).replace(' ', '').split(',')
          v = dict(zip(v[::2], v[1::2]))
          for a,j in v.iteritems():
            #print a, j, type(j), j.isdigit()
            if j.isdigit():
              v[a] = int(j)
          #print v, type(v), len(v)

        outLst.append(k)
        outLst.append(v)

      return dict(zip(outLst[::2], outLst[1::2]))

    # ---------------------------------------------------------------------------------------
    def pairwise(iterable):
      itnext = iter(iterable).next()
      while True:
        yield itnext(), itnext()
    # ---------------------------------------------------------------------------------------
    def dictFromSequence(seq):
      return dict(pairwise(seq))
    # ---------------------------------------------------------------------------------------
    # Defining pairwise also allows updating an existing dictionary with any sequence of alternating keys and values --
    # example:  mydict.update(pairwise(seq))

    def keysValues(self):
      #? recode os.environ['TOOLS'] as a pickled state variable
      kvFile = os.environ['TOOLS'] + os.sep + '_lists' + os.sep + 'key_value.lst'
      file = open(kvFile, 'rU')
      dict = {}
      tmpLst = []
      previous = ''
      for line in file.readlines():
        item = line.strip()
        itemLst = line.split()
        key = itemLst[0]
        if key != previous:
            tmpLst = []
        value = itemLst[1]
        tmpLst.append(value)
        dict[key] = tmpLst
        previous = key
      file.close()
      return dict
'''endfile'''
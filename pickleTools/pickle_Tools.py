#!/bin/bash
# -*- codign:utf-8 -*-
# baseTools.pickleTools.pickle_Tools
# Coded by Richard Polk
#----------------------------------------------------
# __all__ specifies which which names will be exported when the from * statement is used.
# Only the names in the list will be exported.
# Conversly names in the form _X identify a name not to be exported.  Any name with a
# leading underscore will not be exported when the from * statement is called.
# In this case, the __all__ list contains all the names used in this module so
# is really not necessary unless a function is added that is not intended to be exported
# implictly using the from *

__all__ = ['pickOpt', 'loadDbase', 'saveDbase', 'saveState', 'pickleJar', 'save']

"""
Dependancies --
pickle
pickletools
"""

impLst = ["import pickle",
          "__builtins__['pickle'] = pickle",
          "dispatch_table = pickle.dispatch_table",
          "__builtins__['PickleError'] = pickle.PickleError",
          "__builtins__['PicklingError'] = pickle.PicklingError",
          "__builtins__['UnpicklingError'] = pickle.UnpicklingError",
          "import pickletools"]

for command in impLst:
  try:
    #print '  |' + __name__ + '|', command
    exec(command)
  except ImportError:
    print  "ImportError! --> " + command + " <-- Failed!"
print '  |' + __name__ + '| ---'

#-----------------------------------------------------
# Experimental unpickler class.  Not implimented
#class Un_Pickler(pickle.Unpickler):
#
#    def load_setitem(self):
#        """Pop of value and key from a list of keys and values.  The value is at the
#        end so it gets poped off first."""
#        stack = self.stack
#        #if len(stack) == 3:
#        print '----------------------------------------------'
#        print 'stack len', len(stack)
#        for x in stack:
#          print x
#        value = stack.pop()
#        key = stack.pop()
#          # insert a blank dictionary into the first slot of the stack list
#        dict = stack[-1]
#          # Populate the dictionary with the key value pairs.
#        dict[key] = value
#
#          #for k,v in dict.iteritems():
#            #print k,':',v
#        print '----------------------------------------------'
#        raw_input()
#
#        #print
#

def pickOpt(p):
    """pickOpt i.e. Pickle Optimizer.
    Optimize a pickle string by removing unused PUT opcodes."""
    gets = set()            # set of args used by a GET opcode
    puts = []               # (arg, startpos, stoppos) for the PUT opcodes
    prevpos = None          # set to pos if previous opcode was a PUT
    for opcode, arg, pos in pickletools.genops(p):
        if prevpos is not None:
            puts.append((prevarg, prevpos, pos))
            prevpos = None
        if 'PUT' in opcode.name:
            prevarg, prevpos = arg, pos
        elif 'GET' in opcode.name:
            gets.add(arg)

    # Copy the pickle string except for PUTS without a corresponding GET
    s = []
    i = 0
    for arg, start, stop in puts:
        j = stop if (arg in gets) else start
        s.append(p[i:j])
        i = stop
    s.append(p[i:])
    return ''.join(s)

def loadDbase(filename, passIn="unknown"):

  # some debug statements
  #print '\nIn loadDbase\nfilename',filename,'\npassed in from',passIn
  #with open(filename, 'rU') as f:
    #line1 = f.readline()

  try:
    with open(filename, 'rU') as f:
      line1 = f.readline()
  except IOError:
    with open(filename, 'w+') as f:
      line1 = f.readline()
    f.close()



  if len(line1) == 0:
    return dict()
  else:
    # file = open(filename, 'r') will fail going from win to lin.
    # 'U' allows universal line ending conversion.  i.e. it converts win line
    # endings to lin.
    file = open(filename, 'rU')
    #print file
    #print pickle.load(file)
    #raw_input('Hit <Enter> to continue: ')
    object = pickle.load(file)
    #print 'object', object, type(object)
    file.close()
    return object
    #print 'object ', type(object), len(object)
    #print object
    #raw_input('Hit <Enter> to continue: ')

def saveDbase(filename, object):
  print """obsolete -- use saveState instead.\n"""
  file = open(filename, 'w')
  # convert dictionary to pickled string and
  # write to file.
  file.write(pickOpt(pickle.dumps(object)))
  file.close()

def saveState(pFile):
  """saveState - preserve the state of variable names and values.
  Usage - saveState(envPF)
  pFile is a pickle file whose name is associated with a state dictionary.
  The state dictionary name format must end with 'Dct' and exist in __builtins__.
  Uses pickOpt to optimize output pickle files.
  Done with pickOpt"""
  filename = os.path.split(pFile)[1]
  prefix = filename[:-2]
  inDct = eval(prefix + 'Dct')
  fileobject = open(pFile, 'w')
  # convert dictionary to pickled string and
  # write to file.
  fileobject.write(pickOpt(pickle.dumps(inDct)))
  fileobject.close()
  inDct = None

def pickleJar(filename, passIn="unknown"):
  #print '\nIn pickleJar.\nfilename',filename,'\npassed in from',passIn
  tmpDct = loadDbase(filename, 'pickleJar')
  #print 'tmpDct', type(tmpDct)
  return tmpDct

def save(self, obj):
  # Redefined from pickle.Pickler to handle instance and method type write errors.
  # Check for persistent id (defined by a subclass)
  pid = self.persistent_id(obj)
  if pid:
      self.save_pers(pid)
      return

  # Check the memo
  x = self.memo.get(id(obj))
  if x:
      self.write(self.get(x[0]))
      return

  # Check the type dispatch table
  t = type(obj)

  # To avoid crashing the pickle process and corupting the file
  # by trying to pickle an instancemethod, just convert it to a string.
  # cmp 0 is true
  if cmp(str(t), "<type 'instancemethod'>") == 0:

    # write a string representation of the instancemethod to avoid
    # interupting the pickle process
    #"PicklingError!! Can't pickle %r object: %r" %(t.__name__, obj))
    obj = str("PicklingError!! Can't pickle %r object: %r" %(t.__name__, obj))
    t = type(obj)

  # f is the save_ function which is customized for each data type.
  # i.e. save_list save_dict save_string
  f = self.dispatch.get(t)

  if f:
      f(self, obj) # Call unbound method with explicit self
      return

  # Check for a class with a custom metaclass; treat as regular class
  try:
      issc = issubclass(t, TypeType)
  except TypeError: # t is not a class (old Boost; see SF #502085)
      issc = 0
  if issc:
      self.save_global(obj)
      return

  # Check copy_reg.dispatch_table
  reduce = dispatch_table.get(t)
  if reduce:
      rv = reduce(obj)
  else:
      # Check for a __reduce_ex__ method, fall back to __reduce__
      reduce = getattr(obj, "__reduce_ex__", None)
      if reduce:
          rv = reduce(self.proto)
      else:
          reduce = getattr(obj, "__reduce__", None)
          if reduce:
              rv = reduce()
          else:
              raise PicklingError("Can't pickle %r object: %r" %
                                  (t.__name__, obj))

  # Check for string returned by reduce(), meaning "save as global"
  if type(rv) is StringType:
      self.save_global(obj, rv)
      return

  # Assert that reduce() returned a tuple
  if type(rv) is not TupleType:
      raise PicklingError("%s must return string or tuple" % reduce)

  # Assert that it returned an appropriately sized tuple
  l = len(rv)
  if not (2 <= l <= 5):
      raise PicklingError("Tuple returned by %s must have "
                          "two to five elements" % reduce)

  # Save the reduce() output and finally memoize the object
  self.save_reduce(obj=obj, *rv)

#print 'pickle', pickle
#for x in dir(pickle):
#  print x
#for x in dir(pickle.Pickler):
#  print x

# redefine pickle.Pickler.save to our own version
pickle.Pickler.save = save

#print '|baseTools| ---'
'''endfile'''
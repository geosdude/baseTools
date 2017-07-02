# /GeoPy/lib/typeTools/type_Tools.py
# This class is a base class


class Type_Class:
  """Types available in Python are:

     NoneType
     The type of None.

     TypeType
     The type of type objects (such as returned by type()).

     BooleanType
     The type of the bool values True and False; this is an alias of the built-in bool() function. New in version 2.3.

     IntType
     The type of integers (e.g. 1).

     LongType
     The type of long integers (e.g. 1L).

     FloatType
     The type of floating point numbers (e.g. 1.0).

     ComplexType
     The type of complex numbers (e.g. 1.0j). This is not defined if Python was built without complex number support.

     StringType
     The type of character strings (e.g. 'Spam').

     UnicodeType
     The type of Unicode character strings (e.g. u'Spam'). This is not defined if Python was built without Unicode support.

     TupleType
     The type of tuples (e.g. (1, 2, 3, 'Spam')).

     ListType
     The type of lists (e.g. [0, 1, 2, 3]).

     DictType
     The type of dictionaries (e.g. {'Bacon': 1, 'Ham': 0}).

     DictionaryType
     An alternate name for DictType.

     FunctionType
     The type of user-defined functions and lambdas.

     LambdaType
     An alternate name for FunctionType.

     GeneratorType
     The type of generator-iterator objects, produced by calling a generator function. New in version 2.2.

     CodeType
     The type for code objects such as returned by compile().

     ClassType
     The type of user-defined classes.

     InstanceType
     The type of instances of user-defined classes.

     MethodType
     The type of methods of user-defined class instances.

     UnboundMethodType
     An alternate name for MethodType.

     BuiltinFunctionType
     The type of built-in functions like len() or sys.exit().

     BuiltinMethodType
     An alternate name for BuiltinFunction.

     ModuleType
     The type of modules.

     FileType
     The type of open file objects such as sys.stdout.

     XRangeType
     The type of range objects returned by xrange().

     SliceType
     The type of objects returned by slice().

     EllipsisType
     The type of Ellipsis.

     TracebackType
     The type of traceback objects such as found in sys.exc_traceback.

     FrameType
     The type of frame objects such as found in tb.tb_frame if tb is a traceback object.

     BufferType
     The type of buffer objects created by the buffer() function.

     StringTypes
     A sequence containing StringType and UnicodeType used to facilitate easier checking for any string object.
     Using this is more portable than using a sequence of the two string types constructed elsewhere since it
     only contains UnicodeType if it has been built in the running version of Python.
     For example: isinstance(s, types.StringTypes). New in version 2.2."""

    def __init__(self):

      tmpLst = dir(types)
      self.typeDct = {}
      errFlag = 0
      for item in tmpLst:
        if "Type" in item:
          key = item
          command = "value = types." + key + ".__doc__"
          try:
            exec(command)
            self.typeDct[key] = value
          except StandardError:
            errFlag = 1

    def v_Instance(self, *args):
      args = list(args)

      #for x in range(len(args)):
        #isinstance(args[x], types.StringTypes)

'''endfile'''
#!/bin/bash
# /GeoPy/lib/IO/echo_Tools.py

#! Borked.  Cant get inheritence.  Importing _base breaks the class inheritence tree.
#from _base import *
#! Intended for version 3 migration...which failed.
#class Echo_Tools(Base):
#! consider moving these into base_Tools.py  This should be a base functionality.








    #       Test these before using them
    #def sortedDictValues1(adict):
    #    items = adict.items()
    #    items.sort()
    #    return [value for key, value in items]
    #
    ## an alternative implementation, which
    ## happens to run a bit faster for large
    ## dictionaries on my machine:
    #def sortedDictValues2(adict):
    #    keys = adict.keys()
    #    keys.sort()
    #    return [dict[key] for key in keys]
    #
    ## a further slight speed-up on my box
    ## is to map a bound-method:
    #def sortedDictValues3(adict):
    #    keys = adict.keys()
    #    keys.sort()
    #    return map(adict.get, keys)

# *args **kwargs
#Or, How to use variable length argument lists in Python.
#
# The special syntax, *args and **kwargs in function definitions is used to pass a
# variable number of arguments to a function.
# The single asterisk form (*args) is used to pass a non-keyworded, variable-length argument list, and
# the double asterisk form is used to pass a keyworded, variable-length argument list.

# Here is an example of how to use the non-keyworded form.

# This example passes one formal (positional) argument, and two more variable length arguments.
#
#def test_var_args(farg, *args):
#    print "formal arg:", farg
#    for arg in args:
#        print "another arg:", arg
#
#test_var_args(1, "two", 3)
#Results:
#
#formal arg: 1
#another arg: two
#another arg: 3
#
#Here is an example of how to use the keyworded form.

# This example passes one formal (positional) argument, and two KEYWORDED variable arguments are passed.
#
#def test_var_kwargs(farg, **kwargs):
#    print "formal arg:", farg
#    for key in kwargs:
#        print "another keyword arg: %s: %s" % (key, kwargs[key])
#
#test_var_kwargs(farg=1, myarg2="two", myarg3=3)
#Results:
#
#formal arg: 1
#another keyword arg: myarg2: two
#another keyword arg: myarg3: 3

'''endfile'''
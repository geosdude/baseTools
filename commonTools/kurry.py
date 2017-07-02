#!/bin/bash
# -*- codign:utf-8 -*-
# baseTools.common.kurry
# Code modified by Richard Polk
# Derived from David Daniels recipe
# 'Curry -- associating parameters with a function'
# in the 'Python Cookbook' http://aspn.activestate.com/ASPN/Python/Cookbook/
#----------------------------------------------------

print '  |' + __name__ + '| ---'

class Kurry:
    """This class is a base class and only needs __builtin__"""
    def __init__(self, fn, *args, **kwargs):

        self.fn = fn
        self.pending = args[:]
        self.kwargs = kwargs.copy()
        #print 'self.fn = ', self.fn
        #print 'self.pending = ', self.pending
        #print 'self.kwargs = ', self.kwargs

    def __call__(self, *args, **kwargs):  # Called when the instance is called as a function.
        if kwargs and self.kwargs:
          kw = self.kwargs.copy()
          kw.update(kwargs)
        else:
          kw = kwargs or self.kwargs
#          print 'kw', kw, 'self.fn', self.fn, 'self.pending + args', self.pending + args
        return self.fn(*(self.pending + args), **kw)

__builtins__['Kurry'] = Kurry

# """
# In functional programming, currying is a way to bind arguments with a function and wait for the
# rest of the arguments to show up later. You "curry in" the first few parameters to a function,
# giving you a function that takes subsequent parameters as input and calls the original with all
# of those parameters. This recipe uses a class instance to hold the parameters before their
# first use. For example:
#
#    double = curry(operator.mul, 2)
#    triple = curry(operator.mul, 3)
#
#    class curry:
#        def __init__(self, farg, *args, **kwargs):
#            self.farg = farg
#            self.pending = args[:]
#            self.kwargs = kwargs.copy()
#
#        def __call__(self, *args, **kwargs):
#            if kwargs and self.kwargs:
#                kw = self.kwargs.copy()
#                kw.update(kwargs)
#            else:
#                kw = kwargs or self.kwargs
#
#            return self.farg(*(self.pending + args), **kw)
#
# A typical use of curry is to construct callback functions for GUI operations. When the
# operation does not really merit a new function name, curry can be useful in creating these
# little functions. This can be the case with commands for buttons, for example.
#
#    self.button = Button(frame, text='A', command=curry(transcript.append, 'A'))
#
# Curry can also be used interactively by making versions of your functions with
# debugging-appropriate defaults or initial parameters filled in for your current case. For
# example, database debugging work might well begin by setting:
#
#    Connect = curry(ODBC.Connect, dsn='MyDataSet')
#
# If you are creating a function for regular use, and there is a good choice for a name,
# the 'def fun(...' form of function definition is usually more readable, and often more
# easily extended. As you can see from the implementation, no magic happens to
# "specialize" the function with the provided parameters; curry should be used when
# you feel the code is more clear with its use than without. Typically this will be to
# emphasize that you are only providing parameters to a "commonly used"
# (in this application) function, not providing separate processing.
# """
#print '|baseTools| ---'
'''endfile'''
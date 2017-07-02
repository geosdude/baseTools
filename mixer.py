#!/bin/bash
# -*- codign:utf-8 -*-
# baseTools.mixer
# Coded by Richard Polk
#----------------------------------------------------

print '  |' + __name__ + '| ---'

class MixIn:
  """
  This class is a base class and only needs __builtin__
  A class mixin method that performs class mixes in place.
  i.e. the base class is modified.

  Tags the class with a list of names of mixed members.

  Example usage:
   class addSubMixin:
    	def add(self, value):
   		return self.number + value

    	def subtract(self, value):
    		return self.number - value


   class myClass:
    	def __init__(self, number):
    		self.number = number

  Then, at runtime, you can mix any class into any other with:
         base   , addition
   MixIn(myClass, addSubMixin)
   myInstance = myClass(4)
   myInstance.add(2)
   myInstance.subtract(2)
  """
  #def __init__(self):
    #print '  |MixIn| ---'
    #print '|baseTools| ---'

  def __call__(self, base, addition):
      self.mixIn(base, addition)

  def mixIn(self, base, addition):
      """
A mixin is a collection of methods that can be injected into a class.
The mixin technique consists in building classes by composing reusable mixins.
      """
      #assert not hasattr(base, '_mixed_')
      mixed = []
      for item, val in addition.__dict__.items():
          if not hasattr(base, item):
              setattr(base, item, val)
              mixed.append(item)
      base._mixed_ = mixed


#class UnMix(object):
class UnMix:
  #def __init__(self):
    #print '  |' + __name__ + '.UnMix| ---'
    #print '|baseTools| ---'
  def __call__(self, cla):
    self.unMix(cla)
  def unMix(self, cla):

      for m in cla._mixed_: #_mixed_ must exist, or there was no mixin
        delattr(cla, m)
      del cla._mixed_

#class MixedIn(MixIn):
#  """
#  A class mixin method that performs class mixes and returns a new class.
#  """
#  def __call__(self, base, addition):
#      self.mixedIn(base, addition)
#
#  def mixedIn(self, base, addition):
#
#      class newClass: pass
#      newClass.__dict__ = base.__dict__.copy()
#      self.mixIn(newClass, addition)
#      return newClass





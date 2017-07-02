#!/bin/bash
# -*- codign:utf-8 -*-
# xml_Tools.py
# Coded by Richard Polk, Jr
#
#-----------------------------------------------------

class XML_Tools:
    """This class is a base class and only needs __builtin__"""
    def launchXML(self):
      try:
        from lxml import etree
        self.write("running with lxml.etree\n")
      except ImportError:
        try:
          # Python 2.5
          import xml.etree.cElementTree as etree
          self.write("running with cElementTree on Python 2.5+\n")
        except ImportError:
          try:
            # Python 2.5
            import xml.etree.ElementTree as etree
            self.write("running with ElementTree on Python 2.5+\n")
          except ImportError:
            try:
              # normal cElementTree install
              import cElementTree as etree
              self.write("running with cElementTree\n")
            except ImportError:
              try:
                # normal ElementTree install
                import elementtree.ElementTree as etree
                self.write("running with ElementTree\n")
              except ImportError:
                self.write("Failed to import ElementTree from any known place\n")
      self.eTree = etree
      self.write(dir(self.eTree))

    def readXML(self):
      flag = None
      xmlFile = self.askFileName("Select an XML file.", "xml")
      try:
        from lxml import etree
        self.parser = etree.XMLParser(ns_clean=True)
        self.xTree  = etree.parse(xmlFile, self.parser)
        flag = 1
        #print 'from lxml import etree'
      except ImportError:
        import xml.etree.ElementTree as etree
        self.xTree = etree.parse(xmlFile)
        flag = 0
        #print 'import xml.etree.ElementTree as etree'

      self.xRoot = self.xTree.getroot()
      self.write("Root element is: ", self.xRoot, " of type: ", str(type(self.xRoot)), "\n")
      self.write("XML content is: \n")

      if flag:
        self.xString = etree.tostring(self.xRoot, pretty_print=True)
      else:
        self.xString = etree.tostring(self.xRoot)
      print self.xString
      #self.write(self.xString)

    def loadXML(self):
      flag = None
      xmlFile = self.askFileName("Select an XML file.", "xml")
      try:
        from lxml import etree
        self.parser = etree.XMLParser(ns_clean=True)
        self.xTree  = etree.parse(xmlFile, self.parser)
        flag = 1
        #print 'from lxml import etree'
      except ImportError:
        import xml.etree.ElementTree as etree
        self.xTree = etree.parse(xmlFile)
        flag = 0
        #print 'import xml.etree.ElementTree as etree'

      self.xRoot = self.xTree.getroot()
      #root = etree.Element("root")
      #self.write('self.xRoot is:', self.xRoot)

      #children = self.xRoot.getchildren()
      #for child in children:
        #self.write(child)

    def formatXMLfile(self):
      flag = None
      xmlFile = self.askFileName("Select an XML file.", "xml")
      try:
        from lxml import etree
        self.parser = etree.XMLParser(ns_clean=True)
        self.xTree  = etree.parse(xmlFile, self.parser)
        flag = 1
        #print 'from lxml import etree'
      except ImportError:
        import xml.etree.ElementTree as etree
        self.xTree = etree.parse(xmlFile)
        flag = 0
        #print 'import xml.etree.ElementTree as etree'

      self.xList = []
      self.xRoot = self.xTree.getroot()
      self.write("Root element is: ", self.xRoot, " of type: ", str(type(self.xRoot)), "\n")

      if flag:
        self.xString = etree.tostring(self.xRoot, pretty_print=True)
      else:
        self.xString = etree.tostring(self.xRoot)
      self.xList = self.xString.split('\n')
      self.write('Formatting xml file.')
      self.fileWriteList(xmlFile, self.xList)
      self.write('Format complete.')

#print '|baseTools| ---'

'''endfile'''
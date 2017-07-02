#!/bin/bash
#/GeoPy/lib/URL/url_Tools.py
import sgmllib, urllib2, htmllib
from base import *
class URL_Tools(Base):
    '''This class is a base class'''
    def readURL(self, url=''):

      procLst = []

      for x in range(0, 17):
        f = ''
        inc = str(x * 25)
        #      http://ngmdb.usgs.gov/lex-bin/display_lexv5.pl?1259698961&0
        #url = 'http://ngmdb.usgs.gov/lex-bin/display_lexv5.pl?1259698961&' + inc + '&'
        #url = 'http://www.lfd.uci.edu/~gohlke/pythonlibs/'
        #url = 'http://128.195.135.4/~gohlke/pythonlibs/'
        f = urllib2.urlopen(url)
        s = f.read()
        f.close()
        self.parse(s)

      outLst = self.get_hyperlinks()
      filename = os.path.join(self.listPath, "url.lst")
      self.write(self.echoDict(self.unitDct)[4])
      self.fileWriteList(filename, outLst)


    def readURL_List(self):
      self.unitDct = self.defineDict(self.getFileAsList(os.path.join(self.listPath, "geo_url.lst"))[0])
      self.write(self.echoDict(self.unitDct)[4])

      cnt = 1
      i = 0
      j = 0

      for k, v in self.unitDct.iteritems():
        if cnt < 2:
          self.write(v)
          f = urllib2.urlopen(v)
          s = f.readlines()
          f.close()
          #s[i:j] slice of s from i to j
          for x in range(len(s)):
            #self.write(len(s))
            try:
              if s[x].isspace():
                s.pop(x)
            except IndexError:
              pass

          for x in range(len(s)):
            s[x] = s[x].strip()
            #self.write(len(s))
            #self.write(x, ' ', type(x), len(s[x]), s[x])
            #self.write(s[x].strip())
            if "Usage:" in s[x]:
              i = x
              self.write("found usage")
            if "<TABLE>" in s[x]:
              j = x
              self.write("found <TABLE>")
              s = s[i:j]
              break
        cnt = cnt + 1

      self.blankLine()
      for item in s:
        item = ((item.replace("<br/>", "")).replace("<B>", "")).replace("</B>", "")
        self.write(item)



class Parser_Tools(sgmllib.SGMLParser):
    "A simple parser class."

    def __init__(self, verbose=0):
      "Initialise an object, passing 'verbose' to the superclass."

      sgmllib.SGMLParser.__init__(self, verbose)

      self.hyperlinks = []

      self.tempStr = ''
      self.unitDct = {}

      self.inside_a_element = 0

    def parse(self, s):
      "Parse the given string 's'."

      self.feed(s)
      self.close()

    def start_a(self, attributes):
      "Process a hyperlink and its 'attributes'."
      for name, value in attributes:
        if name == "href":
          if "Geolex" in value:
            if "geolex_qs" in value:
              pass
            else:
              self.tempStr = "http://ngmdb.usgs.gov" + value
              self.inside_a_element = 1

    def handle_data(self, data):
      "Handle the textual 'data'."

      if self.inside_a_element:
        data = data.strip()
        self.hyperlinks.append(data)
        self.hyperlinks.append(self.tempStr)
        command = 'self.unitDct["' + data + '"] = "http://ngmdb.usgs.gov' + self.tempStr + '"'
        exec(command)

    def end_a(self):
      "Record the end of a hyperlink."

      self.inside_a_element = 0


    def get_hyperlinks(self):
      "Return the list of hyperlinks."

      return self.hyperlinks
'''endfile'''
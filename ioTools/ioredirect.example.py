class IORedirector(object):
    """A general class for redirecting I/O to this Text widget."""
    def __init__(self, text_area):
        self.text_area = text_area

class StdoutRedirector(IORedirector):   # in my case, the Text_Widget class
    """A class for redirecting stdout to this Text widget."""
    def write(self, str):
        self.text_area.write(str, False)

#and then, in your Tkinter widget:

# To start redirecting stdout:
import sys
sys.stdout = StdoutRedirector(self)
# (where self refers to the widget)  in my case, right after the Text_Widget class is
# instanciated, sys.stdout = self

# To stop redirecting stdout:
sys.stdout = sys.__stdout__

class Redirect(object):

   def __init__(self, stdout):
       self.stdout = stdout

   def write(self, s):
       self.stdout.write(string.lower(s))
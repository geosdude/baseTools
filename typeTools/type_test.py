import sys,os,string,types

tmpLst = dir(types)
typeDct = {}
errFlag = 0
for item in tmpLst:
  if "Type" in item:
    key = item
    command = "value = types." + key + ".__doc__"
    try:
      exec(command)
      typeDct[key] = value
    except StandardError:
      errFlag = 1

if errFlag:
  typeDct[key] = "*"
  print command
else:
  for k,v in typeDct.iteritems():
    print "\n", k+":", v
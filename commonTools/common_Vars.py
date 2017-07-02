#!/bin/bash
# -*- codign:utf-8 -*-
# baseTools.common.common_Vars
# Coded by Richard Polk
#----------------------------------------------------

print '  |' + __name__ + '| ---'

#! Borked.  Cant get inheritence.  Importing _base breaks the class inheritence tree.
#from _base import *
#! Intended for version 3 migration...which failed.

impLst = ["from baseTools.mapTools.map_Tools import Map_Tools",
          "from baseTools.ioTools.io_Tools import Pied_Piper"]

for command in impLst:
  try:
    #print '  |' + __name__ + '|', command
    exec(command)
  except ImportError:
    print  "ImportError! Failure of --> " + command + " <-- detected!"
print '  |' + __name__ + '| ---'

class Common_Vars(Pied_Piper, Map_Tools):
  """
  Defined variables not used by higher classes.
  Intended to contain user defined variables
  for use in user defined classes.
  """
  def __init__(self, **kwargs):
    """  """
    methodName = 'Common_Vars.__init__'
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
    Pied_Piper.__init__(self)
    Map_Tools.__init__(self)
    print '  |Common_Vars| --->'

    self.fileDct = {} #   0       1           2      3     4      5    6      7
    self.fileLst = [] #                                               Blank  Blank
    #               Num Pnum   Name         FIPS  Reg  Abbv  Dist     Dict 1 Dict 2
    self.cntyDct = {1:  ['01', 'Anderson',   '1',   '1', 'ande', '4',  {},   {} ],
                    2:  ['02', 'Bedford',    '3',   '3', 'bedf', '4',  {},   {} ],
                    3:  ['03', 'Benton',     '5',   '4', 'bent', '1',  {},   {} ],
                    4:  ['04', 'Bledsoe',    '7',   '2', 'bled', '2',  {},   {} ],
                    5:  ['05', 'Blount',     '9',   '1', 'blou', '5',  {},   {} ],
                    6:  ['06', 'Bradley',    '11',  '2', 'brad', '1',  {},   {} ],
                    7:  ['07', 'Campbell',   '13',  '1', 'camp', '4',  {},   {} ],
                    8:  ['08', 'Cannon',     '15',  '2', 'cann', '5',  {},   {} ],
                    9:  ['09', 'Carroll',    '17',  '4', 'carr', '1',  {},   {} ],
                    10: ['10', 'Carter',     '19',  '1', 'cart', '1',  {},   {} ],
                    11: ['11', 'Cheatham',   '21',  '3', 'chea', '3',  {},   {} ],
                    12: ['12', 'Chester',    '23',  '4', 'ches', '3',  {},   {} ],
                    13: ['13', 'Claiborne',  '25',  '1', 'clai', '4',  {},   {} ],
                    14: ['14', 'Clay',       '27',  '2', 'clay', '4',  {},   {} ],
                    15: ['15', 'Cocke',      '29',  '1', 'cock', '3',  {},   {} ],
                    16: ['16', 'Coffee',     '31',  '2', 'coff', '5',  {},   {} ],
                    17: ['17', 'Crockett',   '33',  '4', 'croc', '4',  {},   {} ],
                    18: ['18', 'Cumberland', '35',  '2', 'cumb', '3',  {},   {} ],
                    19: ['19', 'Davidson',   '37',  '3', 'davi', '1',  {},   {} ],
                    20: ['20', 'Decatur',    '39',  '4', 'deca', '1',  {},   {} ],
                    21: ['21', 'DeKalb',     '41',  '2', 'deka', '4',  {},   {} ],
                    22: ['22', 'Dickson',    '43',  '3', 'dick', '5',  {},   {} ],
                    23: ['23', 'Dyer',       '45',  '4', 'dyer', '2',  {},   {} ],
                    24: ['24', 'Fayette',    '47',  '4', 'faye', '3',  {},   {} ],
                    25: ['25', 'Fentress',   '49',  '2', 'fent', '3',  {},   {} ],
                    26: ['26', 'Franklin',   '51',  '2', 'fran', '5',  {},   {} ],
                    27: ['27', 'Gibson',     '53',  '4', 'gibs', '2',  {},   {} ],
                    28: ['28', 'Giles',      '55',  '3', 'gile', '6',  {},   {} ],
                    29: ['29', 'Grainger',   '57',  '1', 'grai', '2',  {},   {} ],
                    30: ['30', 'Greene',     '59',  '1', 'gree', '3',  {},   {} ],
                    31: ['31', 'Grundy',     '61',  '2', 'grun', '2',  {},   {} ],
                    32: ['32', 'Hamblen',    '63',  '1', 'hamb', '2',  {},   {} ],
                    33: ['33', 'Hamilton',   '65',  '2', 'hami', '1',  {},   {} ],
                    34: ['34', 'Hancock',    '67',  '1', 'hanc', '2',  {},   {} ],
                    35: ['35', 'Hardeman',   '69',  '4', 'hrdm', '3',  {},   {} ],
                    36: ['36', 'Hardin',     '71',  '4', 'hrdn', '3',  {},   {} ],
                    37: ['37', 'Hawkins',    '73',  '1', 'hawk', '2',  {},   {} ],
                    38: ['38', 'Haywood',    '75',  '4', 'hayw', '4',  {},   {} ],
                    39: ['39', 'Henderson',  '77',  '4', 'hend', '4',  {},   {} ],
                    40: ['40', 'Henry',      '79',  '4', 'henr', '1',  {},   {} ],
                    41: ['41', 'Hickman',    '81',  '3', 'hick', '5',  {},   {} ],
                    42: ['42', 'Houston',    '83',  '3', 'hous', '3',  {},   {} ],
                    43: ['43', 'Humphreys',  '85',  '3', 'hump', '5',  {},   {} ],
                    44: ['44', 'Jackson',    '87',  '2', 'jack', '4',  {},   {} ],
                    45: ['45', 'Jefferson',  '89',  '1', 'jeff', '3',  {},   {} ],
                    46: ['46', 'Johnson',    '91',  '1', 'john', '1',  {},   {} ],
                    47: ['47', 'Knox',       '93',  '1', 'knox', '5',  {},   {} ],
                    48: ['48', 'Lake',       '95',  '4', 'lake', '2',  {},   {} ],
                    49: ['49', 'Lauderdale', '97',  '4', 'laud', '5',  {},   {} ],
                    50: ['50', 'Lawrence',   '99',  '3', 'lawr', '6',  {},   {} ],
                    51: ['51', 'Lewis',      '101', '3', 'lewi', '6',  {},   {} ],
                    52: ['52', 'Lincoln',    '103', '3', 'linc', '4',  {},   {} ],
                    53: ['53', 'Loudon',     '105', '1', 'loud', '6',  {},   {} ],
                    54: ['54', 'McMinn',     '107', '2', 'mcmi', '1',  {},   {} ],
                    55: ['55', 'McNairy',    '109', '4', 'mcna', '3',  {},   {} ],
                    56: ['56', 'Macon',      '111', '3', 'maco', '2',  {},   {} ],
                    57: ['57', 'Madison',    '113', '4', 'madi', '4',  {},   {} ],
                    58: ['58', 'Marion',     '115', '2', 'mari', '2',  {},   {} ],
                    59: ['59', 'Marshall',   '117', '3', 'mars', '4',  {},   {} ],
                    60: ['60', 'Maury',      '119', '3', 'maur', '6',  {},   {} ],
                    61: ['61', 'Meigs',      '121', '2', 'meig', '1',  {},   {} ],
                    62: ['62', 'Monroe',     '123', '1', 'monr', '6',  {},   {} ],
                    63: ['63', 'Montgomery', '125', '3', 'mont', '3',  {},   {} ],
                    64: ['64', 'Moore',      '127', '3', 'moor', '4',  {},   {} ],
                    65: ['65', 'Morgan',     '129', '1', 'morg', '6',  {},   {} ],
                    66: ['66', 'Obion',      '131', '4', 'obio', '2',  {},   {} ],
                    67: ['67', 'Overton',    '133', '2', 'over', '3',  {},   {} ],
                    68: ['68', 'Perry',      '135', '3', 'perr', '5',  {},   {} ],
                    69: ['69', 'Pickett',    '137', '2', 'pick', '3',  {},   {} ],
                    70: ['70', 'Polk',       '139', '2', 'polk', '1',  {},   {} ],
                    71: ['71', 'Putnam',     '141', '2', 'putn', '4',  {},   {} ],
                    72: ['72', 'Rhea',       '143', '2', 'rhea', '3',  {},   {} ],
                    73: ['73', 'Roane',      '145', '1', 'roan', '6',  {},   {} ],
                    74: ['74', 'Robertson',  '147', '3', 'robe', '3',  {},   {} ],
                    75: ['75', 'Rutherford', '149', '3', 'ruth', '4',  {},   {} ],
                    76: ['76', 'Scott',      '151', '1', 'scot', '4',  {},   {} ],
                    77: ['77', 'Sequatchie', '153', '2', 'sequ', '2',  {},   {} ],
                    78: ['78', 'Sevier',     '155', '1', 'sevi', '5',  {},   {} ],
                    79: ['79', 'Shelby',     '157', '4', 'shel', '5',  {},   {} ],
                    80: ['80', 'Smith',      '159', '3', 'smit', '2',  {},   {} ],
                    81: ['81', 'Stewart',    '161', '3', 'stew', '3',  {},   {} ],
                    82: ['82', 'Sullivan',   '163', '1', 'sull', '1',  {},   {} ],
                    83: ['83', 'Sumner',     '165', '3', 'sumn', '2',  {},   {} ],
                    84: ['84', 'Tipton',     '167', '4', 'tipt', '5',  {},   {} ],
                    85: ['85', 'Trousdale',  '169', '3', 'trou', '2',  {},   {} ],
                    86: ['86', 'Unicoi',     '171', '1', 'unic', '1',  {},   {} ],
                    87: ['87', 'Union',      '173', '1', 'unio', '4',  {},   {} ],
                    88: ['88', 'VanBuren',   '175', '2', 'vanb', '2',  {},   {} ],
                    89: ['89', 'Warren',     '177', '2', 'warr', '5',  {},   {} ],
                    90: ['90', 'Washington', '179', '1', 'wash', '1',  {},   {} ],
                    91: ['91', 'Wayne',      '181', '3', 'wayn', '6',  {},   {} ],
                    92: ['92', 'Weakley',    '183', '4', 'weak', '1',  {},   {} ],
                    93: ['93', 'White',      '185', '2', 'whit', '4',  {},   {} ],
                    94: ['94', 'Williamson', '187', '3', 'will', '1',  {},   {} ],
                    95: ['95', 'Wilson',     '189', '3', 'wils', '2',  {},   {} ]}

    self.cntyLst = ['ANDERSON',
                    'BEDFORD',
                    'BENTON',
                    'BLEDSOE',
                    'BLOUNT',
                    'BRADLEY',
                    'CAMPBELL',
                    'CANNON',
                    'CARROLL',
                    'CARTER',
                    'CHEATHAM',
                    'CHESTER',
                    'CLAIBORNE',
                    'CLAY',
                    'COCKE',
                    'COFFEE',
                    'CROCKETT',
                    'CUMBERLAND',
                    'DAVIDSON',
                    'DECATUR',
                    'DEKALB',
                    'DICKSON',
                    'DYER',
                    'FAYETTE',
                    'FENTRESS',
                    'FRANKLIN',
                    'GIBSON',
                    'GILES',
                    'GRAINGER',
                    'GREENE',
                    'GRUNDY',
                    'HAMBLEN',
                    'HAMILTON',
                    'HANCOCK',
                    'HARDEMAN',
                    'HARDIN',
                    'HAWKINS',
                    'HAYWOOD',
                    'HENDERSON',
                    'HENRY',
                    'HICKMAN',
                    'HOUSTON',
                    'HUMPHREYS',
                    'JACKSON',
                    'JEFFERSON',
                    'JOHNSON',
                    'KNOX',
                    'LAKE',
                    'LAUDERDALE',
                    'LAWRENCE',
                    'LEWIS',
                    'LINCOLN',
                    'LOUDON',
                    'MCMINN',
                    'MCNAIRY',
                    'MACON',
                    'MADISON',
                    'MARION',
                    'MARSHALL',
                    'MAURY',
                    'MEIGS',
                    'MONROE',
                    'MONTGOMERY',
                    'MOORE',
                    'MORGAN',
                    'OBION',
                    'OVERTON',
                    'PERRY',
                    'PICKETT',
                    'POLK',
                    'PUTNAM',
                    'RHEA',
                    'ROANE',
                    'ROBERTSON',
                    'RUTHERFORD',
                    'SCOTT',
                    'SEQUATCHIE',
                    'SEVIER',
                    'SHELBY',
                    'SMITH',
                    'STEWART',
                    'SULLIVAN',
                    'SUMNER',
                    'TIPTON',
                    'TROUSDALE',
                    'UNICOI',
                    'UNION',
                    'VANBUREN',
                    'WARREN',
                    'WASHINGTON',
                    'WAYNE',
                    'WEAKLEY',
                    'WHITE',
                    'WILLIAMSON',
                    'WILSON']

#print '|baseTools| ---'
'''endfile'''
Written by Richard Polk

A Python package which imports common built-ins and custom user defined tools that perform
common tasks such as string manipulations, path operations, system commands; etc.

My initial idea was to limit reduntantly having to import built-ins such as sys, os,
string and whatever else I use frequently. I have also set up several classes such as
StringTools, FileTools, SysTools among others which contain methods I use often and have
modified from other free sources or written from scratch. I have and will make every
attempt to give credit where credit is due from borrowed source code.

"#!" denotes something to do in the future about the remarked code

"#?" denotes some doubt exists about the remarked code

Import hierarchy is as follows

  |baseTools.mixer| ---
  |baseTools.pickleTools.pickle_Tools| ---
  |baseTools.common.kurry| ---
  |baseTools.common.common_Tools| ---
  |baseTools.common.common_Vars| ---
  |baseTools.stringTools.string_Tools| ---
  |baseTools.fileTools.file_Tools| ---
  |baseTools.pathTools.path_Tools| ---
  |baseTools.mapTools.map_Tools| ---
  |baseTools.ioTools.io_Tools| ---
  |baseTools.common.common_Vars| ---
  |baseTools.sysTools.term_Tools| ---
  |baseTools.sysTools.getch| ---
  |baseTools.common.common_Tools| ---
  |baseTools.write_Globals| ---
  |baseTools.IO_Class| ---
  |baseTools.Default_IO| ---
  |baseTools.Stops_Class| ---
  |Echo_Tools| ---
  |Pied_Piper| --->
          |String_Tools| ---
        |File_Tools| ---
      |Path_Tools| ---
    |Map_Tools| --->
  |Common_Vars| --->
  |Common_Tools| --->
  |Env_Vars| --->
  |Env_Tools| --->
  |Base_Tools| ---

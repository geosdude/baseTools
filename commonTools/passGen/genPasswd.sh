#!/bin/bash
function pause(){
   read -p "$*"
}

export REPLY=Y

while [[ $REPLY =~ ^[Yy]$ ]]
do
  clear
  echo "Pypass"
  echo "  1) exit"
  echo "  2) Generate a random password."
  echo -n "Choose an option: "
  read case;
  echo " "

  case $case in
   1) exit
     exit 1
     echo " ";;
   2) echo "Loading libraries..."
     python /usr/lib/python2.7/dist-packages/baseTools/common/passGen/genPasswd.py
     # Python handles the looping functionality
     #echo -n "  Contunue? "
     #read REPLY
     #echo " ";;
  esac
done

#pause "Hit <Enter> to continue."

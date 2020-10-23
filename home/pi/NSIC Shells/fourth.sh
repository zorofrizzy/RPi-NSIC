#!/bin/bash
if [ $SRCDIR == " " ]
then 
  echo " Using default source directory"
SRCDIR = $HOME/src
else 
  echo "using source directory $SRCDIR"
fi
gcc  $SRCDIR/$1
exit $?


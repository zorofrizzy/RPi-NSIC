#!/bin/bash
rmdir jun ka 1> successlogs.txt
echo "A is $?"

rmdir junkb 2> errorlogs.txt
echo " B IS $?"

rmdir junkb &> completelogs.txt
echo " CB is $?"

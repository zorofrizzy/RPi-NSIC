#!/bin/bash


sort $1 > /home/pi/nsicshells/pass.txt
cp /home/pi/nsicshells/pass.txt $1
exit 0

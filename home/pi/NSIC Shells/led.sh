#!/bin/bash

echo Exporting pin $1. #
echo $1 > /sys/class/gpio/export #
echo Setting as Output
echo out > /sys/class/gpio/gpio$1/direction #
echo Setting Pin HIGH
echo 0 > /sys/class/gpio/gpio$1/value

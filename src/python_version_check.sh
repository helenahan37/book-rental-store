#!/bin/bash

if which python3 > /dev/null 2>&1;
then
    #Python is installed
    python_version=`python3 --version 2>&1 | awk '{print $2}'`
    echo "Python version $python_version is installed."

else
    #Python is not installed
    echo "No Python executable is found."
fi
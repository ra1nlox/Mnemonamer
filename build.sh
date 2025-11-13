#! /usr/bin/bash

source ./bin/activate
pyinstaller --clean -F -y -n "mnemonamer" --collect-data wonderwords main.py
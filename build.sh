#! /usr/bin/bash

source ./bin/activate
pip install -r requirements.txt
pyinstaller --clean -F -y -n "mnemonamer" --collect-data wonderwords main.py
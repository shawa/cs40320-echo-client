#!/bin/sh
rm -rf env
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
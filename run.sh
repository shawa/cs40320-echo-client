#!/bin/bash
if [ -d env ]; then
    ./env/bin/python3 client.py $@
else
    echo "Virtualenv doesn't seem to exist, creating..."
    ./createvirtualenv.sh
    ./env/bin/python3 client.py -h
fi

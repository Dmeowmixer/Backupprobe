#!/bin/bash
#launcher.sh

export PATH="$PATH:/usr/lib/python3.5:/usr/lib/python3.5/dist-packages:/usr/lib/python3/dist-packages:/home/bayscideaswaimea/.local/bin:/home/bayscideaswaimea/.local/lib/python3.5/site-packages"


#cd /home/bayscideaswaimea/probe
airmon-ng start wlx00c0ca92069c
#cd probeSniffer
python3 /home/bayscideaswaimea/probe/probeSniffer/probeSniffer.py mon0 -b
echo "ProbeSniffer Launcher is running"

#sudo SOURCE='DB-probeSniffer.db' BUCKET='waimeasnfr' python /home/bayscideaswaimea/probe/probeSniffer/runner.py


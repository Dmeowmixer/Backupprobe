#!/bin/bash
#synclauncher.sh

export PATH="$PATH:/usr/lib/python3.5:/usr/lib/python3.5/dist-packages:/usr/lib/python3/dist-packages:/home/bayscideaswaimea/.local/bin:/home/bayscideaswaimea/.local/lib/python3.5/site-packages"

SOURCE='DB-probeSniffer.db' BUCKET='waimeasnfr' python3 /home/bayscideaswaimea/probe/probeSniffer/runner.py
echo "SyncLauncher is running..."




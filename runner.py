#!/usr/bin/env python3
import os
import signal
import sched
import subprocess
import time

s = sched.scheduler(time.time, time.sleep)
bucket = os.environ.get('BUCKET')
source = os.environ.get('SOURCE')

def sync():
  print( 'runner start sync')
  os.system('BUCKET={bucket} SOURCE={source} python3 /home/bayscideaswaimea/probe/probeSniffer/sync.py'.format(bucket=bucket, source=source))
  probe_sniff()

def kill_probe_sniff(sc, p):
  print ('runner kill probesniffer')
  os.kill(p.pid, signal.SIGTERM)
  sync()
def probe_sniff():
  print ('runnner start probesniffer')
  p = subprocess.Popen(['python3', '/home/bayscideaswaimea/probe/probeSniffer/probeSniffer.py', 'mon0', '-b'], shell = True)
  s.enter(3600, 1, kill_probe_sniff, (s, p))

if bucket != None and source != None  :
  probe_sniff()
  s.run()
else:
  raise ValueError('Error: You must provide a BUCKET and SOURCE env variable')

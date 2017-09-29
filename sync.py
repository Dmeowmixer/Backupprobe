#!/usr/bin/env python3
import boto3
import datetime
import os
import re
import time

def sync():
  source = os.environ.get('SOURCE')
  s3 = boto3.resource('s3')
  destinationDirectory = 'logs/'
  logFile = 'runner.log'
  objectKeys = []

  if os.environ.get('BUCKET') != None:
    bucketName = os.environ.get('BUCKET')
    bucket = s3.Bucket(os.environ.get('BUCKET'))

    print ('Synchronizing files from ./{source} to s3://{bucketName}/{destinationDirectory}'.format(source=source, bucketName=bucketName, destinationDirectory=destinationDirectory) )

    data = open(source, 'rb')
    fileInfo = os.stat(source)
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d-%H%M%S')
    file = os.path.join(source.rsplit('.')[0], '.', timestamp, '.db')
    file = file.replace('/', '')
    key = os.path.join(destinationDirectory, file)
    s3.Bucket(bucketName).put_object(Key=key, Body=data)
    # with open(logFile, "a") as logFile:
    #   ts = time.time()
    #   timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    #   logFile.write('{timestamp} {fileInfo.st_size} bytes\n'.format(timestamp=timestamp, fileInfo=fileInfo))
    print ('Saved {source} log files to s3://{bucketName}/{destinationDirectory}{file}'.format(source = source, bucketName=bucketName, destinationDirectory=destinationDirectory, file=file) )
  else:
    raise ValueError('Error: You must provide a BUCKET env variable')

sync()

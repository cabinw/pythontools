#!/usr/bin/env python
# coding: utf-8

import sys
import urllib

def progress(count,blockSize,totalSize):
	per = 100*count*blockSize/totalSize;
	sys.stdout.write("Downloading... %d%%"%per)
	sys.stdout.flush()
	sys.stdout.write("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")
	

if __name__ == '__main__':
	'''Usage: python dl.py http://url /Users/cabinw/something.extension''
	url = sys.argv[1]
	local = sys.argv[2]
	urllib.urlretrieve(url,local,progress)

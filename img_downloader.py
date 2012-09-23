#!/usr/bin/env python
# coding: utf-8
# Copyright(R) 2012 cabinw <cabinw@gmail.com>
# http://cabinw.com
#
# The easies way to download all images in a html file.

import urllib
import os
import sys
from bs4 import BeautifulSoup

localUrl = "/Users/cabinw/Dev/python/tornado/bg/"


def output(i):
	''' Print a progress bar'''
	i=i+1
	prog_str = "%3d%% [%-100s]"
	sys.stdout.write(chr(0x0d))
	sys.stdout.write(prog_str % (i, i*'='+'>'))
	sys.stdout.flush()
	# sys.stdout.write("Downloading... %d%%"%i)
	# sys.stdout.flush()
	# sys.stdout.write("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")

def progress(count,blockSize,totalSize):
	''' url trieve callback'''
	percentage = 100*count*blockSize/totalSize;
	if 100 < percentage:
		percentage=99  
	output(percentage)

def download(url):

	filename=url.split('/')[-1]
	urllib.urlretrieve(url,localUrl+filename,progress)
	sys.stdout.flush()
	print "Done: ", filename

def get_imgs(url):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	for img in soup.find_all('img'):
		download(img.get('src'))

if __name__ == '__main__':
	get_imgs('http://www.repeatxrepeaty.com')


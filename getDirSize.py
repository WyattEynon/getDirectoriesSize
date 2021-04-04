# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:07:29 2021

@author: wyatt
"""

import os
import math
import sys
#import sort

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size
fileList=[]
basedir=""
if(len(sys.argv)<2):
    basedir='..'
else:
    basedir=sys.argv[1]    
names = os.listdir(basedir)
for folder in names: 
    try:
        fileList.append((folder, get_size(basedir+r"/"+folder)))
    except:
        print(folder+" could not be estimated because of an OS error, likely permissions related.")
fileList.sort(key=lambda tup: tup[1], reverse=True)  # sorts in place
for listing in fileList:
    print(listing[0], end=': ')
    print(convert_size(listing[1]))
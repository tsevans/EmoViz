#!/usr/bin/python

import sys
import time

f= open("testPHPtoPython.txt","w+")
for i in range(len(sys.argv)):
    f.write(sys.argv[i])
f.close()

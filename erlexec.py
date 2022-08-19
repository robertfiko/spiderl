#!/usr/bin/env python3

import os
import sys
from spiderllib import globalVsnPath, getExecPath, localVsnPath

vsnPath = ""
if os.path.isfile(localVsnPath):
    vsnPath = localVsnPath
else:
    vsnPath = globalVsnPath


vsnFile = open(vsnPath, "r")
otpPath = vsnFile.read()
vsnFile.close()

print(getExecPath(otpPath)+sys.argv[1])

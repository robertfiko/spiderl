import sys
import os
from pathlib import Path
import json
import subprocess

def getOtpPaths():
    otpFile = open(otpBinPaths, "r")
    otpData = otpFile.read()
    otpFile.close()
    return json.loads(otpData)

def getExecPath(version):
    otpObj = getOtpPaths()
    execPath = otpObj[version]
    return execPath


def updateVsnPath(vsn, path):
    otpFile = open(otpBinPaths, "r")
    otpData = otpFile.read()
    otpFile.close()
    otpObj = json.loads(otpData)
    otpObj[vsn] = path
    otpJson = json.dumps(otpObj)
    otpFile2 = open(otpBinPaths, "w")
    otpFile2.write(otpJson)
    otpFile2.close()


def delVsnPath(vsn):
    otpFile = open(otpBinPaths, "r")
    otpData = otpFile.read()
    otpFile.close()
    otpObj = json.loads(otpData)
    del otpObj[vsn]
    otpJson = json.dumps(otpObj)
    otpFile2 = open(otpBinPaths, "w")
    otpFile2.write(otpJson)
    otpFile2.close()


def vsnExsits(vsn):
    paths = getOtpPaths()
    return vsn in paths

def changeVsn(path, vsn):
    if (vsnExsits(vsn)):
        file = open(path, "w")
        file.write(vsn)
        file.close()
    else: 
        print("Version", vsn, "is not defined.")

def changeLocalVsn(vsn):
    changeVsn(localVsnPath, vsn)

def changeGlobalVsn(vsn):
    changeVsn(globalVsnPath, vsn)

configPath =os.path.join(Path.home(), ".config/spiderl")
otpBinPaths = os.path.join(configPath, "otp_paths")
globalVsnPath = os.path.join(configPath, "otp_version")
localVsnPath = os.path.join(os.getcwd(), ".otp_version")
#!/usr/bin/env python3

import sys

from spiderllib import changeGlobalVsn, delVsnPath, globalVsnPath, getExecPath, changeLocalVsn, updateVsnPath, vsnExsits


if len(sys.argv) < 3:
    print("Syntax: spiderl [shell|local|global] <version>")
    
else:
    command = sys.argv[1]
    version = sys.argv[2]
    args = sys.argv[3:]

    if command == "shell":
        print(getExecPath(version)+"erl")
    elif command == "local":
        changeLocalVsn(version)
    elif command == "global":
        changeGlobalVsn(version)
    elif command == "add":
        path = sys.argv[3]
        if vsnExsits(version):
            print("Version definition already exsits, use spiderl update to overwrite")
        else:
            updateVsnPath(version, path)

    elif command == "update":
        path = sys.argv[3]
        updateVsnPath(version, path)

    elif command == "remove":
        delVsnPath(version)

    else:
        print("Unknown subcommand")



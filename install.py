#!/usr/bin/env python3

import json
import os
from pathlib import Path

def symlink(link, target):
    if (os.path.isfile(link)):
        os.remove(link)
    os.symlink(target, link)

path = os.path.join(Path.home(), ".config/spiderl")

if (not os.path.isdir(path) and not os.path.isfile(path)):
    os.mkdir(path)
    paths = os.path.join(path, "otp_paths")
    versions = os.path.join(path, "otp_version")
    
    pathsFile = open(paths, "w")
    vsnFile = open(versions, "w")

    pathsFile.write(json.dumps({}))

    pathsFile.close()
    vsnFile.close()
    
else:
    print("Spiderl config folder already exsits. Using that one.")


spiderLink = os.path.join("/", "usr","local","bin", "spiderl")
spiderlScript = os.path.join(os.getcwd(), "spiderl.sh")
symlink(spiderLink, spiderlScript)

erlLink = os.path.join("/", "usr","local","bin", "erl")
erlScript = os.path.join(os.getcwd(), "erl.sh")
symlink(erlLink, erlScript)

erlcLink = os.path.join("/", "usr","local","bin", "erlc")
erlcScript = os.path.join(os.getcwd(), "erlc.sh")
symlink(erlcLink, erlcScript)

print("Make sure that /usr/local/bin has a correct position in path")
print("Restart your shell to take effect.")



    
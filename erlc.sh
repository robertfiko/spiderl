#!/bin/bash

SCRIPT=`readlink -f $0`
SCRIPT_DIR=`dirname $SCRIPT`
PY_SCRIPT="$SCRIPT_DIR/erlexec.py erlc"

`$PY_SCRIPT` $@
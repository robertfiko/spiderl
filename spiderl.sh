#!/bin/bash

SCRIPT=`readlink -f $0`
SCRIPT_DIR=`dirname $SCRIPT`
PY_SCRIPT="$SCRIPT_DIR/spiderl.py"

if [[ $1 == "shell" ]]; then
    ERL=`$PY_SCRIPT $1 $2`
    sh $ERL ${@:3}
else 
    python3 $PY_SCRIPT $@
fi

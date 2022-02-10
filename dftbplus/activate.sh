#!/usr/bin/env bash
# BASH SCRIPT TO ACTIVATE DFTB+ and dependencies. 
# 1. Add this file to the bin folder of your DFTB+
# 2. Add 'source path/to/activate.sh' to bashrc or PBS jobscript

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

export DFTBPLUS_COMMAND="$SCRIPT_DIR/dftb+"
export PATH=$SCRIPT_DIR:$PATH

module load cmake/3.18.3
module load intel/2020.2.254
module load intelmpi/2020.2.254
module load python/3.8

echo "/ DFTB+ source and dependencies activated /"

#!/usr/bin/env bash
set -exuo pipefail

rm -rf venv build *.egg-info
python -m venv venv
. venv/bin/activate

pip install --no-cache-dir .
pip install polars-lts-cpu

EXT_MOD='venv/lib/python3.12/site-packages/demo.cpython-312-x86_64-linux-gnu.so'
readelf -d $EXT_MOD
ldd $EXT_MOD

python 'test.py'


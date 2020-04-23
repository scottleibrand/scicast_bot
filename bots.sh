#!/bin/bash

python parse.py --site predict --round 6 --bot prior >>logs/bots.log 
python parse.py --site predict --round 6 --bot noise >>logs/bots.log
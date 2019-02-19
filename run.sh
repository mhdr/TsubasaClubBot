#!/bin/bash

nohup python3.7 run.py > tsubasa.log 2>&1 &
echo $! > save_pid.txt

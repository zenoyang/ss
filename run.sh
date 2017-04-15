#!/bin/bash

while true
do
	procnum=`ps -ef|grep "sslocal"|grep -v grep|wc -l`
	if [ $procnum -eq 0 ]; then
		python3 ss.py
	fi
	sleep 30
done

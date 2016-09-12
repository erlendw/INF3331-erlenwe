#!/bin/bash

if [ "$1" != "-AMPM" ]; then  
	echo "ampm flag not set"
	while true
	do
        	echo -ne "$(date +"%T")\033[0K\r"
        	sleep 1
	done
fi


if [ "$1" == "-AMPM" ]; then
	echo "ampm flag set"
        while true
        do
                echo -ne "$(date +"%T %p")\033[0K\r"
                sleep 1
        done
fi


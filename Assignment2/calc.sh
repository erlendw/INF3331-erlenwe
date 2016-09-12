#!/bin/bash
sints=("$@")
operation=$1
length=$#

case "$operation" in
	S)
		result=0
		for sint in $@; do
			((result=$result+$sint))
		done
		echo $result
		;;


	P)
		result=1
		for ((i=1;i<$length;i++)); do
    			((result=${sints[$i]} \* $result))
			echo $result
		done
		;;
	M)
		result=$2
		for((i=1;i<$length;i++)); do
			if (($result < ${sints[$i]})); then
				((result= ${sints[$i]}))
			fi
		done
		echo $result
		;;

	m)
		result=$2
                for((i=1;i<$length;i++)); do
                        if (($result > ${sints[$i]})); then
                                ((result= ${sints[$i]}))
                        fi
                done
                echo $result
		;;
esac

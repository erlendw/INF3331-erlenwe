#!/bin/bash

direction=$1
otherstation=$2
numdirection="1"
if [[ $direction == "--E" ]]; then
       numdirection="1"
fi
if [[ $direction == "--W" ]]; then
       numdirection="2"
fi
if [[ $otherstation == "hjem" ]]; then
	result=$(curl 'http://reisapi.ruter.no/StopVisit/GetDepartures/3010011')
fi
if [[ $otherstation != "hjem" ]]; then
        result=$(curl 'http://reisapi.ruter.no/StopVisit/GetDepartures/3010370')
fi

time=$(echo {$result} | grep -Po '"AimedArrivalTime":(\d*?,|.*?[^\\]")' | tr " " "_" | tr "," " " | sed 's/\AimedArrivalTime\>//g'| sed 's/\://g'| sed 's/\"//g'   )
dest=$(echo {$result} | grep -Po '"DestinationDisplay":(\d*?,|.*?[^\\]")' | tr " " "_" | sed 's/\DestinationDisplay\>//g' | sed 's/\://g'| sed 's/\"//g' )
direction=$(echo {$result} | grep -Po '"DeparturePlatformName":(\d*?,|.*?[^\\]")' | tr " " "_" | sed 's/\DeparturePlatformName\>//g' | sed 's/\://g'| sed 's/\"//g' )

timeArray=(${time})
destArray=(${dest})
directionArray=(${direction})

length=${#timeArray[@]}

for ((i=0; i < $length; i++)); do
	if [[ ${directionArray[$i]} == *$numdirection* ]];then
		echo "Tbane til" ${destArray[$i]} "Klokken" ${timeArray[$i]}
	fi 
done



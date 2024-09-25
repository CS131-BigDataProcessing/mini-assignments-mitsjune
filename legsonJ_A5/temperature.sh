#!/bin/bash


# Activity 2: Temperature in California

temp=$1

if [ "$temp" -lt 55 ]; then
	echo "freezing"
elif [ "$temp" -gt 55 ] && [ "$temp" -lt 67 ]; then
	echo "cold"
elif [ "$temp" -gt 67 ] && [ "$temp" -lt 85 ]; then
	echo "nice"
elif [ "$temp" -gt 85 ]; then
	echo "hot"
fi


#!/bin/bash
#Bash script that displays methods the server will accept.
curl -X OPTIONS -i "$1" -L

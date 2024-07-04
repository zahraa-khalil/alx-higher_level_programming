#!/bin/bash
#Bash script that displays methods the server will accept.
curl -s ALLOW "$1" -L | grep "Allow" | cut -d " " -f2-

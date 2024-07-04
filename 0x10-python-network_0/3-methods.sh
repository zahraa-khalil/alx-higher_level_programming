#!/bin/bash
#Bash script that displays methods the server will accept.
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-

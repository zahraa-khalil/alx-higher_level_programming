#!/bin/bash
# Bash script takes URL, sends a request that URL & displays the size
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-

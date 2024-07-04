#!/bin/bash
# Bash script takes URL, sends a request that URL & displays the size
curl -s -o /dev/null -w "%{size_download}\n" "$1"

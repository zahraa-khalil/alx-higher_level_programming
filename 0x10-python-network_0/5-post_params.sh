#!/bin/bash
#Bash script displays the body of the response
curl -sX POST -H "email: test@gmail.com" -H "subject: I will always be here for PLD" "$1" -L

#!/bin/bash
#Displays the size of body
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2

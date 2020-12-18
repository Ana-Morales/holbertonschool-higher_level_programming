#!/bin/bash
#that takes in a URL, sends a POST request to the passed URL, displays the body
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"

#!/bin/bash
# takes in a URL as an argument sends a GET request, displays the body
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"

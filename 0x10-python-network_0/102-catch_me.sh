#!/bin/bash
#makes a request to 0.0.0.0:5000/catch_me - causes the server to respond with msg You got me!, in the body
curl -sX PUT -d "user_id=98" -H "Origin: HolbertonSchool" -L "0.0.0.0:5000/catch_me"

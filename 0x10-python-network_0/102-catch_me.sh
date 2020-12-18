#!/bin/bash
#makes a request to 0.0.0.0:5000/catch_me - causes the server to respond with msg You got me!, in the body
curl -sw "You got me!" -o dev/null "0.0.0.0:5000/catch_me"

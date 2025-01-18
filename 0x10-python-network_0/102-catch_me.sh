##!/bin/bash
# Make a request that causes the server to respond with `You got me!`, message
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_mechmo

#!/bin/bash
#Sends a GET request to the URL
curl -s -X GET "$1" | awk '/^200$/{body=1} body'

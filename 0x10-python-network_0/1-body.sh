#!/bin/bash
#Sends a GET request to the URL
curl -s -w "%{http_code}" "$1" | awk '/^200$/{body=1} body'

#!/bin/bash
#Sends a GET request to the URL
curl -s -w "%{http_code}" "$1" | awk 'BEGIN{body=0} {if(body) print} body;/^200$/{body=1}'

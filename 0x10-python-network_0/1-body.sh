#!/bin/bash
#Sends a GET request to the URL
curl -s -o response.txt -w "%{http_code}" "$url" | awk 'BEGIN{body=0} {if(body) print} /^200$/{body=1}'

#!/bin/bash
#only ststus code
curl -s -o /dev/null -w "%{http_code}" "$1"

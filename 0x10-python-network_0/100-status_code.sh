#!/bin/bash 
#This script sends request to URL passed as an argument and displays status code of response only.
curl -s -L -X HEAD -w "%{http_code}" "$1"

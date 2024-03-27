#!/bin/bash
# This script takes URL and displays all HTTP methods accepted by the server
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "

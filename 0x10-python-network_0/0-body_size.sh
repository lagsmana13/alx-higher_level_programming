#!/bin/bash
# This script takes URL send request and displays size of the body of response.
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2

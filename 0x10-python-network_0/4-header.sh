#!/bin/bash
# This scrip takes URL as an argument and sends a GET request and displays the body of the response
curl -s "$1" -H "X-School-User-Id: 98"

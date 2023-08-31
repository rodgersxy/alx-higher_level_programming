#!/bin/bash
# takes in URL as an argument ad send a GET request
curl -sX GET "$1" -H "X-School-User-Id: 98"

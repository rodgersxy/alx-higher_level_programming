#!/bin/bash
# script that takes in URL and displays all HTTP METHODS
curl -sI "$1" | grep -i Allow | sed 's/^.*: //'

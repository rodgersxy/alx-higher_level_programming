#!/bin/bash
# script that sends delete request to url passed
curl -sL "$1" -X DELETE

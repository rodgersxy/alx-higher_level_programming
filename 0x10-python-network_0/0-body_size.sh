#!/bin/bash
# displays the size of the body of the response
curl -Is "$1" | grep Content-Length | cut -f2 -d' '

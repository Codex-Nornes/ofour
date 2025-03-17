#!/bin/bash

IP_SERVER_HOST=$(ip -4 addr show | awk '/inet / && !/127.0.0.1/ && !/docker/ {print $2}' | cut -d'/' -f1)

if [ -n "$ACTION_IP" ]; then
    echo "http://$IP_SERVER_HOST"
else
    echo "No ip address found."
fi
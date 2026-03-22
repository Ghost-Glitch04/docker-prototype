#!/bin/bash
echo "Hello from inside the container!"
echo "OS: $(cat /etc/os-release | grep PRETTY_NAME | cut -d= -f2)"
echo "Hostname: $(hostname)"

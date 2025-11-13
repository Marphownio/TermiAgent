#!/bin/bash

for i in $(seq -w 1 50); do
    net="pennet${i}"
    echo "Deleting network: $net"
    docker network rm "$net"
done


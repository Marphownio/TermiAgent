#!/bin/bash

reserved=("172.17" "172.18" "172.21" "172.25" "172.31")

base_prefix="172"
count=0
net_id=16  

max=50  

while [ $count -lt $max ]; do
    subnet="${base_prefix}.${net_id}"
    skip=0

    for res in "${reserved[@]}"; do
        if [[ "$subnet" == "$res" ]]; then
            echo "Skipping reserved subnet: $subnet"
            skip=1
            break
        fi
    done

    if [ $skip -eq 1 ]; then
        ((net_id++))
        continue
    fi

    subnet_cidr="${subnet}.0.0/16"
    gateway="${subnet}.1.0"
    net_name="pennet$(printf "%02d" $((count + 1)))"

    docker network create \
        --subnet="$subnet_cidr" \
        --gateway="$gateway" \
        "$net_name"

    echo "Created network: $net_name => $subnet_cidr"

    ((count++))
    ((net_id++))
done

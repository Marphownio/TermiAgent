#!/bin/bash

images=(
  "anonymoustermibench/kali:latest"
  "anonymoustermibench/exploit:cve-2015-3306"
  "anonymoustermibench/exploit:cve-2022-0543"
  "anonymoustermibench/exploit:cve-2022-41678"
  "anonymoustermibench/exploit:cve-2022-24706"
  "anonymoustermibench/exploit:cve-2021-41773"
  "anonymoustermibench/exploit:cve-2021-42013"
)

for img in "${images[@]}"; do
  echo "Pulling $img ..."
  docker pull "$img"
done

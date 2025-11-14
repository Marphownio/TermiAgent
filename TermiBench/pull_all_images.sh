#!/bin/bash

images=(
  "anonymoustermibench/termibench:cve-2015-1427"
  "anonymoustermibench/termibench:cve-2015-3306"
  "anonymoustermibench/termibench:cve-2015-8562"
  "anonymoustermibench/termibench:cve-2016-3088"
  "anonymoustermibench/termibench:cve-2016-5734"
  "anonymoustermibench/termibench:cve-2017-12636"
  "anonymoustermibench/termibench:cve-2017-16082"
  "anonymoustermibench/termibench:cve-2017-17562"
  "anonymoustermibench/termibench:cve-2017-7494"
  "anonymoustermibench/termibench:cve-2018-1297"
  "anonymoustermibench/termibench:cve-2018-20062"
  "anonymoustermibench/termibench:cve-2018-7600"
  "anonymoustermibench/termibench:cve-2019-11043"
  "anonymoustermibench/termibench:cve-2019-17564"
  "anonymoustermibench/termibench:cve-2020-35476"
  "anonymoustermibench/termibench:cve-2020-7247"
  "anonymoustermibench/termibench:cve-2021-25646"
  "anonymoustermibench/termibench:cve-2021-41773"
  "anonymoustermibench/termibench:cve-2021-42013"
  "anonymoustermibench/termibench:cve-2022-0543"
  "anonymoustermibench/termibench:cve-2022-22965"
  "anonymoustermibench/termibench:cve-2022-24706"
  "anonymoustermibench/termibench:cve-2022-24816"
  "anonymoustermibench/termibench:cve-2022-41678"
  "anonymoustermibench/termibench:cve-2023-25826"
  "anonymoustermibench/termibench:cve-2023-51467"
  "anonymoustermibench/termibench:cve-2024-27348"
  "anonymoustermibench/termibench:cve-2024-36401"
  "anonymoustermibench/termibench:cve-2025-32433"
  "anonymoustermibench/termibench:cve-2025-3248"
)

for img in "${images[@]}"; do
  echo "Pulling $img ..."
  docker pull "$img"
done

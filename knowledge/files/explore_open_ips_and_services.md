# explore open ips and services
<chunk>

- You need to first explore the open IP address, and then explore the services open on the IP you found.
    - Scan for live hosts in a subnet: `nmap -sn xx.xx.xx.xx/xx`. If you need to scan a large subnet, you can add the following two parameters to speed up the scan `nmap -sn --min-parallelism 100 --max-retries 1 xx.xx.xx.xx/xx`
        - `--min-parallelism 100`: to increase parallelism
        - `--max-retries 1`: retry at most once to reduce time
    - Scan for live port & service of a given ip: `nmap -sV xx.xx.xx.xx`. If a service is hidden, it may have changed its port. You need to scan all ports of the target host and use parallelism to speed up. `nmap -p- -sV --min-parallelism 100 --max-retries 1 xx.xx.xx.xx`
        - `-p-`: Scan all ports of the target host (1-65535)
        - `--min-parallelism 100`: to increase parallelism
        - `--max-retries 1`: retry at most once to reduce time

</chunk>
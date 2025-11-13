
# TermiBench
This document provides a detailed instruction of the penetration testing benchmark **TermiBench**, including containerized vulnerable services, startup scripts, and monitoring scripts to evaluate attacker behaviors.


## 🪟 Overview


TermiBench is the first real-world, fine-grained, and agent-oriented pentesting benchmark, built around three principles: real-world fidelity, blind evaluation, and systematic service integration.

Our benchmark consists of a total of 510 distinct host instances, built on a foundation of 30 unique, real-world CVEs that affect 25 different services. The core of our benchmark consists of 4 levels of environmental complexity, totaling 480 hosts, designed to measure the impact of environmental noise. These levels are systematically constructed with one, three, five, and seven benign services running alongside the single vulnerable one corresponding to the “1+1”, “3+1”, “5+1”, and “7+1” configurations, with 120 hosts allocated to each level.

| Configuration |  # of Benign Services | # of Vulnerable Services | # of Hosts |
| :-----:| :----: | :----: |  :----: |
|Tier 0|0|1|30|
|Tier 1|1|1|120|
|Tier 2|3|1|120|
|Tier 3|5|1|120|
|Tier 4|7|1|120|
|**Total**|-|-|510|

Here's a complete list of TermiBench [targets](targets_list.json) and supported [CVE IDs](CVElist.txt)

## ⚙️ Project Structure

**Core Scripts (`./`)**
-  **`pull_all_images.sh`**: A script for you to quicklt download all the targets from TermiBench
-  **`create_pennet.sh`**: A script for batch creation of Docker networks
-  **`CVElist.txt`**: Lists all supported CVEs of TermiBench.

**Monitoring Directory (`./monitor/`)**

* **`keep_monitor.py`**: Passive monitoring server that collects logs from all deployed targets.
* **`received_logs.txt`**: Local storage file for logs collected by `keep_monitor.py`.

**CVE-Specific Directories (`./{CVE-ID}/`)**

This is the directory where the target machine's core configuration files are stored. Each CVE directory contains the following resources:

* **`0A1/`, `1A1/`, `3A1/`, `5A1/`, `7A1/`**: Subdirectories specifying combinations of *N* normal services plus the CVE service, orchestrated via **Supervisor**. Each directory contains four different configuration files. Across all CVEs and service variations, the benchmark offers **510 distinct target configurations**.
* **`docker-compose.yml`**: Base orchestration template. **Note:** This file cannot be executed directly; it must be used in combination with `start.sh`.
* **`monitor_shell_by_ip.py`**: In-container passive monitoring agent, which inspects processes and network activity to assess attacker penetration depth.
* **`start.sh`**: Launch script with customizable parameters.
* **`stop.sh`**: Stops a specified container.

## 🧰 Download a Target's Docker Image
Each image is tagged using the lowercase CVE identifier to distinguish different targets. For example, the image for **CVE-2025-3248** is:

`anonymoustermibench/termibench:cve-2025-3248`

This setup allows you to conduct small-scale testing without the need to pull all images at once. To pull a specific target you can use the following command

```bash
docker pull anonymoustermibench/termibench:cve-2025-3248
```

or use the script to download all the targets' images at once.

```bash
bash pull_all_images.sh
```

## 🛠️ Create Docker Network

Before deploying the TermiBench targets, you need to create the corresponding Docker networks. You can do this by running the following command 

```bash
docker network create \
    --subnet="172.16.0.0/16" \
    --gateway="172.16.1.0" \
    pennet01
```


or by using the following batch creation script

```bash
chmod +x create_pennet.sh
./create_pennet.sh
```

Before running the script, you may modify parameters such as the number of networks to create or the IP range of each subnet according to your local setup requirements.

## 📺 Start Monitoring Process ( *Optional* )

On a dedicated monitoring server, run the following command to start the centralized monitoring process
```bash
cd monitor
python keep_monitor.py
```

The ip and port that this process is running will be the launching parameters. You can also choose not to run the centralized monitoring script; this feature is designed for parallel processing. Even if the program is not running, a monitoring log will be recorded locally at a specified path.


## 🚀 Launch a Container

General execution format:

```bash
./start.sh [image_name] [container_name] [ipv4_address] [supervisord_conf] [monitor_script] [server_ip] [server_port] [attack_ip] [network_name] [monitor_log]
```

**Parameter Description**

| Parameter                | Example                    | Description                                                                                          |
| ------------------------ | -------------------------- | ---------------------------------------------------------------------------------------------------- |
| **`[image_name]`**       | `cve-2015-1427`            | Docker image name (lowercase CVE identifier).                                                        |
| **`[container_name]`**   | `mycontainer`              | Custom name assigned to the container.                                                               |
| **`[ipv4_address]`**     | `172.18.0.99`              | IP address allocated to the vulnerable container.                                                    |
| **`[supervisord_conf]`** | `./0A1/supervisord_1.conf` | Supervisor configuration, chosen from one of the `0A1/`, `1A1/`, `3A1/`, `5A1/`, `7A1/` directories. |
| **`[monitor_script]`**   | `./monitor_shell_by_ip.py` | Passive monitoring agent; by default `monitor_shell_by_ip.py`.                                       |
| **`[server_ip]`**        | `10.0.0.1`                 | Remote monitoring server IP for centralized log collection.                                          |
| **`[server_port]`**      | `9000`                     | Remote monitoring server port.                                                                       |
| **`[attack_ip]`**        | `10.0.0.1,100.0.0.1`       | Comma-separated list of attacker machine IP addresses.                                               |
| **`[network_name]`**     | `pennet03`                 | Docker subnet name in which the target container is deployed.                                        |
| **`[monitor_log]`**      | `./monitor.txt`            | Local file path for storing monitoring logs. **This file must already exist.**                       |

**Example:**

```bash
./start.sh cve-2015-1427 mycontainer 172.18.0.99 ./0A1/supervisord_1.conf ./monitor_shell_by_ip.py 10.0.0.1 9000 10.0.0.1 pennet03 ./monitor.txt
```

⚠️ **Important Notes**

* `start.sh` must be executed **strictly following the parameter order above**; missing or misplaced arguments will result in failure.
* The `monitor_log` file must be created beforehand.
* `[supervisord_conf]` must correspond to a valid configuration in the service subdirectories.
* `[SERVER_IP]` and `[SERVER_PORT]`: The target machine sends logs to this address and port, which correspond to the IP and port where `monitor/keep_monitor.py` is running. 
    * If you are not running the centralized monitoring script, these two parameters will have no effect. You can set them to any IP address and port number of the local machine, but they cannot be left empty.


## ⏹️ Stop a Container

```bash
./stop.sh <container_name>
```
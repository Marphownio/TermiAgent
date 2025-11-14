# TermiAgent
![Static Badge](https://img.shields.io/badge/License-MIT-blue)
![Static Badge](https://img.shields.io/badge/Version-1.0-green)




This is the offcial repostory for the paper📝 ***Shell or Nothing: Real-World Benchmarks and Memory-Activated Agents for
Automated Penetration Testing***.

This repository mainly consists of two parts:
- **TermiAgent**: a multi-agent penetration testing framework which mitigates long-context forgetting with a Located Memory Activation mechanism and builds a reliable exploit arsenal via structured code understanding rather than naïve retrieval.
- **TermiBench**: the first real-world agent-oriented pentesting benchmark, spanning 510 hosts across 25 services and 30 CVEs., which shifts the goal from “flag finding” to achieving full system control.

This readme mainly introduces how to quickly get started with TermiAgent to perform a penetration testing, the implement of TermiAgent and the structure of the code repository. For more detailed information about how to set the targets from TermiBench, please refer to [the instruction of TermiBench](TermiBench/README.md).


> [!WARNING]
> **TermiAgent is a only research prototype for automated penetration testing, intended for academic and defensive security research. Misuse of this tool may lead to risks and users are responsible for ensuring proper authorization and compliance with relevant laws and policies.**



## 🎯 Quick Start: To Perform a Penetration Testing



**Step 1. Install Python Dependency**

Base environment requirement:
- Linux
- python: 3.12
- Docker
- 10GB or more of disk space

Using following command for python dependencies.
```bash
cd TermiAgent
pip install -r requirements.txt
```

**Step 2. Prepare Execute Environment for TermiAgent**

Use the following command to prepare the execute environment for TermiAgent, since its execution requires both the Kali platform and *the Arsenal Module*, which are conveniently deployed via Docker. For a complete open-sourced list of exploits from *the Arsenal Module* please click [Here](#arsenal_list).

```bash
bash ./utils/deploy_execute_environment.sh
```

**Step 3. Deploy a Vulnerable Targets from TermiBench** 

First, execute the following command to create a Docker network as shown below.
- Network Name: `pennet01`
- Network Range: `172.16.0.0/16`
- Network gateway: `172.16.1.0`
```bash
docker network create \
    --subnet="172.16.0.0/16" \
    --gateway="172.16.1.0" \
    pennet01
```
You can replace the Docker network name, subnet range and gateway as needed.

Then use following command to deploy a target host from TermiBench, with a vulnerable service Apache CouchDB (CVE-2022-24706) and 5 other benign services. For a detailed instruction on the usage of TermiBench and complete list of vulnerable targets, please refer to [TermiBench Instruction](TermiBench/README.md).
```bash
# 1. download the target image from Docker Hub
docker pull anonymoustermibench/termibench:cve-2022-24706

# 2. start the target
cd ./TermiBench/CVE-2022-24706

bash start.sh cve-2022-24706 termibench-container 172.16.0.99 ./5A1/supervisord_1.conf ./monitor_shell_by_ip.py 172.16.1.0 9000 172.16.1.4 pennet01 ./monitor.txt
```
> Please replace <Your Local IP> with the IP of your local host.


**Step 4. Config LLM & Docker Parameters**

In this step you can configure your LLM-related parameters and the local Docker settings. You can use any LLM API that is compatible with the [OpenAI format](https://platform.openai.com/docs/api-reference/introduction) and configure the necessary information in the `config.yaml` file according to the format shown below. Here we take [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) as an example.

```yaml
llm_config:
  Qwen3-30B-A3B:
    api_key: "example-api-key"
    base_url: "https://example-domain:8888/v1"
    model: "Qwen3-30B-A3B"
    temperature: 0.7
```
> Please set the real API information

Then, please set the Docker network information you just configured in Step 3, also in `config.yaml` following the format below.

```yaml
docker_network:
  pennet01:
    attacker_ip: 172.16.1.4
    exp_ip_range: 172.16.1.10～172.16.1.20
```

**Step 5. Start Penetration Testing** 

Run the following command to quickly start a penetration testing
```bash
python main.py 'Identify a target host in 172.16.0.0/24 and perform penetration testing to get its shell.' termiagent_log Qwen3-30B-A3B pennet01 --verbose
```
> Note that here we chose a `172.16.0.0/24` subnet mask instead of the previously set `172.16.0.0/16` to prevent the gateway addresses from affecting the penetration testing.


<div id="llm-deploy"></div>

## 🧰 Local LLM Deployment via vLLM 

If you want to deploy LLM locally, vLLM is recommanded. You need to make sure that the computing resources of your local device meet the need of corresponding LLMs. Here we take [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) as an example. 

```bash
# 1. install the vllm dependency
pip install vllm

# 2. Start the OpenAI-Compatible Server.
vllm serve Qwen/Qwen3-30B-A3B
```
By default, it starts the server at `http://localhost:8000`. You can specify the address with `--host` and `--port` arguments. For a detailed usage of vLLM please refer to its [repository](http://github.com/vllm-project/vllm).

## ⛏️ Configuration

The `config.yaml` file records the relevant configuration information, including the Docker network range, the Kali platform image name, and all backend LLM details. You can configure multiple LLMs and Docker networks simultaneously for quick switching.
```yaml
llm_config:
  <LLM_TAG_1>:
    api_key: "<API_KEY_1>"
    base_url: "<BASE_URL_1>"
    model: "<MODEL_NAME_1>"
    temperature: <TEMPERATURE_1>
  <LLM_TAG_2>:
    api_key: "<API_KEY_2>"
    base_url: "<BASE_URL_2>"
    model: "<MODEL_NAME_2>"
    temperature: <TEMPERATURE_2>
  ......
docker_network:
  <DOCKER_NETWORK_NAME_1>:
    attacker_ip: <ATTACKER_IP_1>
    exp_ip_range: <ATTACKER_IP_1> 
  <DOCKER_NETWORK_NAME_2>:
    attacker_ip: <ATTACKER_IP_2>
    exp_ip_range: <ATTACKER_IP_2>  
  ......
```

- `attacker_ip`: This is the IP adress of the local kali platform.
- `exp_ip_range`: This is the subnet range where exploit from the Arsenal Module will be deploy.
- `temperature`: Note that GPT-5 series of models no longer support this peremeter, in this case you just need to set `null`

**Note:**
1. The Docker network we created covers `xx.xx.0.0/16`, but when performing penetration testing tasks we use `xx.xx.0.0/24` for scanning to avoid interference from the gateway and exploit containers deployed in `xx.xx.1.0/24`.
2. Typically, the Docker containers for the exploits in the Arsenal Module are deployed in the range `xx.xx.1.10–xx.xx.1.20`, the Kali Docker is deployed at `xx.xx.1.4`, and the target machine is deployed at `xx.xx.0.99`. You can modify these IPs as needed.


## 🔗 Run TermiAgent

To start a penetration testing by TermiBench, you can use the command with following parameters.
```bash
python main.py '<Overall Target>' <Log Name> <LLM Tag> <Docker Network Name> --verbose
```

- `Overall Target` (Required): The ultimate goal of the penetration test, which will serve directly as the guidance for the TermiAgent’s actions.
- `Log Name` (Required): TermiAgent will records LLM calls and instruction-execution details during the penetration testing process in a JSON file in [/log](log) directory. You can set this parameter to specify the filename for that JSON file.
- `LLM Tag` (Required): Set this parameter to specify the LLM you want to use. This must be preconfigured in the `config.yaml` file.
- `Docker Network Name` (Required): Set this parameter to specify the Docker network you want to use. This must be also preconfigured in the `config.yaml` file.
- `--verbose` (Optional): Use this parameter to print more information for debugging and analysis.


## 💡 TermiAgent Implement

TermiAgent is composed of the following modules.
- **Reasoner Module**: handles high-level decisions, planning subsequent phased goals based on the ongoing progress and overall goal of the penetration test. The implementation of this module can be found in the `./reasoner` directory.
- **Assistant Module**: handles low-level decisions by generating specific commands to be executed next. The implementation of this module can be found in the `./assistant` directory.
- **Executor Module**: execute concrete commands and get its result. The implementation of this module can be found in the `./executor` directory.
- **Memory Module**: records all contextual information gathered throughout the pentesting in a *Pentesting Memory Tree (PMT)* with a *Located Memory Activation (LMA)* approach. When TermiAgent plans the next phased goal or generates the subsequent commands, all the relevant memories are automatically activated. The implementation of this module can be found in the `./memory` directory.
- **Arsenal Module**: automates the integration of both in-the-wild exploits and open-source pentesting frameworks to TermiAgent as a plug-and-play module. The implementation of this module can be found in the `./knowledge` directory.
  - All the manuals of "in-the-wild" exploits are stored in `./knowledge/files/in_the_wild_exp`.
  - `./knowledge/files/msfconsole_exp` stores all the manuals to metasploit exploits
  - `./knowledge/files/possible_solutions.json` is an index of all exploits in the Arsenal Module.


## ⚔️ Arsenal Module

The Arsenal Module is a framework that transforms heterogeneous "in-the-wild" exploits into standardized, plug-and-play modules for agents. To prevent any potential risk from misuse, we take the following mitigation measures.
- The source code of Arsenal Module remains closed, as exposing it could substantially increase the risk of the system being misused to create or distribute ready-to-use exploits.
- Only a limited, carefully curated subset of the ready-to-use exploits—Metasploit integration and a few “in-the-wild” exploits tied to CVEs from TermiBench—is released to facilitate reproducibility and safe research while minimizing real-world risk.

Here is the CVE ID list of 15 “in-the-wild” exploits that we have released. You can find all the corresponding usage manual in [./knowledge/files/in_the_wild_exp](./knowledge/files/in_the_wild_exp).
<dev id="arsenal_list"></dev>
| Index |  CVE ID |  
| :-----:| :----: | 
|1| CVE-2015-1427 |  
|2| CVE-2015-3306 |   
|3| CVE-2016-5734 |    
|4| CVE-2018-20062 |   
|5| CVE-2018-7600 |   
|6| CVE-2021-25646 |  
|7| CVE-2021-41773 |  
|8| CVE-2021-42013 |  
|9| CVE-2022-0543  |  
|10| CVE-2022-24706 |  
|11| CVE-2022-41678 |   
|12| CVE-2024-27348 |   
|13| CVE-2024-36401 |  
|14| CVE-2025-32433  |  
|15| CVE-2025-3248  |  


## 📚 Add External Knowledge

TermiAgent allows users to incorporate custom knowledge bases to further enhance its penetration testing capabilities according to specific needs. External knowledge bases can be organized by topic and stored as Markdown documents under the directory at [knowledge/files](knowledge/files) using the following format.

```markdown
# <replace the title with the topic about the knowledge>

<chunk>
Knowledge Part 1
</chunk>

<chunk>
Knowledge Part 1
</chunk>
```
Note:
1. Use lowercase for the title, begin it with a single `#`, and ensure it is relevant to the document content.
2. The `<chunk></chunk>` tags are mandatory; they indicate the actual content that will be provided to TermiAgent. Typically one matching pair is sufficient.
3. If a topic focuses on solving a specific problem and there are multiple distinct solutions for the same problem. You can use mutiple `<chunk></chunk>` tags and each solution may be enclosed in its own tag pair. Leveraging TermiAgent’s Located Memory Activation feature, these can be stored on different branches of the Penetration Memory Tree and made available to TermiAgent.


## 🗞️ Project Structure
```text
.
├── assistant                          ## TermiAgent: Assistant Module
│   ├── assistant.py
│   └── template.py
├── executor                           ## TermiAgent: Executor Module
│   ├── executor.py
├── knowledge                          ## TermiAgent: Interface for Arsenal Module
│   ├── files                          ## Directory for open-sourced exploits
│   │   ├── in_the_wild_exp            ## Usage Manuals for "in-the-wild" exploits
│   │   ├── msfconsole_exp             ## Usage Manuals for Metasploit exploits
│   │   └── path_traversal.md          ## Additional knowledge base
│   ├── knowledge.py
│   └── template.py
├── log                                ## TermiAgent: Path to store log files
│   └── ........
├── memory                             ## TermiAgent: Memory Module
│   ├── memory.py
│   └── template.py
├── reasoner                           ## TermiAgent: Reasoner Module
│   ├── reasoner.py
│   └── template.py
├── utils                              ## TermiAgent: Some utility tools
│   ├── deploy_execute_environment.sh
│   ├── llm.py
│   ├── logger.py
│   ├── msg.py
│   ├── recorder.py
│   └── start_kali.sh
├── TermiBench                         ## TermiBench: 
│   ├── CVE-2015-1427                  ## Target machines
│   ├── CVE-2015-3306
│   ├── CVE-2015-8562
│   │.....<Omitted duplicates>.........
│   ├── CVElist.txt
│   ├── monitor
│   ├── pull_all_images.sh
│   └── README.md                      ## Detailed usage for TermiBench
├── static                          
│   ├── 230-target-from-TermiBench.json
│   └── in-the-wild-exploits.json
├── config.yaml                        ## TermiAgent: Configuration file
├── main.py                            ## TermiAgent: Entry point
├── LICENSE
├── README.md
└── requirements.txt
```
from langchain_core.prompts import PromptTemplate


PROMPT_SUMMARY = PromptTemplate.from_template("""
You are a professional penetration test assistant. 
Given an action and its observation, you should summarize them into a concise sentence that retains all information relevant to penetration testing. 
You should remove redundant or verbose parts, focus on actionable or security-significant details (e.g., vulnerabilities, ports, responses, credentials, errors, banners, etc.), and make the summary as short as possible without losing value.
## The Action
{ACTION}

## The Observation
{OBSERVATION}           

## this is the hint for your summary
{SUMMARY_HINT}

## You need to give the summary result in the following format:

<result>The summarized information</result>     
                                              
## For Example
<result>After executing command nmap -sV -Pn x.x.x.x, get the result: 22/tcp open ssh OpenSSH 9.2p1 Debian 2+deb12u5.</result>  
    
## Note:
1. The summarized text should retain both the Action and Observation sections. You can abbreviate them separately, but do not omit them
2. You need to ensure that the sentence structure is complete
3. The hydra command can only crack weak passwords, but will not log in directly through ssh. You need to emphasize this point in your summary.
4. Please do not abbreviate the file paths included in the observation.
5. For some commands (such as opening bash), if it has no obvious Observation, it will be summarized as the command was executed without error.
6. When using the sed command to modify a file, you need to emphasize whether you are modifying the original file or saving it as a new file.
7. When summarizing, please only summarize the current action and observation, and discard the next step plan, even if this is included in the hint.
8. When using metasploit module, the command `use path/to/exp` is only used to set the specific module, and does not mean that the module has been executed. You need to emphasize this point in your summary.
""")


PROMPT_IDENTIFY_OPTIONS = PromptTemplate.from_template("""
You are a professional penetration test assistant, and your task is to extract each optional item from the observations obtained by the action.
                                                   
## The Action
{ACTION}

## The Observation
{OBSERVATION}

## You need to generate instruction in the following format and give your reason  

<reason>A short reason for your decision</reason>        
<opt>option 1</opt>     
<opt>option 2</opt>
......

Here are two different examples, but please do not mix them up:

## For Example 1
                                                     
# The action: 
`nmap -sn x.x.x.x`

# The observation:
Nmap scan report for 192.168.2.2
Host is up (0.00080s latency).
Not shown: 995 filtered tcp ports (no-response)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      Linksys WRT45G modified dropbear sshd (protocol 2.0)
80/tcp   open  http     lighttpd
Service Info: OS: Linux; Device: router; CPE: cpe:/o:linux:linux_kernel

# Your answer should be
<reason>There are 2 options</reason>        
<opt>22/tcp   open  ssh     Linksys WRT45G modified dropbear sshd (protocol 2.0)</opt>     
<opt>80/tcp   open  http    lighttpd</opt>

## For Example 2
                                                     
# The action: 
`nmap -sV x.x.x.x`

# The observation:
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-06-18 07:49 UTC
Nmap scan report for xxx (192.168.1.0)
Host is up (0.000016s latency).
MAC Address: 96:EB:28:E6:CD:8C (Unknown)
Nmap done: 256 IP addresses (1 host up) scanned in 7.97 seconds

# Your answer should be
<reason>There is 1 host up, MAC address is not included since we only focus on IPv4</reason>        
<opt>host 192.168.1.0 is up</opt>
""")



PROMPT_IDENTIFY_OPTIONS_SV = PromptTemplate.from_template("""
You are a professional penetration test assistant, and your task is to extract each optional item from the observations obtained by the action. and you should analyze each service using your internal penetration testing knowledge.
For each open service, assess its vulnerability exposure based on known CVEs, misconfiguration potential, default credentials, version-specific exploits, and historical attack vectors.
Then, sort the services from highest to lowest risk — where "risk" is defined as the likelihood and potential impact of being successfully exploited by an attacker.
                                                   
## The Action
{ACTION}

## The Observation
{OBSERVATION}

## You need to generate instruction in the following format and give your reason  

<reason>A short reason for your decision</reason>        
<opt>option 1</opt>     
<opt>option 2</opt>
......

## Here is an examples:
                                                     
# The action: 
`nmap -sv x.x.x.x`

# The observation:
Nmap scan report for 192.168.2.2
Host is up (0.00080s latency).
Not shown: 995 filtered tcp ports (no-response)
PORT     STATE SERVICE  VERSION
21/tcp   open  ftp           ProFTPD 1.3.5
22/tcp   open  ssh      Linksys WRT45G modified dropbear sshd (protocol 2.0)
80/tcp   open  http      Apache httpd 2.4.49 ((Unix))
4369/tcp open  epmd       Erlang Port Mapper Daemon
5984/tcp open  couchdb?
Service Info: OS: Linux; Device: router; CPE: cpe:/o:linux:linux_kernel

# Your answer should be
<reason>There are 5 options, and based on my penetration knowledge, I sort them as below as ....</reason>        
<opt>21/tcp   open  ftp     ProFTPD 1.3.5</opt>
<opt>4369/tcp open  epmd       Erlang Port Mapper Daemon</opt>
<opt>5984/tcp open  couchdb?</opt>
<opt>80/tcp   open  http    Apache httpd 2.4.49 ((Unix))</opt>
<opt>22/tcp   open  ssh     Linksys WRT45G modified dropbear sshd (protocol 2.0)</opt>     

Note:
1. Don't miss any service you get from nmap scanning
2. Services such as https and ssh are relatively more secure by design.
""")


OLD_PROMPT_IDENTIFY_OPTIONS_SV = PromptTemplate.from_template("""
You are a professional penetration test assistant, and your task is to extract each optional item from the observations obtained by the action.
                                                   
## The Action
{ACTION}

## The Observation
{OBSERVATION}

## You need to generate instruction in the following format and give your reason  

<reason>A short reason for your decision</reason>        
<opt>option 1</opt>     
<opt>option 2</opt>
......

## Here is an examples:
                                                     
# The action: 
`nmap -sv x.x.x.x`

# The observation:
Nmap scan report for 192.168.2.2
Host is up (0.00080s latency).
Not shown: 995 filtered tcp ports (no-response)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      Linksys WRT45G modified dropbear sshd (protocol 2.0)
80/tcp   open  http     lighttpd
Service Info: OS: Linux; Device: router; CPE: cpe:/o:linux:linux_kernel

# Your answer should be
<reason>There are 2 options</reason>        
<opt>22/tcp   open  ssh     Linksys WRT45G modified dropbear sshd (protocol 2.0)</opt>     
<opt>80/tcp   open  http    lighttpd</opt>
""")



PROMPT_IDENTIFY_OPTIONS_SN = PromptTemplate.from_template("""
You are a professional penetration test assistant, and your task is to extract each optional item from the observations obtained by the action.
                                                   
## The Action
{ACTION}

## The Observation
{OBSERVATION}

## You need to generate instruction in the following format and give your reason  

<reason>A short reason for your decision</reason>        
<opt>option 1</opt>     
<opt>option 2</opt>
......

## Here is an examples:
                                                     
# The action: 
`nmap -sn x.x.x.x/xx`

# The observation:
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-06-18 07:49 UTC
Nmap scan report for <A host name> (192.168.0.1)
Host is up (0.0000030s latency).
MAC Address: 1A:09:89:0E:C3:2A (Unknown)
Nmap scan report for xxx (192.168.1.0)
Host is up (0.000016s latency).
MAC Address: 96:EB:28:E6:CD:8C (Unknown)
Nmap scan report for <A host name> (192.168.159.1)
Host is up (0.000012s latency).
MAC Address: 1A:09:89:0E:C3:2A (Unknown)
Nmap done: 256 IP addresses (3 host up) scanned in 7.97 seconds

# Your answer should be
<reason>There is 1 host up, MAC address is not included since we only focus on IPv4</reason>        
<opt>host 192.168.1.0 is up</opt>

Note:
1. You only need to extract the ipv4 address, the others are not needed.
""")



PROMPT_IDENTIFY_PASSWORD = PromptTemplate.from_template("""
You are a professional penetration test assistant, and your goal is to identify the password that was successfully cracked in the observation from the hydra command action.

## The Action
{ACTION}

## The Observation
{OBSERVATION}

## You need to generate instruction in the following format and give your reason  
<reason>A short reason for your decision</reason>        
<result>yes or no</result>  
<password>one extracted password if successful cracked</password> 

## For examples

<reason>hydra successfully gets a password</reason>        
<result>yes</result>  
<password>admin123</password> 


<reason>hydra did nor get a password</reason>        
<result>no</result>  
<password></password> 

Note:
1. if hydra command is unsuccessful, leave the password tag blank
""")



PROMPT_IDENTIFY_WHATWEB_RESPONSE = PromptTemplate.from_template("""
You are a security assistant analyzing the output of a WhatWeb command, which identifies technologies used by a web server.

Your task is to **extract the most likely web application or service** based on the WhatWeb result:

* Only extract **high-level services or platforms** such as `WordPress`, `Drupal`, `Joomla`, `phpMyAdmin`, `ThinkPHP`, `GeoServer`, `ActiveMQ` etc.
* **Ignore and do not mention** common web servers or infrastructure like Apache, Nginx, Tomcat, Jetty, Debian, PHP, etc.
* If none of these high-level services can be clearly identified, reply with `none` in the service tag.
* If the WhatWeb response has no content or no identifiable service, reply with `none` in the service tag.

Here is the result of the WhatWeb command:
{WHATWEB_OUTPUT}

## You need to generate your answer in the following format and give your reason

<reason>A short reason for your answer</reason> <service>the service you just identified if success</service>

## Example 1

<reason>WhatWeb output only shows Apache and PHP but no CMS or application framework</reason> <service>none</service>

## Example 2

<reason>Detected meta generator tag with content "Joomla! - Open Source Content Management"</reason> <service>joomla</service>
                      
""")


PROMPT_IDENTIFY_HTML_RESPONSE = PromptTemplate.from_template("""
You are a security assistant analyzing the output of a curl command, which retrieves the HTML content of a web page.

Your task is to Extract possible service from the HTML content:
- If the execution succeeded, analyze the returned HTML content and identify what kind of web application or service the page is likely to belong to (for example: WordPress, Drupal, phpMyAdmin, ThinkPHP, Langflow, HugeGraph, etc.). 
- Ignore and do not mention common web servers like Apache, Nginx, Tomcat, Jetty, etc. And you can only extract the single most likely service
- If no service other than (WordPress, Drupal, phpMyAdmin, ThinkPHP, etc.) can be found, reply with `none` in your service tag. 
- If the response of curl command has no reply content, only the URL itself, reply with `none` in your service tag. 


Here is the response of curl command:
{CURL_RESPONSE}

## You need to generate your answer in the following format and give your reason  

<reason>A short reason for your answer</reason>        
<service>the service you just identified if success</service>

## For example 1
<reason>some error</reason>
<service>none</service>

## For example 2
<reason>found geoserver in the html tag</reason>      
<service>geoserver</service>
""")
from langchain_core.prompts import PromptTemplate


PROMPT_CHECK_IF_WEB_SERVICE = PromptTemplate.from_template("""
You are a cybersecurity expert. Based on the following Nmap scan result, determine whether the detected service is likely to be a web service (such as HTTP, HTTPS, or any other web-based application). Provide a clear “yes” or “no” answer, followed by a brief reason. 

## Here is the Nmap result
{NMAP_RESULT}

## You need to give your answer in the following format: 
<reason>A short reason for your decision</reason>        
<result>yes or no</result>  

## For examples

<reason>php server also run a web service</reason>        
<result>yes</result>  

<reason>ssh is not a web service</reason>        
<result>no</result> 

Note: 
1. If there is a question mark after the nmap scan result, it means that the current service is uncertain. In this case, you only need to reply with no in result tag.
""")

PROMPT_SERVICE_EXTRACT = PromptTemplate.from_template("""
You are a cybersecurity expert. Extract the name of the service based on the following Nmap scan result

## Service from nmap result to extract:
PORT     STATE    SERVICE    VERSION
{SERVICE_TO_EXTRACT}

## you should give your extraction result in the following format:
<reason>your reson</reason>
<result>service name 1</result>  
<result>service name 2</result>  

## For Example 1

Service from nmap result to extract:
PORT     STATE    SERVICE    VERSION
22/tcp   open     ssh   OpenSSH 7.7p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)

<reason>ssh and openssh found</reason>
<result>ssh</result>  
<result>openssh</result>  

## For Example 2

Service from nmap result to extract:
PORT     STATE    SERVICE    VERSION
443/tcp  open    ssl/http    nginx 1.11.13

<reason>nginx running ssl based web found</reason>
<result>ssl</result>  
<result>http</result>  
<result>nginx</result> 

Note:
1. The type of service and the specific implementation protocol of the service are both used as the final result, such as ssh and openssh.
2. You don't need to consider the specific version number, just extract the name.
3. If there is a question mark after the nmap scan result, it means that the current service is uncertain. In this case, you only need to reply with a single result tag containing `none`.
4. Unless you only have the apache field, try to avoid extracting only `apache` directly. Instead, use the fully qualified name, such as `Apache HTTP Server` , `Apache ActiveMQ` etc.
""")
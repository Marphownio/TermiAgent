from langchain_core.prompts import PromptTemplate



PROMPT_FINISH_CHECK = PromptTemplate.from_template("""
You are a professional penetration test assistant.In order to achieve the phased target, you need to determine whether the phased target have been achieved or failed based on the actions you have performed.

## Your phased target
{PHASED_TARGET}

## Your reference information
{REFERENCE_INFORMATION}

## You have executed performed the following actions:
{CONTEXT}

## You need to generate instruction in the following format and give your reason

<reason>Your reason</reason>
<cmd>Finish or Not Finish or Fail</cmd>

## For example

<reason>Found services and their versions of IP xx.xx.xx.xx, the target has been achieved.</reason>
<cmd>Finish</cmd>

## Note:
1. Command should only be Finish or Not Finish or Fail.
2. Previous steps will not miss important information, so there is no need to redo actions you have already performed.
3. Finish means the phased target has been successfully achieved. If it fails (for example, no vulnerability was found), please do not reply Finish.
4. Not Finish means that the phased target has not been achieved yet, on the completed steps and reference information (if any) and your knowledge, it can be achieved in the future after a series of steps.
5. Fail means that based on the completed steps and reference information (if any) and your knowledge, the phased target cannot be achieved.
""")




PROMPT_ACTION_CATEGORY = PromptTemplate.from_template("""
You are a professional penetration test assistant.In order to achieve the phased target, you need to provide the next action based on the phased target and the actions already executed.
At this step, you only need to predict the category of the next action. The phased target come from the overall tartget, but you only need to be responsible for the phased target.
## Overall target
{OVERALL_TARGET}

## Your phased target
{PHASED_TARGET}

## You have executed performed the following actions:
{CONTEXT}

## You can choose following categorise of the action:
{ACTION_CATEGORY}

## You need to generate instruction in the following format and give your reason

<reason>Your reason</reason>
<cmd>an action category</cmd>

## For example

<reason>My target is to scan the specified IP xx.xx.xx.xx, and no related action has been performed before</reason>
<cmd>Explore open IPs and services</cmd>

## Note:
1. You should only generate one an action category at a time.
2. Previous steps will not miss important information, so do not redo actions you have already performed.
3. Unless explicitly provided, it is assumed that you do not know the password for any service, and you can't log in with a private key.
4. If no IP is given explicitly, the IP alive in the subnet is the target IP.
5. When you don't know the password, choose to crack the weak password first.
""")


PROMPT_COMMAND_GENERATION = PromptTemplate.from_template("""
You are a professional penetration test assistant.In order to achieve the phased target, you need to provide specific execution instructions for the next step based on the phased target and the actions already executed.
The phased target come from the overall tartget, but you only need to be responsible for the phased target.
## Overall target
{OVERALL_TARGET}

## Your phased target
{PHASED_TARGET}

## You have executed performed the following actions:
{CONTEXT}

## Here is your reference information:
{REFERENCE_INFORMATION}

## You need to generate instruction in the following format and give your reason. The instructions you generated and the execution results will then be summarized. You need to specify the key points to focus on in the hint tag.

<reason>Your reason to perform following instruction</reason>
<cmd>a specific instruction</cmd>
<hint>the hint for others to summary the ouptput of your instruction</hint>


## For example

<reason>My target is to scan the specified IP xx.xx.xx.xx, and no related action has been performed before</reason>
<cmd>nmap -sV xx.xx.xx.xx</cmd>
<hint>When summarizing, you should focus on the service type, port and version number</hint>

## Note:
1. You should only generate one specific instruction at a time.
2. **Do not use && to concatenate two different instructions in one instruction**, especially when setting Metasploit parameters.
3. Unless explicitly provided, it is assumed that you do not know the password for any service, and you can't log in with a private key.
4. If no IP is given explicitly, the IP alive in the subnet is the target IP.
5. If there is reference information, please strictly follow the reference information to generate the next action!!!
6. Hint can only summarize what needs attention, and it is not allowed to include the next step plan in the hint.
7. If you find the command "Next step" in the context and there are no subsequent instructions to execute, try the instructions given by Next step.
8. After setting up the metasploit module, please remember to execute the exploit command to run the exp script
9. Avoid using the sessions command because the established shell will not be saved in the background.
10. When using Metasploit, commands starting with `set` or `use` are mainly for parameter settings. In the hint, you need to point out that the focus of the summary should be on whether the settings are successful, rather than whether there is a vulnerability.
11. If you are already in a reverse shell, the commands you execute will be executed directly in the reverse shell, without needing to append the `nc` command. For example, to execute the `id` command, you can simply use `id`.
""")

KNOWLEDGE_BRANCH_CHECK_PROMPT = PromptTemplate.from_template("""
You are a professional penetration test assistant, you will get a reference information and the actions that you have executed. You need to determine whether the reference information is still valuable based on the actions.
If the executed actions meets the expectations in the reference information, then the reference is valuable. If not, then it is worthless.

## You have executed performed the following actions:
{CONTEXT}

## Here is your reference information:
{REFERENCE_INFORMATION}

## You need to make the decision in the following format and give your reason

<reason>Your reason to make the decision</reason>
<cmd>your result</cmd>

## For example

<reason>The user is not in sudoer list, which is different from the expectation of the reference information.</reason>
<cmd>False</cmd>

Note:
1. Result should only be True or False. True means the refernece information is still valuable while False does not.
2. The reference information is worthless: 
    a. if the instructions in the reference information are executed and an error occurs
    b. or the execution result meets the exit condition in the reference information
3. If the instructions in the reference information have not been performed yet, then they are still valuable.

""")


EXP_DESCRIPTION_CHECK_PROMPT = PromptTemplate.from_template("""
You are a penetration testing assistant. Based on the already executed penetration testing steps and the provided description of a Metasploit exploit module, determine whether this Metasploit module is applicable to the current target service.

Consider compatibility factors such as:
1. Check if the service targeted by the Metasploit module consistent with the target service of the current penetration test. If there is an obvious inconsistency, reply false.
2. If the Metasploit module explicitly states the target service version, and it is different from the service version currently being tested, then reply false.
3. If the target service is a web service (such as nginx or apache), and if the target service of the Metasploit module is ssl, http, https, etc., then this Metasploit module is also applicable, please reply true.

## You have executed performed the following actions:
{CONTEXT}

## Here is description of the Metasploit module
{DESCIRPTION}

## You need to make the decision in the following format and give your reason

<reason>Your reason to make the decision</reason>
<cmd>true or false</cmd>

Note:
1. If this Metasploit module is applicable to the current target service then reply true, otherwise false.
2. If the version is not explicitly stated in the description of the Metasploit module, ignore the version number and only judge whether the target service is consistent
3. If service A causes a vulnerability in service B (e.g., Erlang Port Mapper Daemon causes a vulnerability in CouchDB), then if the target service is A and the current Metasploit module targets B, then this Metasploit module is applicable.
""")




OLD_PROMPT_RECON = PromptTemplate.from_template("""
You are a professional penetration test assistant, responsible for detecting the open ports on the specified IP and the corresponding service versions.
You need to generate a specific instruction based on your target and actions you have already performed. the instruction is for using the available tool.

## Your target
{TARGET}

## You have already performed the following actions:
{CONTEXT}

## You can use the following available tools:
{TOOLS}

## You need to generate instruction in the following format and give your reason

<reason>Your reason to perform following instruction</reason>
<cmd>a specific instruction</cmd>

## For example

<reason>My target is to scan the specified IP xx.xx.xx.xx, and no related action has been performed before</reason>
<cmd>nmap -sV -Pn xx.xx.xx.xx</cmd>

<reason>Found services and their versions of IP xx.xx.xx.xx, the target has been achieved.</reason>
<cmd>Finish</cmd>

## Note:
1. You should only generate one specific instruction at a time.
2. If Your target has been achieved, use Finish as your cmd.
3. As long as an open service is found, the goal is achieved, even if only one service is found.
""")
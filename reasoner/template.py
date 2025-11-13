from langchain_core.prompts import PromptTemplate

PROMPT_REASONER = PromptTemplate.from_template("""
You are an experienced penetration testing expert leading a team tasked with conducting a penetration test with the overall goal. You need to provide the next phased target based on the context, in order to achieve the overall goal.

## Your overall goal: 
{OVERALL_GOAL} 
                                               
## The context:
{CONTEXT}

## You should provide the next phased target in the following format and give your reason:
<reason>your reason for this instruction</reason>
<target>Your instruction or order</target>

## For example:
### Example 1
<reason>find a ip in the subnet xx.xx.xx.xx/24</reason>
<target>Please investigate the open ports and running services on xx.xx.xx.xx</target>

### Example 2
<reason>the goal is achieved</reason>
<target>finish</target>

## Note:
1. You should only provide instruction or order, not direct linux command or code, and do not specify which metasploit module to use (not even by giving an example).
2. Your instructions should avoid any possible ambiguity, and your instructions should be concise.
3. If the overall goal includes steps for execution, please provide instructions according to the steps in the overall goal.
4. If the overall goal are achieved based on the executed actions, use finish in your response.
5. If an IP address is not found, it means that it has been ignored and no need to execute the command again to find it.
6. If you find the command "Next step" in the context and there are no subsequent instructions to execute, try the instructions given by Next step.
7. If your overall goal is to read the flag file, you will need to report the specific contents, an n-digit password string, in reason tag. Note that just the action of reading the file is not enough to complete the overall goal.
8. If your overall goal is to get the shell of the target host, **after getting the shell, you need to execute the `id` or `whoami` command**. If the execution is successful and you get a response, the overall goal is then completed.
9. If your overall goal is to get the shell of the target host, in some cases, you may not be able to get a persistent shell, and you can only send the target command (such as id) and get a one-time result. This situation can also be considered as achieving the goal.
10. You need to pay attention that some flags are the password of the 'admin' user. If you get the password, you don't need to read the flag file.
""")



PROMPT_TASK_CHECK = PromptTemplate.from_template("""
Analyze the following input prompt and determine whether its primary goal is to (A) read or capture a CTF flag, or (B) gain a shell on a target machine.

## Input Prompt:
{OVERALL_GOAL}  

## You should provide your answer in the following format and give your reason:
<reason>your reason for this answer</reason>
<target>flag or shell</target>

Note:
1. the final answer in taget tag should only be flag of shell.
""")
# from reasoner.template import PROMPT_REASONER
from utils.msg import Msg,Current_Assistant,Phase
import pexpect
import os
import re
import pty
import subprocess
import threading
import queue
import time
import sys
import yaml
import signal

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)


class Executor:

    def __init__(self, llm, logger, network):
        self.logger = logger
        self.llm = llm
        self.timeout = 60 * 5
        self.in_msf_exp_flag = False
        self.in_in_the_wild_exp_flag = False
        self.in_in_the_wild_exp_flag_reverse_shell = False
        self.kali_container_name = f"{network}_mykali"
        self.kali_image_name = config["kali_config"]["kali_image_name"]
        self.local_ip = config["docker_network"][network]["attacker_ip"]
        self.kali_network = network
        self.init_kali_msfconsole()
        self.msf_time_out = 0.6 * 60
        self.COMMANDDONE = "PENTESTAGENT"
        self.COMMANDDONE1 = "PENTEST"
        self.COMMANDDONE2 = "AGENT"
        

    def __del__(self):
        self.close()

    def __call__(self, state: Msg) -> Msg:
        try:
            # if state["action"].lower().strip() == "attempt_failed":
            #     return state.copy()
            observation = self.exec(state["action"], state["password"])
            self.logger.debug(observation)
            new_state = state.copy()
            new_state.update({
                "raw_observation": observation,
                })
            return new_state
            
        except Exception as e:
            raise Exception(e)
        
    def init_kali_raw_console(self):
        try:
            self.logger.info("Kali raw console initiating......", "System")
            self.child_raw = pexpect.spawn('/bin/bash', encoding='utf-8', echo=False)
            # self.child = ANSI(self.child) 
            self.child_raw.expect([r'#\s*$', r'\$\s*$', r'msf6'], timeout=self.timeout)
            
            init_cmd = f'''docker exec -it {self.kali_container_name} bash -c "echo \\"export PS1='# '\\" >> ~/.bashrc && source ~/.bashrc && /bin/bash"'''
            self.child_raw.sendline(init_cmd)
            self.child_raw.expect([r'#\s*$', r'\$\s*$', r'msf6'], timeout=self.timeout)
            output = self.child_raw.before.strip()
            self.logger.info("Kali raw console initiation finished", "System")
        except Exception as e:
            self.logger.error(f"Error initializing Kali console: {e}")
            exit(0)
            
    def init_local_raw_console(self):
        try:
            self.logger.info("Local raw console initiating......", "System")
            self.child_local_raw = pexpect.spawn('/bin/bash', encoding='utf-8', echo=False)
            self.logfile2 = open("./log/local_session.log", "w", encoding='utf-8')
            self.child_local_raw.logfile = self.logfile2
            # self.child = ANSI(self.child)  
            self.child_local_raw.sendline('export PS1=">>> "')
 
            self.child_local_raw.expect('>>> ', timeout=self.timeout)
            # self.child_local_raw.expect([r'#\s*$', r'\$\s*$', r'msf6'], timeout=self.timeout)
            
            output = self.child_local_raw.before.strip()
            self.logger.info("Local raw console initiation finished", "System")
        except Exception as e:
            self.logger.error(f"Error initializing Local console: {e}")
            exit(0)


    def run_and_kill(self, cmd, timeout=100):
        proc = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        def kill_proc():
            try:
                os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
            except ProcessLookupError:
                pass

        timer = threading.Timer(timeout, kill_proc)
        timer.start()



    def exec_for_reverse_shell(self,cmd):
        try:

            command_nc = cmd.split("&")[0].strip()
            command_docker = cmd.split("&")[1].strip()

            self.child_raw.sendline(command_nc)
            self.run_and_kill(command_docker)
            try:
                index = self.child_raw.expect([r'#\s*$', r'\$\s*$', r'>\s*$'], timeout=self.timeout)

                if index != 0:
                    # success
                    self.logger.info("Entered target's reverse shell", "System")
                    output = self.child_raw.before.strip().replace(cmd,"")
                    output = "You have successfully obtained the target machine's reverse shell and you are now in a reverse shell, and you can execute subsequent commands directly."
                    self.in_in_the_wild_exp_flag_reverse_shell = True
                else:
                    output = self.child_raw.before.strip().replace(cmd, "")
                    output = "no reverse shell was found"
                    self.in_in_the_wild_exp_flag_reverse_shell = False
                return output
            except pexpect.TIMEOUT:
                self.logger.debug("expect() timed out waiting for reverse shell")
                try:
                    self.child_raw.sendcontrol('c')
                    # or: self.child_local_raw.send('\x03')
                    time.sleep(1)
                    self.child.expect([r'#\s*$', r'\$\s*$', r'msf6'], timeout=self.timeout)
                    output = self.child.before.strip().replace(cmd,"")
                    return "no reverse shell was found"
                except Exception as e:
                    self.logger.debug(f"Failed to send Ctrl-C to pexpect child: {e}")
                    return "no reverse shell was found"
        except Exception as e:
            self.logger.error(f"Error exec in raw console: {e}")
            exit(0)


    def exec_in_local_raw_console_reverse_shell(self,cmd):
        try:
            self.child_raw.sendline(cmd.strip())
            self.child_raw.expect([r'#\s*$', r'\$\s*$', r'>\s*$'], timeout=self.timeout)
            output = self.child_raw.before.strip().replace(cmd,"")
            return self.clean_output(output,cmd)
        except Exception as e:
            self.logger.error(e)
            exit(0)


            
    def exec_in_local_raw_console(self, cmd):
        try:
            self.child_local_raw.sendline(cmd)
            index = self.child_local_raw.expect([r'>>>\s*$', r'>\s*$', r'\$\s*$'], timeout=self.timeout)
            if self.in_in_the_wild_exp_flag:
                output = self.child_local_raw.before.strip()
                if index == 0:
                    self.in_in_the_wild_exp_flag = False
            else:  
                if index != 0:
                    # success
                    self.logger.info("Entered in-the-wild exp shell", "System")
                    output = self.child_local_raw.before.strip().replace(cmd,"")
                    output = "You have successfully obtained the target machine's shell and can start executing commands."
                    self.in_in_the_wild_exp_flag = True
                else:
                    output = self.child_local_raw.before.strip().replace(cmd, "")
                    self.in_in_the_wild_exp_flag = False
            return output
        except Exception as e:
            self.logger.error(f"Error exec in raw console: {e}")
            exit(0)
            
    def exec_in_kali_raw_console(self, cmd):
        try:
            self.child_raw.sendline(cmd)
            self.child_raw.expect([r'#\s*$', r'\$\s*$', r'msf6'], timeout=self.timeout)
            output = self.child_raw.before.strip().replace(cmd,"")
            return self.clean_output(output, cmd)
        except Exception as e:
            self.logger.error(f"Error exec in Kali console: {e}")
            exit(0)
        
    def init_kali_msfconsole(self):
        try:
            self.logger.info("Console initiation start......", "System")
            self.child = pexpect.spawn('/bin/bash', encoding='utf-8', echo=False)
            # self.child = ANSI(self.child)   
            self.child.expect([r'#\s*$', r'\$\s*$', r'msf6'], timeout=self.timeout)
            self.logfile = open("./log/kali_session.log", "w", encoding='utf-8')
            self.child.logfile = self.logfile
            output = self.exec(f"bash ./utils/start_kali.sh {self.kali_container_name} {self.kali_image_name} {self.kali_network} {self.local_ip}")
            self.logger.info(output)
            self.exec(f"docker exec -it {self.kali_container_name} msfconsole")
            self.logger.info("Console initiation finished", "System")
            self.init_kali_raw_console()
            self.init_local_raw_console()
        except Exception as e:
            self.logger.error(f"Error initializing Kali console: {e}")
            exit(0)

        

    def exec(self, cmd, password = ""):
        try:
            
            if cmd.strip().startswith("whatweb"):
                return self.exec_in_kali_raw_console(cmd)
            if self.in_in_the_wild_exp_flag:
                return self.exec_in_local_raw_console(cmd)
            if self.in_in_the_wild_exp_flag_reverse_shell:
                return self.exec_in_local_raw_console_reverse_shell(cmd)
            if cmd.strip().startswith("docker") and "anonymoustermibench/exploit" in cmd:
                return self.exec_in_local_raw_console(cmd)
            if cmd.strip().startswith("nc") and "anonymoustermibench/exploit" in cmd:
                return self.exec_for_reverse_shell(cmd)
            if cmd.strip().startswith("use") or cmd.strip().startswith("set"):
                self.in_msf_exp_flag = False

            if cmd.startswith("ssh_login"):
                # match parameter
                user_match = re.search(r'--user\s+(\S+)', cmd)
                password_match = re.search(r'--password\s+(\S+)', cmd)
                host_match = re.search(r'--host\s+(\S+)', cmd)
                port_match = re.search(r'--port\s+(\S+)', cmd)

                # extract parameter
                user = user_match.group(1) if user_match else None
                password = password_match.group(1) if password_match else None
                host = host_match.group(1) if host_match else None
                port = port_match.group(1) if port_match else "22"
                output = self.ssh_login(host, port, user, password)
            elif cmd.startswith("sudo") or cmd.startswith("su"):
                self.child.sendline(cmd)
                # self.child.expect([r'#\s*$', r'\$\s*$', r'msf6'], timeout=self.timeout)
                index = self.child.expect([
                    r'[Pp]assword:',    # match password  
                    r'[Pp]assword for [^:\n]+:',
                    r'#\s*$',           # root shell  
                    r'\$\s*$',          #   shell  
                    r'msf6',           #  other
                ], timeout=self.timeout)

                if index == 0 or index == 1:
                    # get password input
                    self.child.sendline(password)
                    index = self.child.expect([
                        r'#\s*$', 
                        r'\$\s*$', 
                        r'msf6',                   
                        r'Sorry, try again.',      
                        r'[Pp]ermission denied',
                        r'incident has been reported to the administrator.',
                        r'Authentication failure'
                        ], timeout=self.timeout)

                    if index in [3, 4]:  
                        self.child.send('\x03')  # send Ctrl+C
                        output = "Authentication failed. Aborted with Ctrl+C."
                        self.child.expect([r'#\s*$', r'\$\s*$', r'msf6'], timeout=5)
                    elif index == 5:
                        output = "Authentication failed. this user is not in the sudoers file."
                        self.child.expect([r'#\s*$', r'\$\s*$', r'msf6'], timeout=5)
                    elif index == 6:
                        output = "Authentication failed."
                        self.child.expect([r'#\s*$', r'\$\s*$', r'msf6'], timeout=5)
                    else:
                        output = "Authentication succeed, get:" + self.child.before.strip()
                else:
                    output = "sudo command executed with no error, get: " + self.child.before.strip()
            elif cmd.strip() == "exploit":
                try:
                    self.child.sendline(cmd)
                    index = self.child.expect([r'meterpreter.*?>', r'#\s*$', r'\$\s*$', r'msf6'], timeout=self.msf_time_out)
                    if index == 0:
                        self.logger.info("msfconsole exploit successfully", "System")
                        time.sleep(1)
                        self.child.sendline("shell")
                        new_cmd = f"id; echo '{self.COMMANDDONE1}''{self.COMMANDDONE2}'"
                        self.child.sendline(new_cmd)
                        self.child.expect(f"{self.COMMANDDONE}", timeout=self.timeout)
                        self.child.before.strip().replace(new_cmd,"")
                        self.in_msf_exp_flag = True
                        self.logger.info("Entered msfconsole exp shell", "System")
                        output = "You have successfully obtained the target machine's shell and can start executing commands"
                    else:
                        output = self.child.before.strip().replace(cmd,"")
                except pexpect.TIMEOUT:
                    output = self.child.before.strip().replace(cmd,"")
                    new_cmd = f"id; echo '{self.COMMANDDONE1}''{self.COMMANDDONE2}'"
                    self.child.sendline(new_cmd)
                    self.child.expect(f"{self.COMMANDDONE}", timeout=self.timeout)
                    output = self.child.before.strip().replace(new_cmd,"")
                    self.in_msf_exp_flag = True
                    self.logger.info("Entered msfconsole exp shell", "System")
                    output = "You have successfully obtained the target machine's shell and can start executing commands"
            elif self.in_msf_exp_flag == True:
                new_cmd = f"{cmd.strip()}; echo '{self.COMMANDDONE1}''{self.COMMANDDONE2}'"
                self.child.sendline(new_cmd)
                self.child.expect(f"{self.COMMANDDONE}", timeout=self.timeout)
                output = self.child.before.strip().replace(new_cmd,"")
            else:
                self.child.sendline(cmd)
                self.child.expect([r'#\s*$', r'\$\s*$', r'msf6'], timeout=self.timeout)
                output = self.child.before.strip().replace(cmd,"")
            return self.clean_output(output,cmd)
        except Exception as e:
            self.child.sendcontrol('c')  # send Ctrl+C
            self.child.expect([r'#\s*$', r'\$\s*$', r'msf6'], timeout=self.timeout)
            self.logger.error(e)
            output = self.child.before.strip().replace(cmd,"")
            return self.clean_output(output,cmd) + "\n\nExecution_Error:" + str(e)

    def ssh_login(self, host, port, user, password):
        ssh_cmd = f"ssh -p {port} {user}@{host}"
        try:
            self.child.sendline(ssh_cmd)

            i = self.child.expect([
                "yes/no",               
                "password:",             
                pexpect.EOF,
                pexpect.TIMEOUT
            ],
            timeout=self.timeout)

            if i == 0:
   
                self.child.sendline("yes")
                self.child.expect("password:")
                self.child.sendline(password)
            elif i == 1:
                self.child.sendline(password)
            else:
                self.logger.error("SSH login failed")
                return f"SSH command {ssh_cmd} login failed"

            j = self.child.expect([
                r'#\s*$', r'\$\s*$', r'msf6',                        
                r'Permission denied, please try again',                                
                pexpect.EOF,
                pexpect.TIMEOUT
            ], timeout=self.timeout)

            return f"SSH login succeed! With output:\n {self.child.before.strip()}"

            if j == 3:  # Permission denied
                self.logger.error("SSH login failed: wrong password")
                child.sendcontrol('c')
                child.expect([r'#\s*$', r'\$\s*$', r'msf6'], timeout = self.timeout)
                return "SSH login failed: wrong password"
            elif j in [4, 5]:  # EOF or TIMEOUT
                self.logger.error("SSH login failed: no shell prompt")
                return "SSH login failed: no shell prompt"
        except Exception as e:
            self.logger.error(e)
            return str(e)
    def clean_nmap_output(self, input_text):
        cleaned_lines = []
        for line in input_text.splitlines():
            if not line.startswith("SF:"):
                cleaned_lines.append(line)
        return "\n".join(cleaned_lines)

    def clean_output(self, output_raw, cmd):
        output = output_raw[-20000:]
        if cmd.startswith("curl"):
            return output
        if self.in_msf_exp_flag == True or self.in_in_the_wild_exp_flag == True or self.in_in_the_wild_exp_flag_reverse_shell == True:
            return output
        if cmd.startswith("nmap") and "-sv" in cmd.lower():
            output = self.clean_nmap_output(output)
        # output_lines = output.splitlines()
        # final_output = []
        # flag = True

        # for line in output_lines:
        #     if not flag:
        #         final_output.append(line)
        #     if flag and "[*] exec" in line:
        #         flag = False

        # cleaned = '\n'.join(final_output)
        cleaned = output
        cleaned = re.sub(r'\x1b\[[0-9;]*m', '', cleaned)  
        i = cleaned.rfind('\n')
        if i != -1:
            cleaned = cleaned[:i]
        return cleaned.replace(" > \r\r\n[*] exec: \r\n\r","")

    def close(self):
        self.child.close()
        self.child_raw.close()
        self.child_local_raw.close()
        self.logfile.close()
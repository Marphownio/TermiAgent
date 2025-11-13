from utils.msg import Msg,Current_Assistant,Phase
from memory.template import PROMPT_IDENTIFY_OPTIONS, PROMPT_SUMMARY, PROMPT_IDENTIFY_OPTIONS_SN, PROMPT_IDENTIFY_OPTIONS_SV, PROMPT_IDENTIFY_PASSWORD, PROMPT_IDENTIFY_WHATWEB_RESPONSE, PROMPT_IDENTIFY_HTML_RESPONSE
import traceback
import re
import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)


class DecisionNode:
    def __init__(self, 
                 parent_node = None,
                 first_child_node = None,
                 first_peer_node = None,
                 raw_context = None,
                 brief_context = None,
                 knowledge_branch_key = "",
                 knowledge_branch_index = 0,
                 splitting_flag = False,
                 reset_phased_goal_flag = False
                 ):
        self.parent_node = parent_node
        self.first_child_node = first_child_node
        self.first_peer_node = first_peer_node
        self.raw_context = raw_context if raw_context is not None else []
        self.brief_context = brief_context if brief_context is not None else []
        self.knowledge_branch_key = knowledge_branch_key
        self.knowledge_branch_index = knowledge_branch_index
        self.repeat_time = 0
        self.repeat_flag = False
        self.repeat_time_limit = 20
        self.splitting_flag = splitting_flag  
        self.curl_web_flag = False  
        self.reset_phased_goal_flag = reset_phased_goal_flag  
        self.exp_node_flag = False
        self.exp_instruction = ""

    def set_exp_node(self, exp_instruction):
        self.exp_node_flag = True
        self.exp_instruction = exp_instruction

    def set_splitting_flag_true(self):
        self.splitting_flag = True
        self.curl_web_flag = True

    def set_curl_web_flag_flase(self):
        self.curl_web_flag = False


class Memory:
    def __init__(self, llm, logger, recorder, knowledge_base, network):
        self.logger = logger
        self.llm = llm
        self.root_node = DecisionNode()
        self.root_node.raw_context.append(["msfconsole","opened"])
        self.root_node.brief_context.append(f"Opend msfconsole, and note your local ip is {config['docker_network'][network]['attacker_ip']}, not 0.0.0.0. You can deploy self-built exploit in ip {config['docker_network'][network]['exp_ip_range']}, and with docker network {network}")
        self.current_node = self.root_node
        self.recorder = recorder
        self.knowledge_base = knowledge_base

    def is_on_knowledge_branch(self):
        current_key, current_index = self.get_knowledge_key_index()
        if current_key == "":
            return False
        else:
            return True

    def set_exp_knowledge_key_index(self):
        self.current_node.knowledge_branch_index = 0
        self.current_node.knowledge_branch_key = "exp"

    def is_exp_node(self):
        return self.current_node.exp_node_flag

    def is_checked_exp_node(self):
        if self.current_node.knowledge_branch_key == "exp":
            return True
        else:
            return False

    def get_exp_instruction_file(self):
        return self.current_node.exp_instruction

    def add_child_node_in_context(self,
                    option_list,
                    split_flag=False,
                    brief_context_flag=False,
                    first_node_split_flag=False,
                    reset_phased_goal_flag=False
                    ):
        if option_list == None or len(option_list) == 0:
            return
        new_node_list = []
        for option_item in option_list:
            new_node = DecisionNode(
                self.current_node,
                None,
                None,
                None,
                None,
                "",
                0,
                split_flag,
                reset_phased_goal_flag
            )
            if len(option_item) == 3:
                new_node.set_exp_node(option_item[2])
                option_item = option_item[:2]
            new_node.raw_context.append(option_item)
            if brief_context_flag:
                new_node.brief_context.append(f"{option_item[0]} {option_item[1].lower()}")
            new_node_list.append(new_node)
        if first_node_split_flag:
            new_node_list[0].set_splitting_flag_true()
        self.current_node.first_child_node = new_node_list[0]

        for i in range(len(new_node_list)-1):
            new_node_list[i].first_peer_node = new_node_list[i+1]

    def check_curl_web_service(self):
        if not (self.current_node.splitting_flag and self.current_node.curl_web_flag):
            return
        whatweb_flag = False
        curl_flag = False    
        for item in self.current_node.raw_context:
            if item[0].strip().startswith("-whatweb"):
                whatweb_flag = True
            if item[0].strip().startswith("-curl"):
                curl_flag = True
            if item[0].strip().startswith("whatweb"):
                prompt = PROMPT_IDENTIFY_WHATWEB_RESPONSE.format(
                    WHATWEB_OUTPUT = item[1]
                )
                res = self.llm(prompt)
                self.logger.debug(res)
                matches2 = re.findall(r"<service>(.*?)</service>", res)
                if len(matches2) == 1 and matches2[0].lower().strip() != "none":
                    self.current_node.set_curl_web_flag_flase()
                    selected_set = set()
                    possible_solutions_list = self.knowledge_base.get_a_service_possible_solutions(matches2[0].lower().strip(),selected_set)
                    self.add_child_node_in_context(possible_solutions_list,False,True,False,True)
                    self.switch_to_next_node()
                    return
                elif curl_flag:
                    self.current_node.set_curl_web_flag_flase()
                    self.switch_to_next_node()
                    return
                else:
                    item[0] = f"-{item[0].strip()}"
                    item[1] = "No target server has been found, Next step: continue to try the service fingerprint."
                    
            if item[0].strip().startswith("curl"):
                prompt = PROMPT_IDENTIFY_HTML_RESPONSE.format(
                    CURL_RESPONSE = item[1]
                )
                res = self.llm(prompt)
                self.logger.debug(res)
                matches2 = re.findall(r"<service>(.*?)</service>", res)
                if len(matches2) == 1 and matches2[0].lower().strip() != "none":
                    self.current_node.set_curl_web_flag_flase()
                    selected_set = set()
                    possible_solutions_list = self.knowledge_base.get_a_service_possible_solutions(matches2[0].lower().strip(),selected_set)
                    self.add_child_node_in_context(possible_solutions_list,False,True,False,True)
                    self.switch_to_next_node()
                    return
                elif whatweb_flag:
                    self.current_node.set_curl_web_flag_flase()
                    self.switch_to_next_node()
                    return
                else:
                    item[0] = f"-{item[0].strip()}"
                    item[1] = "No target server has been found, Next step: continue to try the service fingerprint."
                    
        if (whatweb_flag and curl_flag) or len(self.current_node.raw_context)>4:
            self.current_node.set_curl_web_flag_flase()
            self.switch_to_next_node()
            return
                    
            
        

    def split_current_node(self):
        if not (self.current_node.splitting_flag and self.current_node.first_child_node == None and self.current_node.curl_web_flag == False):
            return
        else:
            information = self.current_node.raw_context[0][1]
            possible_solutions_list, first_node_split_flag = self.knowledge_base.get_service_possible_solutions(information)
            self.add_child_node_in_context(possible_solutions_list,False,True,first_node_split_flag,True)
            self.switch_to_next_node()

    def switch_to_next_child_node(self):
        self.logger.info("Switch to the next child node.","System")
        self.summary_context()
        self.current_node = self.current_node.first_child_node
        self.split_current_node()
        

    def switch_to_next_peer_node(self):
        self.logger.info("Switch to the next peer node.","System")
        self.current_node = self.current_node.first_peer_node
        self.split_current_node()

    def switch_to_next_node(self):
        if self.current_node.first_child_node is not None:
            self.switch_to_next_child_node()
        elif self.current_node.first_peer_node is not None:
            self.switch_to_next_peer_node()
        else:
            node = self.current_node
            while self.root_node != node:
                node = node.parent_node
                if node.first_peer_node is not None:
                    self.current_node = node.first_peer_node
                    self.split_current_node()
                    return
            print("back to root")
            exit(0)

        

    def get_knowledge_key_index(self):
        return self.current_node.knowledge_branch_key, self.current_node.knowledge_branch_index

    def add_child_node_in_knowledge(self, knowledge_list):
        new_node_list = []
        for item in knowledge_list:
            new_node = DecisionNode(
                self.current_node,
                None,
                None,
            )
            new_node.knowledge_branch_key = item[0]
            new_node.knowledge_branch_index = item[1]
            new_node_list.append(new_node)

        # extra None node
        # new_node = DecisionNode(
        #         self.current_node,
        #         None,
        #         None,
        #     )
        # new_node_list.append(new_node)
        
        self.current_node.first_child_node = new_node_list[0]

        for i in range(len(new_node_list)-1):
            new_node_list[i].first_peer_node = new_node_list[i+1]

        self.switch_to_next_child_node()


    def parse_options(self, text):
        matches = re.findall(r"<opt>(.*?)</opt>", text)
        if len(matches) == 0:
            self.logger.error("error")
            traceback.print_exc()
        return matches
    
    def parse_summary(self, text):
        matches = re.findall(r"<result>(.*?)</result>", text)
        if len(matches) != 1:
            self.logger.error("error")
            traceback.print_exc()
        return matches[0].strip()

            
    def back_to_last_cross(self):
        while self.current_node.first_peer_node == None:
            self.current_node = self.current_node.parent_node


    def identify_options(self, state: Msg):
        specific_cmd = state["action"].split()[0].strip().lower()
        self.logger.debug(specific_cmd)
        split_flag= False
        if specific_cmd != "nmap":
            return False
        if "-sv" in state["action"].lower():
            current_prompt = PROMPT_IDENTIFY_OPTIONS_SV
            split_flag = True
        elif "-sn" in state["action"].lower():
            current_prompt = PROMPT_IDENTIFY_OPTIONS_SN
        else:
            current_prompt = PROMPT_IDENTIFY_OPTIONS
        prompt = current_prompt.format(
            ACTION = state["action"],
            OBSERVATION = state["raw_observation"]
        )
        res = self.llm(prompt)
        self.logger.debug(res)
        option_list = self.parse_options(res)
        new_option_list = []
        for item in option_list:
            new_option_list.append((state["action"],item))
        self.add_child_node_in_context(new_option_list, split_flag)
        self.switch_to_next_child_node()
        return True

    def summary_action_observation(self, action, observation, summary_hint=""):
        prompt = PROMPT_SUMMARY.format(
            ACTION = action,
            OBSERVATION = observation,
            SUMMARY_HINT = summary_hint
        )
        res = self.llm(prompt)
        self.logger.debug(res)
        return self.parse_summary(res)


    def summary_context(self, summary_hint=""):
        raw_context_len = len(self.current_node.raw_context)
        brief_context_len = len(self.current_node.brief_context)
        number_of_context_to_summary = raw_context_len - brief_context_len
        for i in range(number_of_context_to_summary):
            context_item_to_summary = self.current_node.raw_context[brief_context_len + i]
            brief_item = self.summary_action_observation(context_item_to_summary[0],context_item_to_summary[1],summary_hint)
            self.current_node.brief_context.append(brief_item)

    def add_context(self, state: Msg):
        self.current_node.raw_context.append([
            state["action"],
            state["raw_observation"],
        ])
    
    def get_history_context(self):
        node = self.current_node
        context_list = []
        while True:
            context_list.append("\n".join(node.brief_context))
            if self.root_node == node:
                break
            else:
                node = node.parent_node
        context = ""
        for item in reversed(context_list):
            context = context + item
        # return "\n".join(self.current_node.brief_context)
        return context


    def get_context(self, summary_hint):
        if len(self.current_node.raw_context) != len(self.current_node.brief_context):
            self.summary_context(summary_hint)
        return self.get_history_context()

    def identify_password(self, state: Msg):
        specific_cmd = state["action"].split()[0].strip().lower()
        target_cmd = {"hydra"}
        if specific_cmd not in target_cmd:
            return
        prompt = PROMPT_IDENTIFY_PASSWORD.format(
            ACTION = state["action"],
            OBSERVATION = state["raw_observation"]
        )
        res = self.llm(prompt)
        self.logger.debug(res)
        matches = re.findall(r"<password>(.*?)</password>", res)
        if len(matches) != 1:
            self.logger.error("error")
            traceback.print_exc()
        if len(matches[0].strip())>0:
            state.update({
                "password": matches[0].strip(),
                "raw_observation": res.strip()
            })

    def clear_current_node_context(self):
        if self.current_node.knowledge_branch_key != "":
            self.current_node.raw_context = []
            self.current_node.brief_context = []
        else:
            first_node = self.current_node.raw_context[0]
            self.current_node.raw_context = [first_node]
            self.current_node.brief_context = []
        self.logger.info("Context updated!","System")
            

    def if_exceed_repeat_limit(self):
        if self.current_node.repeat_time > self.current_node.repeat_time_limit:
            if self.current_node.repeat_flag:
                self.switch_to_next_node()
            else:
                self.current_node.repeat_flag = True
                self.current_node.repeat_time = 0
                self.clear_current_node_context()
            return True
        else:
            self.current_node.repeat_time = self.current_node.repeat_time + 1
            return False

    def check_reset_phased_goal_flag(self):
        if self.current_node.reset_phased_goal_flag:
            self.current_node.reset_phased_goal_flag = False
            return True
        else:
            return False
        

    def __call__(self, state: Msg) -> Msg:
        summary_flag = False
        to_reasoner = "false"
        if state["action"].lower().strip() == "fail" or state["action"].lower().strip() == "attempt_failed":
            self.current_node.repeat_time = 100
        if self.if_exceed_repeat_limit():
            pass
        elif state["action"].lower().strip() == "attempt_failed":
            self.switch_to_next_node()
            to_reasoner = "true"
        elif state["action"].lower().strip() == "fail":
            self.switch_to_next_node()
            to_reasoner = "true"
        elif state["action"].lower().strip() == "force_failed":
            self.switch_to_next_node()
            to_reasoner = "true"
        else:
            self.recorder.write_action_observation(
                state["action"],
                state["raw_observation"]
            )
            if not self.identify_options(state):
                self.identify_password(state)
                self.add_context(state)
                summary_flag = True
        self.check_curl_web_service()
        self.logger.print_tree(self.root_node, self.current_node)
        new_state = state.copy()
        summary_hint = ""
        # if summary_flag and state["action"].lower().strip().startswith("curl"):
        if summary_flag:
            summary_hint = state["summary_hint"]
        
        if self.check_reset_phased_goal_flag():
            to_reasoner = "true"
        new_state.update({
            "context": self.get_context(summary_hint),
            "to_reasoner": to_reasoner
            })
        self.logger.debug(new_state)
        return new_state

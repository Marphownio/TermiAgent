import re
import os
from typing import List, Tuple
from knowledge.template import PROMPT_CHECK_IF_WEB_SERVICE,PROMPT_SERVICE_EXTRACT
import json
from rapidfuzz import fuzz


class KnowledgeBase:
    def __init__(
        self,
        logger,
        llm,
        directory = "./knowledge/files",
        top_k: int = 2
    ):
        self.logger = logger
        self.llm = llm
        self.directory = directory
        self.content, self.key_list = self.parse_markdown()
        self.get_possible_solutions()
        self.task_type = "shell"
        # print(kv_pairs)
        # # documents = self.build_documents(kv_pairs)
    
    def extract_chunks(self, text):
        
        chunks = re.findall(r'<chunk>(.*?)</chunk>', text, re.DOTALL)
        if not chunks:
            return text
        if len(chunks) == 1:
            return chunks[0]
        return chunks

    def set_task_type(self, task_type):
        self.task_type = task_type

    def parse_markdown(self):
        data = {}
        key_list = []

        for filename in os.listdir(self.directory):
            if filename.endswith('.md'):
                file_path = os.path.join(self.directory, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()

                 
                for line in content.splitlines():
                    if line.strip().startswith('# '):
                        key = line.strip()[2:].strip()
                        data[key] = self.extract_chunks(content)
                        key_list.append(key)
                        break
                else:
                     
                    continue

        return data, key_list
    

    def get_reference_content(self, current_key, current_index):
        return self.content[current_key][current_index]

    def get_reference_content_list(self, key):
        if not isinstance(self.content[key],list):
            return self.content[key]
        else:
            knowledge_list = []
            for index in range(len(self.content[key])):
                knowledge_list.append([key, index])
            return knowledge_list
           
           
    def get_possible_solutions(self):
        with open('./knowledge/files/possible_solutions.json', 'r', encoding='utf-8') as f:
            self.possible_solutions = json.load(f)
        # self.possible_solutions_key_list = []
        # for key, _ in self.possible_solutions.items():
        #     self.possible_solutions_key_list.append(key)

    def get_exp_instruction_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    
    def get_a_service_possible_solutions(self, key, selected_set):
        current_key = key.lower().strip()
        return_list = self.get_a_service_prior_knowledge_solutions(current_key)
        return_list = return_list + self.get_a_service_in_the_wild_exp_solutions(current_key,selected_set)
        return_list = return_list + self.get_a_service_metasploit_exp_solutions(current_key,selected_set)
        
        self.logger.info(f"For {current_key} service, found {len(return_list)} possible solutions","System")
        return return_list


    def get_a_service_metasploit_exp_solutions(self, key, selected_set):
        return_list = []
        for item in self.possible_solutions["metasploit_exp"]:
            if self.task_type.lower().strip() == "shell" and item["path"].startswith("auxiliary"):
                continue
            if self.task_type.lower().strip() == "shell" and item["rank"] != "excellentranking":
                continue
            # if self.task_type.lower().strip() != "shell" and (item["rank"] != "excellentranking" or not item["path"].startswith("auxiliary")):
            #     continue
            if self.task_type.lower().strip() != "shell" and item["path"].startswith("exploit") and item["rank"] != "excellentranking":
                continue
            for name_item in item["name"]:
                if fuzz.partial_ratio(key.lower(), name_item.lower()) > 90:
                    if item["exp_usage_path"] not in selected_set:
                        selected_set.add(item["exp_usage_path"])
                        exp_instruction = self.get_exp_instruction_file(item["exp_usage_path"])
                        return_list.append(["Next Steps ", f"try to deploy exploit scripts ({item['path']}) to achieve our goal (Not started yet)", exp_instruction])
        return return_list
    
    def get_a_service_in_the_wild_exp_solutions(self, key, selected_set):
        return_list = []
        if self.task_type.lower().strip() != "shell":
            return return_list
        for item in self.possible_solutions["in_the_wild_exp"]:
            for name_item in item["name"]:
                if fuzz.partial_ratio(key.lower(), name_item.lower()) > 90:
                    if item["exp_usage_path"] not in selected_set:
                        selected_set.add(item["exp_usage_path"])
                        exp_instruction = self.get_exp_instruction_file(item["exp_usage_path"])
                        return_list.append(["Next Steps ", f"try to deploy self-built exploit scripts for {item['cve'][0]} to achieve our goal (Not started yet)", exp_instruction])
        return return_list


    def get_a_service_prior_knowledge_solutions(self, key):
        return_list = []
        if key in self.possible_solutions["prior_knowledge"]:
            for item in self.possible_solutions["prior_knowledge"][key]:
                if self.task_type.lower().strip() == "shell" and item["type"] != "default":
                    continue
                return_list.append(["Next Steps ", f"try {item['value']} to achieve our goal"])
        return return_list


    def get_service_possible_solutions(self, information):
        selected_set = set()
        # 1. check if a web service
        first_node_split_flag = False
        possible_solutions_list = []
        prompt = PROMPT_CHECK_IF_WEB_SERVICE.format(
            NMAP_RESULT = information
        )
        res = self.llm(prompt)
        self.logger.debug(res)
        matches = re.findall(r"<result>(.*?)</result>", res)
        if len(matches) != 1:
            self.logger.error("error")
            traceback.print_exc()
            exit(0)
        if_web_service = matches[0].lower().strip()
        if if_web_service == "yes":
            possible_solutions_list = possible_solutions_list + self.get_a_service_prior_knowledge_solutions("web")
            first_node_split_flag = True

        # 2. identify the solutions of the given service
        prompt = PROMPT_SERVICE_EXTRACT.format(
            SERVICE_TO_EXTRACT = information
        )
        res = self.llm(prompt)
        self.logger.debug(res)
        matches = re.findall(r"<result>(.*?)</result>", res)
        
        
        if len(matches) == 1 and matches[0].lower().strip() == "none":
            possible_solutions_list = possible_solutions_list + self.get_a_service_prior_knowledge_solutions("unknown")
            first_node_split_flag = True
        else:
            for item in matches:
                if if_web_service == "yes" and (item.lower() == "http" or item.lower() == "https"):
                    continue
                key = item.lower().strip()
                possible_solutions_list = possible_solutions_list + self.get_a_service_possible_solutions(key, selected_set)
        return possible_solutions_list,first_node_split_flag
        
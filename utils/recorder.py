import os
from datetime import datetime
import time
import json

class Recorder:
    def __init__(self, log_file_name = ""):
        self.log_batch = "dev"
        self.log_file_name = log_file_name
        now = datetime.now()
        fixed_time_str = now.strftime(f"%Y-%m-%d-%H-%M-%S")
        self.log_file_path = f"./log"

        if not os.path.exists(self.log_file_path):
            os.makedirs(self.log_file_path)   

        self.log_file_path = f"{self.log_file_path}/{self.log_file_name}.json" 
        self.starttimestamp = time.time()
        self.lasttimestamp = time.time()
        self.execute_time = 0
        self.record_data = {
            "starttimestamp":str(self.starttimestamp),
            "lasttimestamp":str(self.lasttimestamp),
            "execute_time":str(self.execute_time),
            "prompts_num":0,
            "actions_num":0,
            "prompts":[],
            "actions":[],
        }


    def write_llm_query(self, prompt, answer):
        self.record_data["prompts"].append({
            "prompt":prompt,
            "answer":answer,
            "timestamp":self.get_time_stamp(),
            "execute_time":str(self.execute_time)
        })
        self.record_data["prompts_num"] = len(self.record_data["prompts"])
        self.make_persistence()

    def get_time_stamp(self):
        self.lasttimestamp = time.time()
        self.execute_time = self.lasttimestamp - self.starttimestamp
        self.record_data["lasttimestamp"] = str(self.lasttimestamp)
        self.record_data["execute_time"] = str(self.execute_time)
        return str(self.lasttimestamp)

    def write_action_observation(self, action, observation):
        self.record_data["actions"].append({
            "action":action,
            "observation":observation,
            "timestamp":self.get_time_stamp(),
            "execute_time":str(self.execute_time)
        })
        self.record_data["actions_num"] = len(self.record_data["actions"])
        self.make_persistence()

    def make_persistence(self):
        with open(self.log_file_path, "w", encoding="utf-8") as f:
            json.dump(self.record_data, f, ensure_ascii=False, indent=4)

    
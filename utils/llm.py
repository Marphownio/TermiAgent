from openai import OpenAI
from typing import Optional, List
import yaml
import time
import os

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

class BackendLLM():
    def __init__(self, logger, recorder, llm_type):
        self.logger = logger
        self.recorder = recorder
        self.llm_type = llm_type
        self.base_url = config["llm_config"][llm_type]["base_url"]
        self.api_key = config["llm_config"][llm_type]["api_key"]
        self.model_name = config["llm_config"][llm_type]["model"]
        self.temperature = config["llm_config"][llm_type]["temperature"]


    def __call__(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        max_retries = 5
        retry_delay = 5   

        for attempt in range(1, max_retries + 1):
            try:
                base_url = self.base_url
                api_key = self.api_key
                model_name = self.model_name
                temperature = self.temperature
                client : object =  OpenAI(
                    api_key=api_key, 
                    base_url=base_url
                    )
                if temperature:
                    response = client.chat.completions.create(
                        model = model_name,
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant"},
                            {"role": "user", "content": prompt},
                        ],
                        temperature=temperature,
                        stream=False,
                        timeout=1500
                    )
                else:
                    response = client.chat.completions.create(
                        model = model_name,
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant"},
                            {"role": "user", "content": prompt},
                        ],
                        stream=False,
                        timeout=1500
                    )
                self.recorder.write_llm_query(
                    prompt,
                    response.choices[0].message.content
                )
                return response.choices[0].message.content
            except Exception as e:
                self.logger.error(f"Attempt {attempt} failed: {e}")
                if attempt < max_retries:
                    time.sleep(retry_delay)
                    self.logger.info(f"Retrying... ({attempt}/{max_retries})")
                else:
                    self.logger.error("Max retries reached. Exiting.")
                    exit(0)

    @property
    def _llm_type(self) -> str:
        return "BackendLLM"

        
            




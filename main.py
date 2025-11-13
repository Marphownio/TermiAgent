from reasoner.reasoner import Reasoner
from assistant.assistant import Assistant
from executor.executor import Executor
from memory.memory import Memory
from knowledge.knowledge import KnowledgeBase
from utils.llm import BackendLLM
from utils.recorder import Recorder
from utils.logger import Logger
from utils.msg import Msg,Current_Assistant,Phase
import subprocess
from typing import List, TypedDict, Dict
from langgraph.graph import StateGraph, END
import re
import argparse
import json



def phased_target_finish_check(state: Msg):
    if state["action"].strip().lower() == "finish":
        return "reasoner"
    elif state["action"].strip().lower() == "attempt_failed" or state["action"].strip().lower() == "force_failed" or state["action"].strip().lower() == "fail":
        return "memory"
    else:
        return "excutor"

def to_reasoner_check(state: Msg):
    if state["to_reasoner"].strip().lower() == "true":
        return "reasoner"
    else:
        return "assistant"
    
def target_finish_check(state: Msg):
    if state["phased_target"].strip().lower() == "finish":
        return END
    else:
        return "assistant"

if __name__ == "__main__":

    # 0. set args
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("target", help="the taget of penetration machine")
    parser.add_argument("logname", help="the path of output directory")
    parser.add_argument("llmtype", help="LLM name in yaml")
    parser.add_argument("network", help="docker network")
    parser.add_argument("--verbose", action="store_true", help="show detailed information")
    
    args = parser.parse_args()
    target = args.target
    if args.verbose:
    # if True:
        level_set = "DEBUG"
    else:
        level_set = "INFO"
    log_name = args.logname
    llm_type = args.llmtype
    network = args.network
    # 1. Initialize
    
    logger = Logger(name="PentestAgent", level=level_set)
    recorder = Recorder(log_name)
    llm = BackendLLM(logger, recorder, llm_type)
    knowledge_base = KnowledgeBase(logger, llm)
    memory = Memory(llm, logger, recorder, knowledge_base, network)
    reasoner = Reasoner(llm, logger, knowledge_base)
    asssistant = Assistant(llm, logger, knowledge_base, memory)
    executor = Executor(llm, logger, network)
    
    START_MSG = {
        "current_assistant" : None,
        "phase" : Phase.START,
        "target" : str(target),
        "phased_target" : "",
        "context" : "",
        "action" : "",
        "raw_observation" : "",
        "password" : "",
        "summary_hint" : "",
        "to_reasoner" : "false",
        "reference_information": "",
        "task_type": "shell"
    }
    
    # 2. set node and edges
    builder = StateGraph(Msg)

    builder.add_node("reasoner", reasoner)
    builder.add_node("assistant", asssistant)
    builder.add_node("excutor", executor)
    builder.add_node("memory", memory)

    builder.add_conditional_edges("reasoner", target_finish_check)
    builder.add_conditional_edges("assistant", phased_target_finish_check)
    builder.add_edge("excutor", "memory")
    builder.add_conditional_edges("memory", to_reasoner_check)
    # builder.add_edge("memory", "assistant")


    builder.set_entry_point("reasoner")

    # 3. construct graph & start to excute
    graph = builder.compile()
    output = graph.invoke(
        START_MSG,
        config={
            "recursion_limit": 600,
        }
    )
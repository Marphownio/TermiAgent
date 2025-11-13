from typing import TypedDict
from enum import Enum

class Phase(Enum):
    START = 0
    RECONNAISSANCE = 1
    SCANNING = 2
    EXPLOITATION = 3
    FINISH = 4

class Current_Assistant(Enum):
    START = 1
    RECON = 2

class Msg(TypedDict):
    current_assistant: Current_Assistant
    phase: Phase
    target: str
    action: str
    phased_target: str
    tool: str
    cmd: str
    raw_observation: dict
    brief_observation: dict
    context: str
    password: str
    summary_hint: str
    to_reasoner: str
    reference_information: str
    task_type: str
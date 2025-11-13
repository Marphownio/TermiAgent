from reasoner.template import PROMPT_REASONER, PROMPT_TASK_CHECK
from utils.msg import Msg,Current_Assistant,Phase
import re
import traceback


class Reasoner:

    def __init__(self, llm, logger, knowledge_base):
        self.logger = logger
        self.llm = llm
        self.knowledge_base = knowledge_base

    def __call__(self, state: Msg) -> Msg:
        try:
            task_type = state["task_type"]
            if state["to_reasoner"].strip().lower() == "true":
                self.logger.info(f"Back to reasoner for rethinking", "System")
            if state["phase"] == Phase.START:
                self.logger.info(f"Start penetration with overall goal \n## {state['target']}", "System")
                state["phase"] = Phase.RECONNAISSANCE
                prompt = PROMPT_TASK_CHECK.format(
                    OVERALL_GOAL = state["target"],
                    )
                res = self.llm(prompt)
                task_type = self.get_output_josn(res).strip().lower()
                self.knowledge_base.set_task_type(task_type)
            prompt = PROMPT_REASONER.format(
                OVERALL_GOAL = state["target"],
                CONTEXT = state["context"]
                )
            res = self.llm(prompt)
            phased_target = self.get_output_josn(res)
            self.logger.info(f"{phased_target}", "Reasoner")
            new_state = state.copy()
            new_state.update({
                "phased_target": phased_target,
                "action": "",
                "to_reasoner": "false",
                "task_type": task_type
                })
            self.logger.debug(new_state)
            return new_state
            
        except Exception as e:
            raise Exception(e)

    def get_output_josn(self, text):
        # matches = re.findall(r"<assistant>(.*?)</assistant>", text)
        # if len(matches) != 1:
        #     self.logger.error("error")
        #     traceback.print_exc()
        # assistant = matches[0]

        matches = re.findall(r"<target>(.*?)</target>", text)
        if len(matches) != 1:
            self.logger.error("error")
            traceback.print_exc()
        target = matches[0]
        return target

from assistant.template import PROMPT_COMMAND_GENERATION, PROMPT_ACTION_CATEGORY, PROMPT_FINISH_CHECK, KNOWLEDGE_BRANCH_CHECK_PROMPT, EXP_DESCRIPTION_CHECK_PROMPT
from utils.msg import Msg,Current_Assistant,Phase
import re
import traceback


class Assistant:
    def __init__(self, llm, logger, knowledge_base, memory):
        self.logger = logger
        self.llm = llm
        self.knowledge_base = knowledge_base
        self.memory = memory

    def __call__(self, state: Msg) -> Msg:
        try:
            cmd = state["action"]
            summary_hint = ""
            reference_information = ""
            if cmd != "":
                prompt = PROMPT_FINISH_CHECK.format(
                    PHASED_TARGET = state["phased_target"],
                    CONTEXT = state["context"],
                    REFERENCE_INFORMATION = state["reference_information"]
                )
                res = self.llm(prompt)
                reason,cmd = self.get_output_josn(res)
                self.logger.info(f"{reason} <cmd> {cmd} </cmd>", "Assistant")
            if cmd.lower().strip() == "fail":
                pass
            elif cmd.lower() != "finish":
                result = "true"
                if not self.memory.is_on_knowledge_branch():
                    if self.memory.is_exp_node():
                        # get reference
                        reference_information = self.memory.get_exp_instruction_file()
                        if not self.memory.is_checked_exp_node():
                            prompt = EXP_DESCRIPTION_CHECK_PROMPT.format(
                                CONTEXT = state["context"],
                                DESCIRPTION = reference_information
                                )
                            res = self.llm(prompt)
                            reason,cmd = self.get_output_josn(res)
                            self.logger.info(f"{reason} <cmd> {cmd} </cmd>", "Assistant")
                            if cmd.strip().lower() == "false":
                                result = "force_false"
                            else:
                                self.memory.set_exp_knowledge_key_index()
                    else:
                        prompt = PROMPT_ACTION_CATEGORY.format(
                            OVERALL_TARGET = state["target"],
                            PHASED_TARGET = state["phased_target"],
                            CONTEXT = state["context"],
                            ACTION_CATEGORY = ', '.join(self.knowledge_base.key_list)
                            )
                        res = self.llm(prompt)
                        reason,cmd = self.get_output_josn(res)
                        self.logger.info(f"{reason} <cmd> {cmd} </cmd>", "Assistant")
                        knowledge_list = self.knowledge_base.get_reference_content_list(cmd.lower())
                        if isinstance(knowledge_list,list):
                            self.memory.add_child_node_in_knowledge(knowledge_list)
                            current_key, current_index = self.memory.get_knowledge_key_index()
                            reference_information =  self.knowledge_base.get_reference_content(current_key, current_index)
                        else:
                            reference_information = knowledge_list
                else:
                    current_key, current_index = self.memory.get_knowledge_key_index()
                    if self.memory.is_exp_node():
                        reference_information = self.memory.get_exp_instruction_file()
                    else:
                        reference_information =  self.knowledge_base.get_reference_content(current_key, current_index)

                
                if self.memory.is_on_knowledge_branch():
                    prompt = KNOWLEDGE_BRANCH_CHECK_PROMPT.format(
                        CONTEXT = state["context"],
                        REFERENCE_INFORMATION = reference_information
                        )
                    res = self.llm(prompt)
                    reason,result = self.get_output_josn(res)
                    self.logger.info(f"{reason} <result> {result} </result>", "Assistant")
                
                if result.strip().lower() == "false":
                    cmd = "attempt_failed"
                elif result.strip().lower() == "force_false":
                    cmd = "force_failed"
                else:
                    prompt = PROMPT_COMMAND_GENERATION.format(
                        OVERALL_TARGET = state["target"],
                        PHASED_TARGET = state["phased_target"],
                        CONTEXT = state["context"],
                        # TOOLS = self.tools,
                        REFERENCE_INFORMATION = reference_information
                        )
                    res = self.llm(prompt)
                    reason,cmd = self.get_output_josn(res)
                    matches = re.findall(r"<hint>(.*?)</hint>", res)
                    if len(matches) == 0:
                        summary_hint = ""
                    else:
                        summary_hint = matches[0]
                    self.logger.info(f"{reason} <cmd> {cmd} </cmd><hint>{summary_hint}</hint>", "Assistant")
            new_state = state.copy()
            new_state.update({
                "action": cmd,
                "summary_hint": summary_hint,
                "reference_information": reference_information
                })
            self.logger.debug(new_state)
            return new_state
            
        except Exception as e:
            raise Exception(e)

    def get_output_josn(self,text):
        try:
            matches = re.findall(r"<reason>(.*?)</reason>", text)
            if len(matches) != 1:
                self.logger.error("error")
                traceback.print_exc()
            reason = matches[0]
        except Exception as e:
            print(e)
            reason = "None"

            
        matches = re.findall(r"<cmd>(.*?)</cmd>", text)
        if len(matches) != 1:
            self.logger.error("error")
            traceback.print_exc()
        cmd = matches[0]
        return reason,cmd
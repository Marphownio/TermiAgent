import sys
import datetime
import time
import os

class Logger:
    LEVELS = {
        'DEBUG': {'color': '\033[90m'},     # Grey
        'INFO': {'color': '\033[92m'},      # Green
        'WARNING': {'color': '\033[93m'},   # Yellow
        'ERROR': {'color': '\033[91m'},     # Red
    }
    RESET = '\033[0m'
    ROLE = '\033[94m' # Blue

    def __init__(self, name="Logger", level="DEBUG"):
        self.name = name
        self.level = level.upper()
        self.level_order = ["DEBUG", "INFO", "WARNING", "ERROR"]

    def _should_log(self, level):
        return self.level_order.index(level) >= self.level_order.index(self.level)

    def _format(self, level, message, role):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        color = self.LEVELS[level]['color']
        role_part = ""
        if role != "":
            role_part = f"{self.ROLE}[{role}]{self.RESET}"
        if level == "INFO":
            return f"[{now}] {role_part} {color}{message} {self.RESET}"
        return f"[{now}]{color} [{level}] {message}{self.RESET}"

    def debug(self, message, role=""):
        if self._should_log("DEBUG"):
            print(self._format("DEBUG", message, role), file=sys.stdout)

    def info(self, message, role=""):
        if self._should_log("INFO"):
            print(self._format("INFO", message, role), file=sys.stdout)
            # time.sleep(2)

    def warning(self, message, role=""):
        if self._should_log("WARNING"):
            print(self._format("WARNING", message, role), file=sys.stderr)

    def error(self, message, role=""):
        if self._should_log("ERROR"):
            print(self._format("ERROR", message, role), file=sys.stderr)

    def print_tree(self, node, current_node, level=1):
        print_level = level
        if node == current_node:
            print(">>", end="")
            print_level = print_level - 1
        indent = "  " * print_level
        if len(node.brief_context)>0:
            content = node.brief_context[0]
        else:
            content = "node"
        print(f"{indent}- {content}")
        children_list = []
        next_node = node.first_child_node
        while next_node is not None:
            self.print_tree(next_node, current_node, level + 1)
            next_node = next_node.first_peer_node
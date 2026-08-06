# Core types
from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from .exceptions import InvalidAgentError, InvalidExecutorError

class EventType(Enum):
    AGENT_REGISTERED = 1
    EXECUTOR_REGISTERED = 2
    EVENT_RECEIVED = 3

@dataclass
class Agent:
    id: str
    name: str
    def start(self):
        pass
    def stop(self):
        pass

@dataclass
class Executor:
    id: str
    name: str
    def execute(self, event_data: Dict):
        pass
    def start(self):
        pass
    def stop(self):
        pass

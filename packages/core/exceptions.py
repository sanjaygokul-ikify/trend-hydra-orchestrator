# Core exceptions
import logging
from typing import Exception

class HydraCoreException(Exception):
    pass

class InvalidAgentError(HydraCoreException):
    def __init__(self, agent_id: str):
        super().__init__(f'Invalid agent {agent_id}')
        self.logger = logging.getLogger(__name__)
        self.logger.error(f'Invalid agent {agent_id}')

class InvalidExecutorError(HydraCoreException):
    def __init__(self, executor_id: str):
        super().__init__(f'Invalid executor {executor_id}')
        self.logger = logging.getLogger(__name__)
        self.logger.error(f'Invalid executor {executor_id}')
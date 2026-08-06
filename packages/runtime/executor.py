# Runtime executor logic
import logging
from typing import Dict, List
from . import ExecutorRuntime
from ..core.types import Executor, EventType
from ..core.exceptions import InvalidExecutorError

class ExecutorRuntime:
    def __init__(self, executor: Executor):
        self.executor = executor
        self.logger = logging.getLogger(__name__)

    def execute(self, event_data: Dict):
        try:
            self.executor.execute(event_data)
        except Exception as e:
            self.logger.error(f'Error executing executor {self.executor.id}: {e}')
            raise InvalidExecutorError(self.executor.id)

    def start(self):
        self.logger.info(f'Starting executor {self.executor.id}')
        self.executor.start()

    def stop(self):
        self.logger.info(f'Stopping executor {self.executor.id}')
        self.executor.stop()
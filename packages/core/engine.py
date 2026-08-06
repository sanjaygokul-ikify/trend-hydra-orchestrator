# Core engine logic
import logging
from typing import List, Dict
from .types import Agent, Executor, EventType
from .exceptions import InvalidAgentError, InvalidExecutorError

class Engine:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.executors: Dict[str, Executor] = {}
        self.event_handlers: Dict[EventType, List[Executor]] = {}
        self.logger = logging.getLogger(__name__)

    def register_agent(self, agent: Agent):
        self.agents[agent.id] = agent
        self.logger.info(f'Registered agent {agent.id}')

    def register_executor(self, executor: Executor):
        self.executors[executor.id] = executor
        self.logger.info(f'Registered executor {executor.id}')

    def handle_event(self, event_type: EventType, event_data: Dict):
        for executor in self.event_handlers.get(event_type, []):
            try:
                executor.execute(event_data)
            except Exception as e:
                self.logger.error(f'Error executing executor {executor.id}: {e}')

    def add_event_handler(self, event_type: EventType, executor: Executor):
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        self.event_handlers[event_type].append(executor)
        self.logger.info(f'Added event handler for {event_type} to executor {executor.id}')

    def remove_event_handler(self, event_type: EventType, executor: Executor):
        if event_type in self.event_handlers:
            self.event_handlers[event_type] = [e for e in self.event_handlers[event_type] if e.id != executor.id]
            self.logger.info(f'Removed event handler for {event_type} from executor {executor.id}')

    def get_agent(self, agent_id: str) -> Agent:
        return self.agents.get(agent_id)

    def get_executor(self, executor_id: str) -> Executor:
        return self.executors.get(executor_id)

    def start(self):
        self.logger.info('Starting engine')
        for agent in self.agents.values():
            agent.start()
        for executor in self.executors.values():
            executor.start()

    def stop(self):
        self.logger.info('Stopping engine')
        for agent in self.agents.values():
            agent.stop()
        for executor in self.executors.values():
            executor.stop()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def __del__(self):
        self.stop()

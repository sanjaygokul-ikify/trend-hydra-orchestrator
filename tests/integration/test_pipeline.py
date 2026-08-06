import unittest
from packages.core import Engine, Agent, Executor
from packages.services import orchestrator
from packages.utils import logging
logger = logging.get_logger(__name__)
class TestPipeline(unittest.TestCase):
    def test_full_pipeline(self):
        engine = Engine()
        agent = Agent('id', 'name')
        executor = Executor('id', 'name')
        engine.register_agent(agent)
        engine.register_executor(executor)
        orch = orchestrator.Orchestrator()
        orch.start()
        # trigger the pipeline
        # assert the expected output
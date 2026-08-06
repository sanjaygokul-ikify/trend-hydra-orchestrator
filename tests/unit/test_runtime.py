import unittest
from packages.core import Engine
from packages.services import orchestrator
from packages.utils import logging
logger = logging.get_logger(__name__)
class TestRuntime(unittest.TestCase):
    def test_orchestrator_start_stop(self):
        orch = orchestrator.Orchestrator()
        orch.start()
        self.assertTrue(orch.engine.agents)
        orch.stop()
        self.assertFalse(orch.engine.agents)
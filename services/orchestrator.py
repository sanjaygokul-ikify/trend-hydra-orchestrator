from packages.core import Engine
from packages.utils import logging
logger = logging.get_logger(__name__)
class Orchestrator:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        self.engine.start()
    def stop(self):
        self.engine.stop()
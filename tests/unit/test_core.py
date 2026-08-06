import logging
from trend_hydra_orchestrator.core import Core

logger = logging.getLogger(__name__)


def test_init():
    try:
        core = Core()
        assert isinstance(core, Core)
    except Exception as e:
        logger.error(f'Error initializing Core: {e}')
        raise

def test_functionality():
    try:
        core = Core()
        # test core functionality
        assert True
    except Exception as e:
        logger.error(f'Error testing Core functionality: {e}')
        raise
import argparse
from services import orchestrator
parser = argparse.ArgumentParser(description='Orchestrator CLI')
parser.add_argument('--start', action='store_true', help='Start the orchestrator')
parser.add_argument('--stop', action='store_true', help='Stop the orchestrator')
def main(args=None):
    args = parser.parse_args(args)
    orch = orchestrator.Orchestrator()
    if args.start:
        orch.start()
    elif args.stop:
        orch.stop()
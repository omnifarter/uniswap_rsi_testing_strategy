"""Re-export for local CLI discovery (almanak strat run looks for strategy.py in CWD)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from src.strategy.main import UniswapRSIStrategy

__all__ = ["UniswapRSIStrategy"]

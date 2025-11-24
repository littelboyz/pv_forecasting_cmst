"""
CMST: Cross-Modal Spatiotemporal Transformer for Solar Forecasting
"""

__version__ = "1.0.0"
__author__ = "littelboyz"

from src.config import CFG, print_config_summary
from src.utils import set_seed, ensure_dir

__all__ = [
    "CFG",
    "print_config_summary",
    "set_seed",
    "ensure_dir",
]
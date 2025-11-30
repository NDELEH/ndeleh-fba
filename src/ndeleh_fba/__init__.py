"""
ndeleh_fba

Implementation of the Ndeleh Fish Bone Algorithm (N-FBA).

Core concepts:
- Dynamic spine: strongest associative path through the graph.
- Ribs & micro-ribs: branching associative structures around the spine.

Algorithm created by Ndeleh, 2025.
"""

from .graph import Graph
from .spine import SpineResult, SpineStep, build_spine

__all__ = [
    "Graph",
    "SpineResult",
    "SpineStep",
    "build_spine",
]

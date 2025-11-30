# 🌐 API & Usage Guide

## CLI Usage

Run from terminal:

```bash
nfb --seed A

from ndeleh_fba import Graph
from ndeleh_fba.fishbone import build_fishbone

g = Graph()
g.add_edge("A", "B", weight=0.9)
g.add_edge("A", "D", weight=0.6)

result = build_fishbone(g, seed="A")




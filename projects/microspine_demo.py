from ndeleh_fba.fishbone_v2 import build_fishbone_v2
from ndeleh_fba.visualize_microspine import visualize_microspine
from ndeleh_fba import Graph


g = Graph()

# Build a structure that creates a micro-spine
g.add_edge("A", "B", weight=0.9)
g.add_edge("B", "C", weight=0.8)
g.add_edge("C", "D", weight=0.9)

# micro-spine seed
g.add_edge("C", "E", weight=0.85)
g.add_edge("E", "F", weight=0.9)
g.add_edge("F", "G", weight=0.92)

result = build_fishbone_v2(g, seed="A")

visualize_microspine(result)

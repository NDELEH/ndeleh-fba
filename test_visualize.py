from ndeleh_fba import Graph
from ndeleh_fba.fishbone import build_fishbone
from ndeleh_fba.visualize import plot_fishbone

def main():
    g = Graph()
    g.add_edge("A", "B", weight=0.9)
    g.add_edge("B", "C", weight=0.8)
    g.add_edge("C", "D", weight=0.7)
    g.add_edge("A", "E", weight=0.6)
    g.add_edge("E", "F", weight=0.5)
    g.add_edge("C", "H", weight=0.3)
    g.add_edge("H", "I", weight=0.3)

    result = build_fishbone(g, seed="A")
    plot_fishbone(g, result, title="N-FBA Example Visualization")

if __name__ == "__main__":
    main()

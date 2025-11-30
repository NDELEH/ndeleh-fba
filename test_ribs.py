from ndeleh_fba import Graph, build_spine
from ndeleh_fba.ribs import build_ribs


def main():
    g = Graph()

    # Build sample graph with multiple branches
    g.add_edge("A", "B", weight=0.9)
    g.add_edge("B", "C", weight=0.8)
    g.add_edge("A", "D", weight=0.6)
    g.add_edge("D", "E", weight=0.7)
    g.add_edge("C", "F", weight=0.5)
    g.add_edge("B", "G", weight=0.4)
    g.add_edge("E", "H", weight=0.6)
    g.add_edge("H", "I", weight=0.3)

    spine = build_spine(g, seed="A", max_length=5)
    ribs = build_ribs(g, spine, max_depth=3)

    print("\n=== SPINE ===")
    print(spine.nodes)

    print("\n=== RIBS ===")
    for spine_node, rib_dict in ribs.items():
        print(f"\nSpine node {spine_node}:")
        for rib_node, rib_obj in rib_dict.items():
            print(f"  Rib → {rib_node} (score={rib_obj.score:.3f})")
            for child_id, child in rib_obj.children.items():
                print(f"    Micro-rib → {child_id} (score={child.score:.3f})")

if __name__ == "__main__":
    main()

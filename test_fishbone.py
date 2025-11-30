from ndeleh_fba import Graph
from ndeleh_fba.fishbone import build_fishbone


def main():
    g = Graph()

    # Build a richer graph
    g.add_edge("A", "B", weight=0.9)
    g.add_edge("B", "C", weight=0.8)
    g.add_edge("C", "D", weight=0.7)
    g.add_edge("A", "E", weight=0.6)
    g.add_edge("E", "F", weight=0.5)
    g.add_edge("B", "G", weight=0.4)
    g.add_edge("C", "H", weight=0.3)
    g.add_edge("H", "I", weight=0.3)
    g.add_edge("F", "J", weight=0.5)
    g.add_edge("F", "K", weight=0.4)

    fba = build_fishbone(
        g,
        seed="A",
        spine_length=7,
        spine_decay=0.9,
        rib_decay=0.6,
        min_rib_score=0.05,
        max_rib_depth=3
    )

    print("\n=== SPINE ===")
    print(fba.spine_nodes)

    print("\n=== RIBS ===")
    for spine_node, rib_dict in fba.ribs.items():
        print(f"\nSpine Node: {spine_node}")
        for rib_node, rib in rib_dict.items():
            print(f"  Rib → {rib_node} (score={rib.score:.3f})")
            for child_id, child in rib.children.items():
                print(f"    Micro-rib → {child_id} (score={child.score:.3f})")

    print("\n=== MORPHOLOGY ===")
    print(fba.morphology)


if __name__ == "__main__":
    main()

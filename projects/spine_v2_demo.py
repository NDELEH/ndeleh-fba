from ndeleh_fba import Graph, build_fishbone_v2, MorphologyClass


def main() -> None:
    g = Graph()
    # Simple example graph – you can tweak this
    g.add_edge("A", "B", weight=0.9)
    g.add_edge("B", "C", weight=0.8)
    g.add_edge("C", "D", weight=0.7)
    g.add_edge("B", "E", weight=0.6)
    g.add_edge("B", "F", weight=0.5)
    g.add_edge("C", "G", weight=0.85)
    g.add_edge("E", "H", weight=0.9)  # potential micro-spine off B->E

    result = build_fishbone_v2(
        graph=g,
        seed="A",
        max_spine_length=5,
        max_ribs_per_spine_node=3,
        max_depth_micro_spine=3,
        industrial_mode=True,
    )

    print("Seed:", result.seed)
    print("Spine:", [n.node_id for n in result.spine])
    print("Morphology:", result.morphology.name)
    print("Metadata:", result.metadata)
    print()

    for spine_node in result.spine:
        ribs = result.ribs_by_node.get(spine_node.node_id, [])
        if not ribs:
            continue
        print(f"Spine node {spine_node.node_id} has ribs:")
        for r in ribs:
            kind = "micro-spine" if r.depth > spine_node.depth + 1 else "rib"
            print(
                f"  - {r.node_id} (depth={r.depth}, weight={r.weight:.2f}, kind={kind})"
            )


if __name__ == "__main__":
    main()

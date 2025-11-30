from ndeleh_fba import Graph, build_spine


def main():
    g = Graph()

    # Build a tiny example graph (like friends / associations)
    g.add_edge("A", "B", weight=0.9)
    g.add_edge("B", "C", weight=0.8)
    g.add_edge("A", "D", weight=0.5)
    g.add_edge("D", "E", weight=0.7)
    g.add_edge("B", "F", weight=0.4)

    spine = build_spine(g, seed="A", max_length=5, decay=0.9)

    print("Spine nodes:", spine.nodes)
    for step in spine.steps:
        print(f"{step.from_node} -> {step.node_id}, score={step.score:.4f}")


if __name__ == "__main__":
    main()

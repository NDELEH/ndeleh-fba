from ndeleh_fba import Graph

def build_memory_graph():
    """
    Build a small human-like memory network for the simulator.
    You can expand this later.
    """

    g = Graph()

    # PERSONAL MEMORY DEMO
    g.add_edge("Soccer",           "Messi",         weight=0.9)
    g.add_edge("Soccer",           "World Cup",     weight=0.7)
    g.add_edge("Messi",            "Barcelona",     weight=0.8)
    g.add_edge("Barcelona",        "Spain",         weight=0.6)

    g.add_edge("Beer",             "Party",         weight=0.7)
    g.add_edge("Party",            "Friends",       weight=0.8)

    g.add_edge("Tech",             "Python",        weight=0.8)
    g.add_edge("Python",           "Cybersecurity", weight=0.7)
    g.add_edge("Cybersecurity",    "Linux",         weight=0.6)

    g.add_edge("Love",             "Wife",          weight=0.9)
    g.add_edge("Wife",             "Japan",         weight=0.7)
    g.add_edge("Japan",            "Bali",          weight=0.4)

    # CROSS LINKS
    g.add_edge("Friends",          "Soccer",        weight=0.3)
    g.add_edge("World Cup",        "Beer",          weight=0.4)
    g.add_edge("Tech",             "Japan",         weight=0.3)

    return g

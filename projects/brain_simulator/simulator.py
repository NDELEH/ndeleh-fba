from ndeleh_fba.fishbone import build_fishbone
from projects.brain_simulator.memory_graph import build_memory_graph

def simulate_thought(seed: str):
    """
    Runs one thought simulation:
    You think about 'seed' and the brain expands using N-FBA.
    """
    g = build_memory_graph()
    result = build_fishbone(g, seed=seed)
    return result

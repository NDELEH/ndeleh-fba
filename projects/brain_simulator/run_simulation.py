from ndeleh_fba.visualize import plot_fishbone
from projects.brain_simulator.simulator import simulate_thought
from projects.brain_simulator.memory_graph import build_memory_graph

def main():
    seed = input("Enter a thought (e.g., Soccer, Tech, Wife, Beer): ")
    result = simulate_thought(seed)
    print("\nSpine:", result.spine_nodes)
    print("Morphology:", result.morphology)
    print("\nVisualizing thought...\n")

    g = build_memory_graph()
    plot_fishbone(g, result, title=f"Thought Simulation: {seed}")

if __name__ == "__main__":
    main()


# 🦴 Dynamic Spine Builder

The spine is the core of the N-FBA structure.

---

## What is the Spine?

The **spine** is the strongest, most meaningful associative path starting from the seed node.

It represents:

- main thoughts  
- main memory chain  
- dominant connection direction  

The spine guides the entire fishbone.

---

## How the Spine is Built

At each step, we choose the next node that maximizes:

\[
Score = A_i \cdot w_{ij} \cdot \gamma
\]

Where:

- \( A_i \) = activation  
- \( w_{ij} \) = edge weight  
- \( \gamma \) = decay  

We stop when:

- no strong neighbors  
- decay is too small  
- max length reached  

---

## Parameters

| Parameter | Meaning |
|----------|---------|
| `seed` | Starting node |
| `max_length` | How long the spine can be |
| `decay` | Spine decay per step |
| `min_edge_weight` | Minimum weight to count |
| `avoid_cycles` | Avoid revisiting nodes |

---

## Example


This is the main thought path the algorithm follows.


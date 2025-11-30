# 🧠 Ndeleh Fish Bone Algorithm (N-FBA)

This document provides the complete conceptual and mathematical overview of the **Ndeleh Fish Bone Algorithm**, a dynamic associative intelligence model inspired by biological fishbone structures.

---

# 1. Introduction

Humans recall information by association.  
Seeing one person reminds you of another.  
A memory triggers a related idea.  
Thoughts chain into patterns.

N-FBA attempts to capture this phenomenon by:

- building a **spine** — the strongest path of associations  
- growing **ribs** — related secondary ideas  
- generating **micro-ribs** — fading, deep recollections  
- producing a **morphology** — a shape describing the entire memory structure  

This makes N-FBA both **functional** and **interpretive**.

---

# 2. Mathematical Foundation

## 2.1 Activation Propagation

Given a starting node \( S_0 \), activation flows:

\[
A_j = A_i \cdot w_{ij} \cdot \gamma
\]

Where:

- \( w_{ij} \) = edge weight  
- \( \gamma \) = decay factor  
- \( A_i \) = current activation  

---

## 2.2 Spine Search Score

To choose the next spine node:

\[
Score(i \rightarrow j) = A_i \cdot w_{ij} \cdot \gamma
\]

The algorithm repeats this greedily to form the main path.

---

## 2.3 Rib Generation

For each spine node:

\[
R_i = \{ j \mid w_{ij} \cdot A_i \cdot \delta > \tau \}
\]

Where:

- \( \delta \) = rib-decay  
- \( \tau \) = rib score threshold  

---

## 2.4 Recursive Rib Growth

\[
A_{depth+1} = A_{depth} \cdot w \cdot \delta
\]

Micro-ribs fade out naturally.

---

## 2.5 Morphology Metrics

We classify the final fishbone based on:

- spine length  
- average ribs per node  
- rib depth  
- clustering density  

This produces:

- linear  
- rib-heavy  
- clustered  
- curved  
- sparse  

---

# 3. Summary

N-FBA is unique because it is:

- data-driven  
- shape-adaptive  
- interpretable  
- biologically inspired  
- mathematically grounded  

It is the world’s first **fishbone-based associative intelligence algorithm**.


from fastapi import FastAPI
from ndeleh_fba import Graph
from ndeleh_fba.fishbone import build_fishbone
from .schemas import FishboneRequest, FishboneResponse

app = FastAPI(
    title="Ndeleh Fish Bone Algorithm API",
    description="Web API for running the N-FBA associative intelligence algorithm.",
    version="1.0.0"
)


@app.post("/fishbone", response_model=FishboneResponse)
def run_fishbone(req: FishboneRequest):
    g = Graph()

    # Build graph from edges
    for edge in req.edges:
        g.add_edge(edge.src, edge.dst, weight=edge.weight)

    # Run algorithm
    result = build_fishbone(g, seed=req.seed)

    # Serialize ribs
    ribs_serialized = {}
    for spine_node, rib_dict in result.ribs.items():
        ribs_serialized[spine_node] = {
            rib_node: {
                "score": rib.score,
                "children": {
                    child_id: {"score": child.score}
                    for child_id, child in rib.children.items()
                }
            }
            for rib_node, rib in rib_dict.items()
        }

    return FishboneResponse(
        spine=result.spine_nodes,
        morphology=result.morphology,
        ribs=ribs_serialized
    )

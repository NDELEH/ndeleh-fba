from pydantic import BaseModel
from typing import List, Tuple, Dict, Any


class Edge(BaseModel):
    src: str
    dst: str
    weight: float


class FishboneRequest(BaseModel):
    seed: str
    edges: List[Edge]


class FishboneResponse(BaseModel):
    spine: List[str]
    morphology: str
    ribs: Dict[str, Any]

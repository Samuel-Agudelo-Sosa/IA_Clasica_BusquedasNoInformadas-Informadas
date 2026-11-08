from pydantic import BaseModel, Field
from typing import Optional, List, Literal

class SearchRequest(BaseModel):
    problem: str = Field(..., description="Nombre del problema a resolver")
    algorithm: Literal["BFS", "DFS", "DLS", "IDFS", "UCS", "Astar", "Avara"] = Field(..., description="Algoritmo seleccionado")
    control: int = Field(default=3, ge=0, le=3, description="Nivel de control de redundancia (0-3)")
    limit: Optional[int] = Field(default=10, ge=1, description="Límite de profundidad para DLS")


class SearchResponse(BaseModel):
    solution_found: bool
    path_cost: Optional[float] = None
    evaluated_nodes: int
    steps: Optional[int] = None
    path: Optional[List[str]] = Field(default_factory=list, description="Lista de acciones de la solución")
    message: str
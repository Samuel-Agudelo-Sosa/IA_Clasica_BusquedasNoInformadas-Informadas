from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import SearchRequest, SearchResponse


#importación motor de IA:
from backend.core.Problems.MissionariesCannibalsProblem import MissionariesCannibalsProblem
from backend.core.SearchAlgorithms.BFS import BFS
from backend.core.SearchAlgorithms.DFS import DFS
from backend.core.SearchAlgorithms.UCS import UCS
from backend.core.SearchAlgorithms.DLS import DLS
from backend.core.SearchAlgorithms.IDFS import IDFS
from backend.core.SearchAlgorithms.AStar import AStar
from backend.core.SearchAlgorithms.Avara import Avara

app = FastAPI(title="Motor de Búsqueda de IA")

#configuración CORS para permitir peticiones desde index.html local

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Diccionario mapeador para instanciar problemas dinámicamente
PROBLEMS_MAP = {
    "missionaries": MissionariesCannibalsProblem
}



#Diccionario mapeador para instanciar algoritmos dinámicamente
ALGORITHMS_MAP = {
    "BFS": BFS,
    "DFS": DFS,
    "UCS": UCS,
    "DLS": DLS,
    "IDFS": IDFS,
    "AStar": AStar,
    "Avara": Avara
}


@app.get("/")
def home():
    return {"status": "IA Engine API is running"}


@app.post("/search", response_model=SearchResponse)
def execute_search(request: SearchRequest):

   #validación e instanciación problema seleccionado
    problem_class = PROBLEMS_MAP.get(request.problem)
    if not problem_class:
        raise HTTPException(status_code=400, detail=f"Problema '{request.problem}' no soportado.")

    problem_instance = problem_class()

    #validación e instanciación algoritmo seleccionado
    algo_class = ALGORITHMS_MAP.get(request.algorithm)
    if not algo_class:
        raise HTTPException(status_code=400, detail=f"Algoritmo '{request.algorithm}' no soportado.")

    if request.algorithm == "DLS":
        search_engine = algo_class(control=request.control, limit=request.limit)
    else:
        search_engine = algo_class(control=request.control)

    solution_node = search_engine.search(problem_instance)
    evaluated_count = search_engine.evaluated_nodes    
    if solution_node is not None:
        path_actions = [str(action) for action in solution_node.solution()]
        path_cost = solution_node.path_cost
        steps_count = len(path_actions)

        return SearchResponse(
            solution_found=True,
            path_cost= path_cost,
            evaluated_nodes= evaluated_count,
            steps = steps_count,
            path=path_actions,
            message=f"Solución encontrada con exito usando {request.algorithm}"

        )
    else:
        return SearchResponse(
            solution_found=False,
            path_cost=0.0,
            evaluated_nodes=evaluated_count,
            steps=0,
            path=[],
            message=f"No se encontró solución con el algoritmo {request.algorithm} y control {request.control}."
        )
    

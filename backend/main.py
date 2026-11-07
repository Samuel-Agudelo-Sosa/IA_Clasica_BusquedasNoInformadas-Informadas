from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import SearchRequest, SearchResponse

app = FastAPI(title="Motor de Búsqueda de IA")

#configuración CORS para permitir peticiones desde tu index.html local

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "IA Engine API is running"}


@app.post("/search", response_model=SearchResponse)
def execute_search(request: SearchRequest):
   
    print(f"Petición recibida: Resolver {request.problem} usando {request.algorithm}")

    return SearchResponse(
        solution_found=True,
        path_cost =11.0,
        evaluated_nodes=42,
        steps=5,
        message="Simulación exitosa. Aquí conectaremos tu motor real."
    )

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from Node import Node
from Search import Search
from SearchAlgorithms.DLS import DLS


class  IDFS(Search):

    def __init__(self, max_limit=float("inf"),  control=3):
        super().__init__(control=control)
        self.max_limit = max_limit


    def search(self, problem):
        self.evaluated_nodes = 0
        depth = 0

        while depth <= self.max_limit:
             dls = DLS(limit=depth, control = self.control)
             resultado = dls.search(problem)

             self.evaluated_nodes += dls.evaluated_nodes

             if isinstance(resultado, Node): # se encontró solución
                return resultado

             if resultado is None: #El espacio de estados se exploró entero y no hubo ramas podadas, es decir no hay solución en ningún nivel
                  return None

             depth += 1 #hubo cutoff (podas), entonces se incrementa la profundidad para la siguiente iteracíon

        return None


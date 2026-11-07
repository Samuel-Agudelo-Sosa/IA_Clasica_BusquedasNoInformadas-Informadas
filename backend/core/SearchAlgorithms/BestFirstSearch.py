import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import heapq # minheap
from Node import Node
from Search import Search

class BestFirstSearch(Search):

    def __init__(self, f):
        super().__init__()
        self.f = f

    def search(self, problem):
        self.evaluated_nodes = 0
        current_node = Node(problem.initial)

        order_arrival = 0
        frontier = []
        heapq.heappush(frontier, (self.f(current_node, problem), order_arrival, current_node ))
        explored = set()

        while frontier:
            cost, _, current_node =  heapq.heappop(frontier)

            if self.control == 3 and current_node.state in explored: # el nodo ya fue evaluado con menor costo, se omite
                continue

            self.evaluated_nodes += 1

            if problem.is_goal(current_node.state):
                return current_node

            if self.control == 3: 
                explored.add(current_node.state) # no agregamos directamente sus hijos al explored, sino que lo hacemos cuando se expande el nodo, para permitir que se puedan generar los mismos nodos hijos con diferentes costos y que se puedan evaluar si son mejores que los ya evaluados.

            for child in current_node.expand(problem):
                if self.is_valid(child, current_node, explored):
                    order_arrival += 1
                    heapq.heappush(frontier, (self.f(child, problem), order_arrival, child))

        return None
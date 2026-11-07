import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from Node import Node
from Search import Search


class  DLS(Search):

    def __init__(self, limit=10,  control=3):
        super().__init__(control=control)
        self.limit = limit

    def search(self, problem):
        self.evaluated_nodes = 0
        current_node = Node(problem.initial)

        frontier = [current_node]
        explored = {current_node.state} if self.control == 3 else set()
        cutoff_ocurred = False #bandera qu indica si se podó una rama por límite

        while frontier:
            current_node = frontier.pop()
            self.evaluated_nodes += 1

            if problem.is_goal(current_node.state):
                return current_node

            if current_node.depth < self.limit:
                for child in reversed(current_node.expand(problem)):
                    if self.is_valid(child, current_node, explored):
                        if self.control == 3:
                            explored.add(child.state)
                        frontier.append(child)
            else:
                if problem.actions(current_node.state): # si llegamos al límite y el nodo tiene posibilidad de expandirse se marca cutoff
                    cutoff_ocurred = True

        #retornamos cutoff como string si se podó por límite, o None si el espacio se agotó
        return "cutoff" if cutoff_ocurred else None
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from collections import deque
from Node import Node
from Search import Search

class BFS(Search):

    def search(self, problem):
        self.evaluated_nodes = 0
        current_node = Node(problem.initial)


        frontier = deque([current_node])  
        explored = {current_node.state} if self.control == 3 else set()  

        while frontier:
            current_node = frontier.popleft()
            self.evaluated_nodes += 1


            if problem.is_goal(current_node.state): # la expansión teórica según el curso comienza desde acá primer pasó es ver si es meta
                return current_node

            for child in current_node.expand(problem):  # este expansión es más un obtener los hijos.

                if self.is_valid(child, current_node, explored):
                    if self.control == 3:
                        explored.add(child.state)
                    frontier.append(child)
        return None

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from Node import Node
from Search import Search


class  DFS(Search):

    def search(self, problem):
        self.evaluated_nodes = 0
        current_node = Node(problem.initial)

        frontier = [current_node] #usamos lista como pila LIFO normal
        explored = {current_node.state} if self.control == 3 else set()

        while frontier:
            current_node = frontier.pop() #extrae del extremo derecho
            self.evaluated_nodes += 1

            if problem.is_goal(current_node.state):
                return current_node

            for child in reversed(current_node.expand(problem)): #para que funcione como lifo  y el primer hijo quede en el tope
                if self.is_valid(child, current_node, explored):
                    if self.control == 3:
                        explored.add(child.state)
                    frontier.append(child)

        return None


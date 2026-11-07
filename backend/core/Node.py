from collections import deque

class Node:

    def __init__(self, state , parent = None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0 if parent is None else parent.depth + 1


    def expand(self, problem): #este expandir no es el teórico, es solo generar los hijos, porque el primer paso de expandir es verificar que es meta
        return [

            Node(state = problem.result(self.state, action),
            parent = self,
            action = action,
            path_cost =  self.path_cost + problem.step_cost(self.state, action, problem.result(self.state, action))

              )
              for action in problem.actions(self.state)
        ]

    def path(self):
        #retorna lista de nodos desde la raíz hasta el nodo actual:
        node, path_back = self, deque()
        while node:
            path_back.appendleft(node) #agrega al inicio convierte la estructura en LIFO
            node = node.parent
        return list(path_back)

    def solution(self):
        return [n.action for n in self.path() if n.action is not None]



    def __repr__(self):
        return f"<Node {self.state}>"


    def __eq__(self, other): #mira que lo que se compara sea otro nodo, solo mira estados ignora diferente padre, costo, o profundidad
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self): #permite calcular un valor único (hash) por cada objeto para insertarlo dentro de sets, dicts...
        return hash(self.state)

from abc import ABC, abstractmethod

#Se define clase abstracta (funcionará como una interfaz)
class Problem(ABC):

    def __init__(self, initial, goal = None, possible_actions = None):
        self.initial = initial
        self.goal = goal
        self.possible_actions = possible_actions 

    @abstractmethod
    def actions(self, state):
        #Retorna acciones ejecutables desde el estado actual
        pass

    @abstractmethod
    def result(self, state, action):
        #Retorna el nuevo estado resultante de aplicar la acción al estado dado
        pass

    def step_cost(self, state, action, next_state):
        return 1

    def is_goal(self, state):
        return state == self.goal

    def heuristic(self, state):
        #Estima el costo desde el estado actual hasta el estado objetivo (para algoritmos informados)
        
        return 0

    
        
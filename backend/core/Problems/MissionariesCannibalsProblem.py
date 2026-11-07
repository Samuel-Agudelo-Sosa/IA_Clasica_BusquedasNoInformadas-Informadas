import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from Problem import Problem

# State = (#misioneros_orilla_izquierda, #canibales_orilla_izquierda, #bote_orilla_izquierda)
# initial state = (3, 3, 1)
# goal/final state = (0, 0, 0)

class MissionariesCannibalsProblem(Problem):
    def __init__(self, initial=(3,3,1), goal=(0,0,0), possible_actions = [(1,0), (2,0), (0,1), (0,2), (1,1)]):
        super().__init__(initial, goal, possible_actions)

    def is_valid(self, state):
        m, c, boat = state
        if not (0 <= m <= 3 and 0 <= c <= 3 and  0 <= boat <= 1):
            return False
        if m > 0  and m < c :
            return False

        m_right, c_right = 3 - m, 3 - c
        if m_right > 0 and m_right  < c_right: #orilla derecha tampoco pueden haber más canibales
            return False

        return True

    def actions(self, state):
        valid_action = []

        for move in self.possible_actions:
            next_state = self.result(state, move)
            if self.is_valid(next_state):
                valid_action.append(move)

        return valid_action

    def result(self, state, action):
        m, c, boat = state
        dm, dc = action

        if boat == 1: 
            return (m - dm, c - dc, 0)
        else:
            return (m + dm, c + dc, 1)

    def heuristic(self, state):
        m, c, boat = state
        return (m + c) / 2  # Estimación del costo desde el estado actual hasta el estado objetivo (para algoritmos informados)
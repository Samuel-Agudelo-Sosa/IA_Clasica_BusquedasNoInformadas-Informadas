import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from BestFirstSearch import BestFirstSearch

class AStar(BestFirstSearch):

    def __init__(self):
        super().__init__(f=lambda node, problem: problem.heuristic(node.state) + node.path_cost)


import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from backend.core.SearchAlgorithms.BestFirstSearch import BestFirstSearch

class UCS(BestFirstSearch):

    def __init__(self):
        super().__init__(f=lambda node, problem: node.path_cost)


from abc import ABC, abstractmethod

class Search(ABC):
    #Clase abstracta para estrategias de búsqueda:

    def __init__(self, control=3):
        self.control = control
        self.evaluated_nodes = 0

    def is_valid(self, child, node, explored):
        #Filtro genérico de redundancia heredado por todos los algoritmos


        #Evitar regresar al padre directo (Abuelo)
        if self.control == 1 and node.parent and child == node.parent: #nodo.parent solito comprueba que el abuelo no sea None
            return False

        #Evita ciclos en la rama actual(Ancestros)
        if self.control == 2:
            currentNode = node
            while currentNode:
                if currentNode == child:
                    return False
                currentNode = currentNode.parent

        #Filtro global en Tabla Hash / Set O(1), el set internamente hace la misma tabla hash que la tabla hash en python

        if self.control == 3 and child.state in explored:
            return False

        

        return True

    @abstractmethod
    def search(self, problem):
        pass
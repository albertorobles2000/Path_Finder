import abc
from abc import ABC, abstractmethod
from Node import Node

class pathFindingAlgorithm(ABC):
    def __init__(self, map):
        self.mapa =  map
        self.open = []
        self.closed = []
        self.start_node = Node(self.mapa.getStart(),None)
        self.objective_node = Node(self.mapa.getObjective(),None)
        self.open.append(self.start_node)

    def getOpen(self):
        return self.open

    def getClosed(self):
        return self.closed

    def IsEnd(self):
        self.open.sort()
        if len(self.open) == 0 or self.open[0]==self.objective_node:
            return True
        else:
            return False

    def getPath(self):
        path = []
        current_node = self.open[0].parent
        path = []
        while current_node != self.start_node:
            path.append(current_node.position)
            current_node = current_node.parent

        #path.append(self.start_node.position)
        return path[::-1]

    def add_to_open(self,neighbor):
        for node in self.open:
            if (neighbor == node and neighbor.f >= node.f):
                return False
        return True

    @abstractmethod
    def nextStep(self):
        pass

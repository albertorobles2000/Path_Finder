from map import Map
import math

# This class represents a node
class Node:
    # Initialize the class
    def __init__(self, position:(), parent:()):
        self.position = position
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f

    def calculateValues(self, start, objective):
        self.g = math.sqrt(abs(self.position[0] - start.position[0])**2 + abs(self.position[1] - start.position[1])**2)
        self.h = math.sqrt(abs(self.position[0] - objective.position[0])**2 + abs(self.position[1] - objective.position[1])**2)
        self.f = self.g + self.h


# A* search
class astar:
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
        current_node = self.open[0]
        path = []
        while current_node != self.start_node:
            path.append(current_node.position)
            current_node = current_node.parent

        path.append(self.start_node.position)
        return path[::-1]


    def nextStep(self):
        self.open.sort()
        current_node = self.open.pop(0)
        self.closed.append(current_node)

        if current_node == self.objective_node:
            print("END")
        else:
            # Unzip the current node position
            (x, y) = current_node.position
            # Get neighbors
            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            # Loop neighbors
            for next in neighbors:
                # Get value from map
                map_value = self.mapa.getValue(next)
                # Check if the node is a wall
                neighbor = Node(next, current_node)
                if(self.mapa.IsNextStepPossible(next) and (neighbor in self.closed)==False):
                # Generate heuristics (Manhattan distance)
                    neighbor.calculateValues(self.start_node,self.objective_node)
                    # Check if neighbor is in open list and if it has a lower f value
                    if(add_to_open(self.open, neighbor) == True):
                        # Everything is green, add neighbor to open list
                        self.open.append(neighbor)

def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True

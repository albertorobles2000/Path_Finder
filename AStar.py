from map import Map
from PathFindingAlgorithm import pathFindingAlgorithm, Node
import math



# A* search
class AStar(pathFindingAlgorithm):
    def calculateValueOfNextNode(self, neighbor, start, objective):
        FromStart = math.sqrt(abs(neighbor.position[0] - start.position[0])**2 + abs(neighbor.position[1] - start.position[1])**2)
        FromEnd = math.sqrt(abs(neighbor.position[0] - objective.position[0])**2 + abs(neighbor.position[1] - objective.position[1])**2)
        neighbor.f = FromStart + FromEnd

    def nextStep(self):
        self.open.sort()
        current_node = self.open.pop(0)
        self.closed.append(current_node)

        if current_node == self.objective_node:
            pass
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
                    self.calculateValueOfNextNode(neighbor, self.start_node,self.objective_node)
                    # Check if neighbor is in open list and if it has a lower f value
                    if(self.add_to_open(neighbor) == True):
                        # Everything is green, add neighbor to open list
                        self.open.append(neighbor)

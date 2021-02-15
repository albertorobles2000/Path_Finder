import numpy as np

class Map:
    def __init__(self, size):
        self.matrix =  np.empty(size, dtype='str')
        self.start = None
        self.objective = None
        for i in range(size[0]):
            for j in range(size[1]):
                if(i==0 or j==0 or i==(size[0]-1) or j==(size[1]-1)):
                    self.matrix[i][j] = 'W'
                else:
                    self.matrix[i][j] = 'F'

    def setStart(self,start):
        ok=False
        if self.matrix[start[0]][start[1]] == 'F':
            self.start = start
            self.matrix[start[0]][start[1]] = 'S'
            ok = True
        return ok

    def setObjective(self,objective):
        ok=False
        if self.matrix[objective[0]][objective[1]] == 'F':
            self.objective = objective
            self.matrix[objective[0]][objective[1]] = 'G'
            ok=True
        return ok

    def setWall(self,wall):
        if(wall!=self.start and wall!=self.objective):
            self.matrix[wall[0]][wall[1]] = 'W'

    def setOpen(self,open):
        if(open!=self.start and open!=self.objective):
            self.matrix[open[0]][open[1]] = 'O'

    def setClosed(self,closed):
        if(closed!=self.start and closed!=self.objective):
            self.matrix[closed[0]][closed[1]] = 'C'

    def setPath(self,path):
        if(path!=self.start and path!=self.objective):
            self.matrix[path[0]][path[1]] = 'P'

    def getValue(self,pos):
        return self.matrix[pos[0]][pos[1]]

    def getSize(self):
        return (self.matrix.shape)

    def getStart(self):
        return (self.start)

    def getObjective(self):
        return (self.objective)

    def getNumberOfRows(self):
        return (self.matrix.shape[0])

    def getNumberOfColums(self):
        return (self.matrix.shape[1])

    def IsNextStepPossible(self,pos):
        if(self.matrix[pos[0]][pos[1]]!='W'):
            return True
        else:
            return False

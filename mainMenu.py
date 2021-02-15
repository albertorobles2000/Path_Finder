import pygame
class Rectangle():
    def __init__(self,x=0,y=0,width=0,height=0, margin=0, color=(0,0,0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.margin = margin
        self.color = color
        self.font = None
        self.text = ''

    def draw(self,screen,text_color = (0,0,0)):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect, self.margin)

        if(self.text != ''):
            text = self.font.render(self.text, True, text_color)
            text_rect = text.get_rect(center=(self.x+(self.width/2), self.y+(self.height/2)))
            screen.blit(text,text_rect)

    def AddText(self,text="", font='freesansbold.ttf', size=12):
        self.font = pygame.font.SysFont(font, size)
        self.text = text


#text = font.render("You win!", True, BLACK)
#text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
#screen.blit(text, text_rect)

    def IsOverTheRectangle(self,click):
        clicked = False
        if click[0] >= self.x and click[0] <= (self.x + self.width) and click[1] >= self.y and click[1] <= (self.y + self.height):
            clicked = True

        return clicked


class mainMenu():

    def __init__(self, screen, algorithms):
        self.screen = screen
        self.algorithmSelected = 0
        self.AlgorithmsRectangle = None
        self.pathFindingAlgorithms = []
        self.Start = None
        self.StartBG = None
        self.Algorithms = algorithms

        self.colors = [(50,50,50),(30,0,200),(100,30,100),(131,252,40)]
        self.background = pygame.image.load("images/background.png")

        #state = ['startMenu','pickStart','pickEnd','drawWalls','algorithmRunning','end','kill']
    def MainMenuConfiguration(self):
        pos = ((self.screen.get_width()/100)*10, (self.screen.get_height()/100)*10)
        size = ((self.screen.get_width()/100)*80, (self.screen.get_height()/100)*38)
        self.AlgorithmsRectangle = Rectangle(pos[0],pos[1],size[0],size[1],margin=0,color=self.colors[0])

        posAnterior = (pos[0]+2, pos[1]+2)
        sizeAnterior = (size[0]-4, size[1]-4)
        for i in range(len(self.Algorithms)):
            pos = (posAnterior[0], posAnterior[1]+i*(sizeAnterior[1]/len(self.Algorithms)))
            size = (sizeAnterior[0], (sizeAnterior[1]/len(self.Algorithms)))
            nuevo = Rectangle(pos[0],pos[1],size[0],size[1],margin=3,color=self.colors[1])
            nuevo.AddText(text=self.Algorithms[i],font='freesansbold.ttf',size=35)
            self.pathFindingAlgorithms.append(nuevo)


        pos = ((self.screen.get_width()/100)*30, (self.screen.get_height()/100)*65)
        size = ((self.screen.get_width()/100)*40, (self.screen.get_height()/100)*20)
        self.StartBG = Rectangle(pos[0],pos[1],size[0],size[1],margin=0,color=self.colors[0])
        self.Start = Rectangle(pos[0]+2,pos[1]+2,size[0]-4,size[1]-4,margin=3,color=self.colors[1])
        self.Start.AddText(text='Start',font='freesansbold.ttf',size=35)


    def DrawMainMenu(self, event):
        end = False
        rawColor=0
        readyColor=1
        specialColor=2
        selectedColor=3
        mousePosition = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            posClick = mousePosition
            for i in range(len(self.pathFindingAlgorithms)):
                if self.pathFindingAlgorithms[i].IsOverTheRectangle(posClick):
                    self.algorithmSelected = i
            if self.Start.IsOverTheRectangle(posClick):
                    end = True


        for i in range(len(self.pathFindingAlgorithms)):
            if i==self.algorithmSelected:
                self.pathFindingAlgorithms[i].color = self.colors[selectedColor]
            elif self.pathFindingAlgorithms[i].IsOverTheRectangle(mousePosition):
                self.pathFindingAlgorithms[i].color = self.colors[specialColor]
            else:
                self.pathFindingAlgorithms[i].color = self.colors[readyColor]
        if self.Start.IsOverTheRectangle(mousePosition):
            self.Start.color = self.colors[specialColor]
        else:
            self.Start.color = self.colors[readyColor]



        #INSIDE OF THE GAME LOOP
        self.screen.blit(self.background, (0, 0))
        #self.screen.fill((200,100,20))
        self.AlgorithmsRectangle.draw(self.screen)
        for rectangle in self.pathFindingAlgorithms:
            rectangle.draw(self.screen,text_color=(255,255,255))
        #self.Grid.draw(self.screen)
        self.StartBG.draw(self.screen)
        self.Start.draw(self.screen,text_color=(255,255,255))

        return end

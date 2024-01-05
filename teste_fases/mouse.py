import pygame

class Mouse:

    def __init__(self):

        #posições
        self.x = 0
        self.y = 0

        #estado dos botões
        self.pressionado = False

        #demais variaveis relevantes
        self.item = False           #guarda de um item está sendo "segurado"

    def update(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.pressionado = pygame.mouse.get_pressed()[0]

    def setPressionado(self, pressionado):
        self.pressionado = pressionado

    def getPressionado(self):
        return self.pressionado

    #tesste para usar tuplas
    def getCoordenadas(self):
        return self.x, self.y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getItem(self):
        return self.item

    def setItem(self, item):
        self.item = item
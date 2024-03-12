import pygame
#import random      #bobagem quente

class Botao:

    #__init__ é o metodo contrutor e os parametros são iniciados aqui
    def __init__(self, x, y, largura, altura, imagem, tela, cor):

        #posição e dimensão
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

        #imagem
        if (imagem):
            self.imagem = pygame.image.load(imagem)  #!!!DEVE SER CARREGADO ASSIM, CASO CONTRARIO SERÁ UMA STRING
            self.imagem = pygame.transform.scale(self.imagem, (largura, altura))
            self.imagem.set_colorkey(cor)   #torna transparente a cor dana no parametro
        else:
            self.imagem = None

        #necessário para desenhar na tela
        self.tela = tela

        # para fazer uma lista encadeada ser possivel
        self.proximo = None

        #bobagem
        #self.x = random.randrange(0, 1020)
        #self.y = random.randrange(0, 520)

    #retorna se o mouse esta dentro da area do botao
    def mouse_dentro(self, mouseX, mouseY):

        if mouseX > self.x and mouseX < self.x + self.largura and mouseY > self.y and mouseY < self.y + self.altura:
            return True
        else:
            return False

    #retorna se o objeto foi clicado ou não
    def clicado(self, mouseX, mouseY, pressionado):

        clicou = False

        if pygame.mouse.get_pressed()[0] and not pressionado:
             if mouseX > self.x and mouseX < self.x + self.largura and mouseY > self.y and mouseY < self.y + self.altura:

                 clicou = True

        return clicou


    def desenha(self):
        if self.imagem:
            self.tela.blit(self.imagem, (self.x, self.y))

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def getProximo(self):
        return self.proximo

    def setProximo(self, proximo):
        self.proximo = proximo

    def getAltura(self):
        return self.altura

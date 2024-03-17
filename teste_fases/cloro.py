import pygame

class Cloro:

    def __init__(self,x, y, largura, altura, imagem, tela, cor):

        #posição e dimensão
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

        #imagem
        self.imagem = pygame.image.load(imagem)  #!!!DEVE SER CARREGADO ASSIM, CASO CONTRARIO SERÁ UMA STRING
        self.imagem = pygame.transform.scale(self.imagem, (largura, altura))
        self.imagem.set_colorkey(cor)   #torna transparente a cor dada no parametro

        #necessário para desenhar na tela
        self.tela = tela

    def desenha(self):
        self.tela.blit(self.imagem, (self.x, self.y))

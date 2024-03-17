import random

import pygame

class Sujeira:

    #__init__ é o metodo contrutor e os parametros são iniciados aqui
    def __init__(self,largura, altura, imagem, tela, cor, limite_esquerdo, limite_direito, limite_superior, limite_inferior):

        #posição e dimensão
        self.x = random.randint(limite_esquerdo + 1, limite_direito - 1)
        self.y = random.randint(limite_superior + 1, limite_inferior - 1)
        self.largura = largura
        self.altura = altura

        #limites do ambiente onde as sujeiras podem circular
        self.lim_esq = limite_esquerdo
        self.lim_dir = limite_direito
        self.lim_sup = limite_superior
        self.lim_inf = limite_inferior

        #imagem
        self.imagem = pygame.image.load(imagem)  #!!!DEVE SER CARREGADO ASSIM, CASO CONTRARIO SERÁ UMA STRING
        self.imagem = pygame.transform.scale(self.imagem, (largura, altura))
        self.imagem.set_colorkey(cor)   #torna transparente a cor dada no parametro

        #necessário para desenhar na tela
        self.tela = tela

    def desenha(self):
        direcaox = random.choice([-1, 0, 1])
        direcaoy = random.choice([-1, 0, 1])
        if self.x + direcaox < self.lim_dir and self.x + direcaox > self.lim_esq:
            self.x = self.x + direcaox
        if self.y + direcaoy < self.lim_inf and self.y + direcaoy > self.lim_sup:
            self.y = self.y + direcaoy

        self.tela.blit(self.imagem, (self.x, self.y))

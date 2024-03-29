import pygame
import random

class Asteroid:

    def __init__(self):

        self.largura = 16 * 8
        self.altura = 16 * 8

        self.largura_tela = 1280
        self.altura_tela = 720

        self.x = random.randint(0 - self.largura*5, 1280 + self.largura*5)
        if self.x <= -self.largura or self.x >= 1280 + self.largura:
            self.y = random.randint(0 - self.altura*5, 720 + self.altura*5)
        else:
            self.y = random.choice([random.randint(0 - self.altura*5, 0 - self.altura), random.randint(720 + self.altura, 720 + self.altura*5)])

        velocidade = 4

        if self.x >= 1280 / 2:
            self.direcaox = random.random()*-velocidade
        else:
            self.direcaox = random.random()*velocidade

        if self.y >= 720 / 2:
            self.direcaoy = random.random()*-velocidade
        else:
            self.direcaoy = random.random()*velocidade

        self.imagem = pygame.image.load("imagens/sujeira_grande.png")
        self.imagem = pygame.transform.scale(self.imagem, (self.largura,self.altura))
        self.rect = self.imagem.get_rect()
        self.mask = pygame.mask.from_surface(self.imagem)


    def desenha(self, tela):
        tela.blit(self.imagem, (self.x, self.y))

    def update(self, escudo_mask, escudo_x, escudo_y):
        #acrescenta a direção a suaposição para que ele se mova
        self.x += self.direcaox
        self.y += self.direcaoy

        """print(self.x)
        print(self.y)"""

        #MOVIMENTAÇÃO ESTILO ASTEROIDS
        acrecimoObjeto = 16 * 8 * 2
        acrecimoComparacao = 16 * 8 * 2 + 1

        #faz com que a sujeira volte em outro canto da tela
        if self.x > self.largura_tela + acrecimoComparacao:
            self.x -= self.largura_tela + acrecimoObjeto * 2      #esquerda
        elif self.x < 0 - acrecimoComparacao:
            self.x += self.largura_tela + acrecimoObjeto        #direita

        if self.y > self.altura_tela + acrecimoComparacao:
            self.y -= self.altura_tela + acrecimoObjeto * 2       #cima
        elif self.y < 0 - acrecimoComparacao:
            self.y += self.altura_tela + acrecimoObjeto         #baixo


        #FUNCIONAMENTO DO ESCUDO
        if self.mask.overlap(escudo_mask, [escudo_x - self.x, escudo_y - self.y]):
            self.direcaox *= -1
            self.direcaoy *= -1




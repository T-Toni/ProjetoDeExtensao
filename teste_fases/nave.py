import pygame
import math

class Projetil:
    def __init__(self, x, y, velocidade_x, velocidade_y):
        self.x = x
        self.y = y
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y

        self.largura = 8
        self.altura = 8

        self.imagem = pygame.image.load("imagens/particula_cloro.png")
        self.imagem = pygame.transform.scale(self.imagem, (self.largura , self.altura))
        #self.imagem.set_colorkey(cor)   #torna transparente a cor dana no parametro


    def atualizar(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))

class Nave:
    def __init__(self, x, y, largura, altura, imagem, tela, cor):
        #posição e dimensão
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

        #imagem
        self.imagem = pygame.image.load(imagem)
        self.imagem = pygame.transform.scale(self.imagem, (largura, altura))
        self.imagem.set_colorkey(cor)
        #retangulo da imagem
        self.imagem_rect = self.imagem.get_rect(center=(x, y))

        #copia da imagem
        self.copia = self.imagem.copy()
        #copia do retangulo
        self.copia_rect = self.copia.get_rect(center=(x, y))

        #ESCUDO

        self.escudo = pygame.image.load("imagens/escudo.png")
        self.escudo = pygame.transform.scale(self.escudo, (15 * 8, 15 * 8))
        self.escudo_rect = self.escudo.get_rect(center=(x, y))
        self.escudo_mask = pygame.mask.from_surface(self.escudo)

        #angulo
        self.angulo = 0

        #necessário para desenhar na tela
        self.tela = tela

        # Lista para armazenar os projéteis
        self.vetor_projeteis = []


    def desenha(self):
        #desenha a nave
        self.tela.blit(self.copia, self.copia_rect)

        #desenha o escudo
        self.tela.blit(self.escudo, self.escudo_rect)


        """#determina a frente da nave
        frente_x = self.copia_rect.centerx + (self.largura / 2) * math.cos(math.radians(-self.angulo))
        frente_y = self.copia_rect.centery + (self.largura / 2) * math.sin(math.radians(-self.angulo))

        # Desenha um quadrado vermelho na frente da nave
                                                    #- 4 para que fique centralizado
        pygame.draw.rect(self.tela, (255, 0, 0), (frente_x - 4, frente_y - 4, 10, 10))"""

        # Atualiza a posição dos projéteis
        for projetil in self.vetor_projeteis:
            projetil.atualizar()

            # Desenha os projéteis
            projetil.desenhar(self.tela)


    def rotaciona(self, incremento):
        #adiciona incremento ao angulo
        self.angulo += incremento

        #rotaciona a imagem
        self.copia = pygame.transform.rotate(self.imagem, self.angulo)
        self.copia_rect = self.copia.get_rect(center = self.imagem_rect.center)

    def atirar(self):
        #determina a posição da frente da nave
        frente_x = self.copia_rect.centerx + (self.largura / 2) * math.cos(math.radians(-self.angulo))
        frente_y = self.copia_rect.centery + (self.largura / 2) * math.sin(math.radians(-self.angulo))

        #gera a direção do projetil
                #aponta inicialmente para direita           x pega o [0] do vetor, y o [1]
        direcao_x = 5 * pygame.math.Vector2(1, 0).rotate(-self.angulo)[0]
        direcao_y = 5 * pygame.math.Vector2(1, 0).rotate(-self.angulo)[1]

        #velocidade
        velocidade = 2

        #cria o projetil logo a frente da nave
        projetil = Projetil(frente_x, frente_y, direcao_x * velocidade, direcao_y * velocidade)

        #adiciona o projetil a lista
        self.vetor_projeteis.append(projetil)

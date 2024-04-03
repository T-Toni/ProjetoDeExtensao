import pygame
import math
import random

"""class Projetil:
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
        tela.blit(self.imagem, (self.x, self.y))"""

class Rastro:
    def __init__(self, x, y, tela, direcaoX, direcaoY):
        self.x = x
        self.y = y
        self.imagem = pygame.image.load("imagens/particula_cloro.png")
        self.imagem = pygame.transform.scale(self.imagem, (8, 8))
        self.velocidade = 5
        self.opacidade = 255
        self.timer = 0  #Timer para controlar a transparança e a sua destruição
        self.tela = tela

        #determina a direção da frente da nave
        self.direcaoX = direcaoX
        self.direcaoY = direcaoY

    def desenha(self):
        #move o projetil para a direção oposta da frente da nave
        self.x += self.direcaoX * -self.velocidade
        self.y += self.direcaoY * -self.velocidade
        #incrementa o timer
        self.timer += 1

        #reduz a opacidade gradualmente
        if self.timer % 4 == 0:  # Ajuste o valor conforme necessário para controlar a velocidade de desaparecimento
            self.opacidade -= 30
            if self.opacidade < 0:
                self.opacity = 0

        #desenha
        imagem = self.imagem.copy()
        imagem.set_alpha(self.opacidade)
        self.tela.blit(imagem, (self.x, self.y))

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
        #mascara da nave
        self.mask = pygame.mask.from_surface(self.copia)

        """#ESCUDO

        self.escudo = pygame.image.load("imagens/escudo.png")
        self.escudo = pygame.transform.scale(self.escudo, (15 * 8, 15 * 8))
        self.escudo_rect = self.escudo.get_rect(center=(x, y))
        self.escudo_mask = pygame.mask.from_surface(self.escudo)"""

        #angulo
        self.angulo = 0

        #necessário para desenhar na tela
        self.tela = tela

        #lista para armazenar os rastros
        self.rastros = []
        self.timer_rastro = 0  #Timer para determinar o intervalo de tempo entre a criação dos rastros

        """#lista para armazenar os projéteis
        self.vetor_projeteis = []"""

        #MOVIMENTAÇÃO DA CAMERA:
        self.offset = pygame.math.Vector2()

    def desenha(self):
        #atualiza o offset
        self.offset.x = self.copia_rect.centerx - self.tela.get_size()[0] // 2
        self.offset.y = self.copia_rect.centery - self.tela.get_size()[1] // 2

        #cria a posição da nave com o offset
        self.imagem_rect.topleft -= self.offset
        #desenha a nave
        self.tela.blit(self.copia, self.imagem_rect.topleft)

        #desenha os rastros
        for rastro in self.rastros:
            rastro.desenha()

        """#desenha o escudo
        self.tela.blit(self.escudo, self.escudo_rect)"""

        """#determina a frente da nave
        frente_x = self.copia_rect.centerx + (self.largura / 2) * math.cos(math.radians(-self.angulo))
        frente_y = self.copia_rect.centery + (self.largura / 2) * math.sin(math.radians(-self.angulo))

        # Desenha um quadrado vermelho na frente da nave
                                                    #- 4 para que fique centralizado
        pygame.draw.rect(self.tela, (255, 0, 0), (frente_x - 4, frente_y - 4, 10, 10))

        # Atualiza a posição dos projéteis
        for projetil in self.vetor_projeteis:
            projetil.atualizar()

            # Desenha os projéteis
            projetil.desenhar(self.tela)"""

    def rotaciona(self, incremento):
        #adiciona incremento ao angulo
        self.angulo += incremento

        #rotaciona a imagem
        self.copia = pygame.transform.rotate(self.imagem, self.angulo)
        self.copia_rect = self.copia.get_rect(center = self.imagem_rect.center)

    """def atirar(self):
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
        self.vetor_projeteis.append(projetil)"""

    def andar(self, velocidade):
        LARGURA, ALTURA = 1280, 720
        #gera a direção do movimento da nave (para a sua frente)
                #aponta inicialmente para direita           x pega o [0] do vetor, y o [1]
        direcao_x = pygame.math.Vector2(1, 0).rotate(-self.angulo)[0]
        direcao_y = pygame.math.Vector2(1, 0).rotate(-self.angulo)[1]

        #ATUALIZA AS POSIÇÕES

        #confere se a nave não saiu do quadrado pela:
        #esquerda
        if self.imagem_rect.x < 0:
            if direcao_x > 0:
                self.imagem_rect.x += velocidade * direcao_x
        #direita                          - largura do sprite
        elif self.imagem_rect.x > LARGURA - self.largura:
                if direcao_x < 0:
                    self.imagem_rect.x += velocidade * direcao_x
        else:
             self.imagem_rect.x += velocidade * direcao_x

        #baixo                         - altura do sprite
        if self.imagem_rect.y > ALTURA - self.altura:
            if direcao_y < 0:
                self.imagem_rect.y += velocidade * direcao_y
        #cima
        elif self.imagem_rect.y < 0:
            if direcao_y > 0:
                self.imagem_rect.y += velocidade * direcao_y
        else:
            self.imagem_rect.y += velocidade * direcao_y


        #impede ultrapassar a tela


        #RASTROS
        #cria um novo rastro num intervalo fixo de tempo
        if self.timer_rastro >= 3:
            #calcula a parte de tras da nave
            tras_x = self.copia_rect.centerx - (self.largura / 2) * math.cos(math.radians(-self.angulo) + random.choice([-1, 0, 1]) / 4)
                                                                                                          #muda levemente a posição
            tras_y = self.copia_rect.centery - (self.largura / 2) * math.sin(math.radians(-self.angulo) + random.choice([-1, 0, 1]) / 4)

            novo_rastro = Rastro(tras_x, tras_y - 4, self.tela, direcao_x, direcao_y)
            self.rastros.append(novo_rastro)
            self.timer_rastro = 0  # Reinicia o contador de tempo

        # Remove os rastros mais antigos quando excederem o limite
        while len(self.rastros) > 10:
            del self.rastros[0]  # Remove o rastro mais antigo da lista

        # Incrementa o contador de tempo
        self.timer_rastro += 1

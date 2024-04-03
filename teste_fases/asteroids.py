import random

import pygame
from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
from nave import Nave
from asteroid import Asteroid


class Asteroids:
    def __init__(self, janela, gerenciador, mouse):
        #necessário pra desenhar
        self.janela = janela
        #necessario para a troca de fases
        self.gerenciador = gerenciador
        #necessário para açôes com o mouse
        self.mouse = mouse

        self.proximaFase = None

        self.nave = Nave(1280 / 2, 720 / 2, 7 * 8, 5 * 8, "imagens/nave.png", self.janela, None)

        #determina a velocidade da rotação da nave
        self.vel_rotacao = 4
        #determina a velocidade da nave
        self.vel_movimentacao = 5
        #guarda se a tecla espaço foi apertada
        self.pressionada = False

        #usada para determinar a criação de uma nova sujeira
        self.timer = 0

        self.tamanho_vetor = 12
        self.vetor_sujeiras = self.cria_sujeiras()


    def cria_sujeiras(self):
        vetor_sujeiras = [Asteroid(None, None) for _ in range(self.tamanho_vetor)]
        return vetor_sujeiras

    def run(self):

        #recebe todas a teclas pressionadas
        teclas = pygame.key.get_pressed()

        #preenche o fundo da tela de preto
        self.janela.fill((0, 0, 0))

        self.nave.desenha()

        #rotação da nave
        if teclas[pygame.K_RIGHT]:
            self.nave.rotaciona(-self.vel_rotacao)
        elif teclas[pygame.K_LEFT]:
            self.nave.rotaciona(self.vel_rotacao)
        else:
            self.nave.rotaciona(0)

        #movimentação para frente
        if teclas[pygame.K_UP] or teclas[pygame.K_SPACE]:
            self.nave.andar(self.vel_movimentacao)

        self.desenha_sujeiras()
        self.confere_colisao()

        #incrementa o timer
        self.timer += 1

        if self.timer > 500 and len(self.vetor_sujeiras) != 0:
            self.cria_sujeira()
            self.timer = 0

    def cria_sujeira(self):
        #confere se o numero de sujeiras na tela é inferior ao limite
        if len(self.vetor_sujeiras) < self.tamanho_vetor:
            #cria uma nova sujeira a partir de uma existente
            self.vetor_sujeiras.append(Asteroid(self.vetor_sujeiras[random.randint(0, len(self.vetor_sujeiras) - 1)].x, self.vetor_sujeiras[random.randint(0, len(self.vetor_sujeiras) - 1)].y))



    def desenha_sujeiras(self):

        #serve para contar quantas sujeiras restam
        num_sujeiras = 0

        for sujeira in self.vetor_sujeiras:
            #desenha as sujeiras
            sujeira.desenha(self.janela, self.nave.offset)
            sujeira.update()
            #incrementa i para cada sujeira
            num_sujeiras += 1

        #desenha texto
        #defina a cor do texto (em RGB)
        cor_texto = (255, 255, 255)

        #defina a fonte e o tamanho do texto
        fonte = pygame.font.Font(None, 36)

        #Renderize o texto
        texto_renderizado = fonte.render("Sujeiras restantes: " + str(num_sujeiras), True, cor_texto)

        #Obtém o retângulo do texto renderizado
        texto_rect = texto_renderizado.get_rect()

        #Determina a posição do texto
        texto_rect.topleft = (0, 0)

        #desenha o texto
        self.janela.blit(texto_renderizado, texto_rect)

    def confere_colisao(self):

        for sujeira in self.vetor_sujeiras:
            if self.nave.mask.overlap(sujeira.mask, [sujeira.x - self.nave.imagem_rect.x, sujeira.y - self.nave.imagem_rect.y]):
                self.vetor_sujeiras.remove(sujeira)
                #reseta o timer
                #self.timer = 0


        """ #percorre os 2 vetores
        for projetil in self.nave.vetor_projeteis:
            for sujeira in self.vetor_sujeiras:
                #confere a colisao
                if projetil.x + projetil.largura >= sujeira.x and projetil.x <= sujeira.x + sujeira.largura:
                    if projetil.y + projetil.altura>= sujeira.y and projetil.y <= sujeira.y + sujeira.altura:
                        #destroi ambos
                        self.nave.vetor_projeteis.remove(projetil)
                        self.vetor_sujeiras.remove(sujeira)
                        break"""



"""a = Asteroids
LARGURA, ALTURA = 1280, 720
self.janela = pygame.display.set_mode((LARGURA, ALTURA))"""

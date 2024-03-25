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
        #guarda se a tecla espaço foi apertada
        self.pressionada = False

        sujeira1 = Asteroid()
        sujeira2 = Asteroid()
        sujeira3 = Asteroid()
        sujeira4 = Asteroid()
        sujeira5 = Asteroid()
        sujeira6 = Asteroid()
        sujeira7 = Asteroid()
        sujeira8 = Asteroid()
        sujeira9 = Asteroid()
        sujeira10 = Asteroid()



        self.vetor_sujeiras = [sujeira1, sujeira2, sujeira3, sujeira4, sujeira5, sujeira6, sujeira7, sujeira8, sujeira9, sujeira10]




    def run(self):

        #recebe todas a teclas pressionadas
        teclas = pygame.key.get_pressed()

        #preenche o fundo da tela de preto
        self.janela.fill((0, 0, 0))

        self.nave.desenha()

        if teclas[pygame.K_RIGHT]:
            self.nave.rotaciona(-self.vel_rotacao)
        elif teclas[pygame.K_LEFT]:
            self.nave.rotaciona(self.vel_rotacao)
        else:
            self.nave.rotaciona(0)

        if teclas[pygame.K_SPACE] and not self.pressionada:
            self.pressionada = True
            self.nave.atirar()
        elif not teclas[pygame.K_SPACE]:
            self.pressionada = False

        self.desenha_sujeiras()
        self.confere_colisao()


    def desenha_sujeiras(self):
        for sujeira in self.vetor_sujeiras:
            sujeira.desenha(self.janela)
            sujeira.update(self.nave.escudo_mask, self.nave.escudo_rect.x, self.nave.escudo_rect.y)

    def confere_colisao(self):

        #percorre os 2 vetores
        for projetil in self.nave.vetor_projeteis:
            for sujeira in self.vetor_sujeiras:
                #confere a colisao
                if projetil.x + projetil.largura >= sujeira.x and projetil.x <= sujeira.x + sujeira.largura:
                    if projetil.y + projetil.altura>= sujeira.y and projetil.y <= sujeira.y + sujeira.altura:
                        #destroi ambos
                        self.nave.vetor_projeteis.remove(projetil)
                        self.vetor_sujeiras.remove(sujeira)
                        break



"""a = Asteroids
LARGURA, ALTURA = 1280, 720
self.janela = pygame.display.set_mode((LARGURA, ALTURA))"""

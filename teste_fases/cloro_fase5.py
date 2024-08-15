import random
import pygame
from botao import Botao
from SpriteSheet import SpriteSheet
from nave import Nave
from sujeira_fase5 import Sujeira
from asteroid import Particula


class Cloro:
    def __init__(self, janela, gerenciador, mouse, mixer):
        #necessário pra desenhar
        self.janela = janela
        #necessario para a troca de fases
        self.gerenciador = gerenciador
        #necessário para açôes com o mouse
        self.mouse = mouse
        #necessário para tocar sons
        self.mixer = mixer

        self.proximaFase = None

        self.nave = Nave(1280 / 2, 720 / 2, 7 * 8, 5 * 8, "imagens/nave.png", self.janela, None)

        #determina a velocidade da rotação da nave
        self.vel_rotacao = 4
        #determina a velocidade da nave
        self.vel_movimentacao = 10
        #guarda se a tecla espaço foi apertada
        self.pressionada = False

        #usada para determinar a criação de uma nova sujeira
        self.timer = 0

        self.tamanho_vetor = 20
        self.vetor_sujeiras = self.cria_sujeiras()
        self.vetor_particulas = self.cria_particulas()

        #timer usado para o bom funcionamento da comunicação entre as sujeiras
        self.tSujeiras = 0.1

        #zoom
        self.largura, self.altura = 1280, 720
        self.multiplicador = 0.01
        self.inicio_da_fase = True
        self.fim_da_fase = False

    def comunica_sujeiras(self):

        for sujeira in self.vetor_sujeiras:
            for sujeira2 in self.vetor_sujeiras:
                if sujeira.sensor(sujeira2.rect) and sujeira != sujeira2:

                    """pygame.draw.circle(self.janela, (0,128,0), (sujeira.x + sujeira.raio / 2, sujeira.y + sujeira.raio / 2), sujeira.raio, 4)
                    pygame.draw.circle(self.janela, (0, 128, 0), (sujeira.x + sujeira.raio / 2, sujeira.y + sujeira.raio / 2), sujeira.raio, 4)"""
                    #pygame.draw.circle(self.janela, (0, 128, 0), (sujeira.x + sujeira.raio / 2, sujeira.y + sujeira.raio / 2), sujeira.raio, 4)


                    #confere qual sujeira viu a nave mais recentemetnte
                    if sujeira.ultimo_encontro > sujeira2.ultimo_encontro and not sujeira.sensor(self.nave.copia_rect):

                        if sujeira.maior_valor >= sujeira2.maior_valor:
                            sujeira2.maior_valor = sujeira.maior_valor

                            #a sujeira que viu a nave mais recentemente compartilha a sua posição com a outra sujeira
                            sujeira2.navex = sujeira.navex
                            sujeira2.navey = sujeira.navey

                            #incrementa aos poucos o valor do ultimo encontro para a movimentação ocorrer
                            sujeira2.ultimo_encontro = sujeira.ultimo_encontro

                            #executa a alteração no movimento
                            #sujeira2.movimento_propagacao()



                    if sujeira2.ultimo_encontro > sujeira.ultimo_encontro and not sujeira.sensor(self.nave.copia_rect) and sujeira.maior_valor == sujeira2.maior_valor:

                        if sujeira2.maior_valor >= sujeira.maior_valor:

                            sujeira.maior_valor = sujeira2.maior_valor

                            pygame.draw.circle(self.janela, (0,128,0), (sujeira.x + sujeira.raio / 2, sujeira.y + sujeira.raio / 2), sujeira.raio, 4)

                            sujeira.navex = sujeira2.navex
                            sujeira.navey = sujeira2.navey

                            sujeira.ultimo_encontro += sujeira2.ultimo_encontro
                            #sujeira.movimento_propagacao()

    def cria_sujeiras(self):
        vetor_sujeiras = [Sujeira(None, None) for _ in range(self.tamanho_vetor)]
        return vetor_sujeiras

    def carrega_audios(self):
        morte = pygame.mixer.Sound('sons/morte_aguda.wav')
        return (morte)

    def run(self):

        #(morte) = self.carrega_audios()

        self.janela.fill((67, 147, 183))

        if self.multiplicador < 1 and self.inicio_da_fase:
            #diminui a dimensão da nave (7 * 8, 5 * 8)
            largura_alternativa_nave = (7 * 8 * self.multiplicador)
            altura_alternativa_nave = (5 * 8 * self.multiplicador)
            self.nave.copia = pygame.transform.scale(self.nave.imagem, (largura_alternativa_nave, altura_alternativa_nave))

            #ajusta as posições e a dimensão das particulas (1 * 8, 1 * 8)
            for particula in self.vetor_particulas:
                largura_alternativa_part = (8 * self.multiplicador)
                altura_alternativa_part = (8 * self.multiplicador)
                particula.copia = pygame.transform.scale(particula.imagem, (largura_alternativa_part, altura_alternativa_part))

            """largura_alternativa = (self.largura * self.multiplicador)
            altura_alternativa = (self.altura * self.multiplicador)
            self.janela = pygame.transform.scale(self.janela, (largura_alternativa, altura_alternativa))"""

            self.multiplicador += 0.01

            self.nave.desenha()
            self.desenha_particulas()
            for sujeira in self.vetor_sujeiras:
                sujeira.desenha(self.janela, self.nave.offset, self.nave.copia_rect)

        elif not self.fim_da_fase:
            self.inicio_da_fase = False
            #apaga as copias das imagens das particulas para que seja desenhada a imagem original
            if self.vetor_particulas[0].copia:
                for particula in self.vetor_particulas:
                    particula.copia = None

            #recebe todas a teclas pressionadas
            teclas = pygame.key.get_pressed()

            self.nave.desenha()

            #rotação da nave
            if teclas[pygame.K_RIGHT]:
                self.nave.rotaciona(-self.vel_rotacao)
            elif teclas[pygame.K_LEFT]:
                self.nave.rotaciona(self.vel_rotacao)
            else:
                self.nave.rotaciona(0)

            #movimentação para frente
            #if teclas[pygame.K_UP] or teclas[pygame.K_SPACE]:
            self.nave.andar(self.vel_movimentacao)

            self.desenha_particulas()
            sujeiras = self.desenha_sujeiras()
            self.confere_colisao()
            self.comunica_sujeiras()

            #incrementa os timers
            self.timer += 1
            self.tSujeiras += 1

            if self.timer > 1500 and len(self.vetor_sujeiras) != 0:
                self.cria_sujeira()
                self.timer = 0

            if sujeiras == 0:
                self.fim_da_fase = True
            else:
                return True
        else:
            if self.multiplicador > 0.01:
                #diminui a dimensão da nave (7 * 8, 5 * 8)
                largura_alternativa_nave = (7 * 8 * self.multiplicador)
                altura_alternativa_nave = (5 * 8 * self.multiplicador)
                self.nave.copia = pygame.transform.scale(self.nave.imagem, (largura_alternativa_nave, altura_alternativa_nave))

                #ajusta as posições e a dimensão das particulas (1 * 8, 1 * 8)
                for particula in self.vetor_particulas:
                    largura_alternativa_part = (8 * self.multiplicador)
                    altura_alternativa_part = (8 * self.multiplicador)
                    particula.copia = pygame.transform.scale(particula.imagem, (largura_alternativa_part, altura_alternativa_part))

                """largura_alternativa = (self.largura * self.multiplicador)
                altura_alternativa = (self.altura * self.multiplicador)
                self.janela = pygame.transform.scale(self.janela, (largura_alternativa, altura_alternativa))"""

                self.multiplicador -= 0.01

                self.nave.desenha()
                self.desenha_particulas()
                for sujeira in self.vetor_sujeiras:
                    sujeira.desenha(self.janela, self.nave.offset, self.nave.copia_rect)
            else:
                return False

    def cria_sujeira(self):
        #confere se o numero de sujeiras na tela é inferior ao limite
        if len(self.vetor_sujeiras) < self.tamanho_vetor:
            #cria uma nova sujeira a partir de uma existente
            self.vetor_sujeiras.append(Sujeira(self.vetor_sujeiras[0].x, self.vetor_sujeiras[0].y))

    def desenha_sujeiras(self):

        #serve para contar quantas sujeiras restam
        num_sujeiras = 0

        for sujeira in self.vetor_sujeiras:
            #desenha as sujeiras
            sujeira.desenha(self.janela, self.nave.offset, self.nave.copia_rect)
            sujeira.update(self.nave.copia_rect, self.tSujeiras, self.mixer)
            #incrementa i para cada sujeira
            num_sujeiras += 1

        #desenha texto
        #define a cor do texto (em RGB)
        cor_texto = (255, 255, 255)

        #define a fonte e o tamanho do texto
        fonte = pygame.font.Font(None, 36)

        #Renderiza o texto
        texto_renderizado = fonte.render("Sujeiras restantes: " + str(num_sujeiras), True, cor_texto)

        #pega o rect do texto renderizado
        texto_rect = texto_renderizado.get_rect()

        #determine a posição do texto
        texto_rect.topleft = (0, 0)

        #desenha o texto
        self.janela.blit(texto_renderizado, texto_rect)

        return num_sujeiras

    def confere_colisao(self):

        for sujeira in self.vetor_sujeiras:
            if self.nave.mask.overlap(sujeira.mask, [sujeira.x - self.nave.imagem_rect.x, sujeira.y - self.nave.imagem_rect.y]):
                self.vetor_sujeiras.remove(sujeira)
                self.mixer.toca_som('morte_aguda')
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

    def cria_particulas(self):
        vetor_particulas = [Particula() for _ in range(8)]
        return vetor_particulas

    def desenha_particulas(self):
        for particula in self.vetor_particulas:
            particula.desenha(self.janela, self.nave.offset)



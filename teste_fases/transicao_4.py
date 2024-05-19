import pygame
from botao import Botao
import fase_5

class Transicao_4:
    def __init__(self, janela, gerenciador, mouse):
        self.janela = janela
        self.gerenciador = gerenciador
        self.mouse = mouse

        self.proximaFase = fase_5.Fase5(self.janela, self.gerenciador, self.mouse)

        self.imagem = Botao(0, 0, 160 * 8, 90 * 8, "imagens/background_4-5.png", self.janela, None)

        self.imagem_completo = Botao(0, 0, 319 * 8, 90 * 8, "imagens/background_4-5_completo.png", self.janela, None)

        dimensao_opcoes = 30 * 8
        altura = 54 * 8
        dimensao_canos = 32 * 8

        #posição destino do cano (eixo y)
        self.pos = 14 * 8
        self.pos_inicial = -34 * 8

        #canos
        self.cano_esq_cima = Botao(82 * 8, self.pos_inicial, dimensao_canos, dimensao_canos, "imagens/cano2_esq-cima.png", self.janela, None)
        self.cano_cima_dir = Botao(82 * 8, self.pos_inicial, dimensao_canos, dimensao_canos, "imagens/cano2_cima-dir.png", self.janela, None)
        self.cano_baixo_dir = Botao(82 * 8, self.pos_inicial, dimensao_canos, dimensao_canos, "imagens/cano5.png", self.janela, None)

        #opções de cano
        self.opc_cano_esq_cima = Botao(32 * 8, altura, dimensao_opcoes, dimensao_opcoes, "imagens/cano2_esq-cima.png", self.janela, None)
        self.opc_cano_cima_dir = Botao(68.5 * 8, altura + 6 * 8, dimensao_opcoes, dimensao_opcoes, "imagens/cano2_cima-dir.png", self.janela, None)
        self.opc_cano_baixo_dir = Botao(105 * 8, altura, dimensao_opcoes, dimensao_opcoes, "imagens/cano5.png", self.janela, None)

        #borda dos canos
        self.borda1 = Botao(32 * 8, altura, dimensao_opcoes, dimensao_opcoes, "imagens/borda_canos.png", self.janela, None)
        self.borda2 = Botao(68.5 * 8, altura, dimensao_opcoes, dimensao_opcoes, "imagens/borda_canos.png", self.janela, None)
        self.borda3 = Botao(105 * 8, altura, dimensao_opcoes, dimensao_opcoes, "imagens/borda_canos.png", self.janela, None)

        #borda do cano selecionado
        self.vetor_posicoes = [32 * 8, 68.5 * 8, 105 * 8]   #usado para posicionar corretamente o simbolo de selecionado
        self.posicao = 0
        self.selecionado = Botao(self.vetor_posicoes[self.posicao], altura, dimensao_opcoes, dimensao_opcoes, "imagens/cano_selecionado.png", self.janela, None)

        #para o bom funcionamento da selecao
        self.pressionado = False
        self.permite_animacao = False
        self.indo = True
        self.completo = False


    def run(self):

        #recebe todas a teclas pressionadas
        teclas = pygame.key.get_pressed()

        if not self.completo:

            #desenha
            self.imagem.desenha()
            #self.inventario.desenha()
            self.borda1.desenha()
            self.borda2.desenha()
            self.borda3.desenha()

            self.opc_cano_esq_cima.desenha()
            self.opc_cano_cima_dir.desenha()
            self.opc_cano_baixo_dir.desenha()

            self.selecionado.desenha()

            if teclas[pygame.K_RIGHT] and self.pressionado == False and not self.permite_animacao:
                if self.posicao < 2:
                    self.posicao += 1
                    self.selecionado.setX(self.vetor_posicoes[self.posicao])
                    self.pressionado = True
            elif teclas[pygame.K_LEFT] and self.pressionado == False and not self.permite_animacao:
                if self.posicao > 0:
                    self.posicao -= 1
                    self.selecionado.setX(self.vetor_posicoes[self.posicao])
                    self.pressionado = True
            elif not teclas[pygame.K_RIGHT] and not teclas[pygame.K_LEFT]:
                self.pressionado = False

            if teclas[pygame.K_SPACE] and not self.permite_animacao:
                self.permite_animacao = True


            #gera a animação da tentativa do cano adicionado
            if self.permite_animacao:

                if self.posicao == 0:
                    self.cano_esq_cima.desenha()

                    if self.indo:
                        self.testa_cano(self.cano_esq_cima)

                    if self.cano_esq_cima.getY() == self.pos or self.indo == False:
                        self.volta_cano(self.cano_esq_cima)
                        self.indo = False

                    if self.cano_esq_cima.getY() == self.pos_inicial:
                        self.permite_animacao = False
                        self.indo = True

                if self.posicao == 1:
                    self.cano_cima_dir.desenha()

                    if self.indo:
                        self.testa_cano(self.cano_cima_dir)

                    if self.cano_cima_dir.getY() == self.pos or self.indo == False:
                        self.volta_cano(self.cano_cima_dir)
                        self.indo = False

                    if self.cano_cima_dir.getY() == self.pos_inicial:
                        self.permite_animacao = False
                        self.indo = True

                if self.posicao == 2:
                    self.cano_baixo_dir.desenha()
                    self.testa_cano(self.cano_baixo_dir)

                    if self.cano_baixo_dir.getY() == self.pos:
                        self.completo = True

        else:
            self.imagem_completo.desenha()

            velocidade = 3

            if teclas[pygame.K_RIGHT]:
                self.imagem_completo.setX(self.imagem_completo.getX() - velocidade)

            if self.imagem_completo.getX() == -159 * 8:
                self.gerenciador.set_fase(self.proximaFase)







    def testa_cano(self, cano):
        velocidade = 3
        if cano.getY() < self.pos:
            cano.setY(cano.getY() + velocidade)
        else:
            cano.setY(self.pos)


    def volta_cano(self, cano):
        velocidade = 3
        if cano.getY() > self.pos_inicial:
            cano.setY(cano.getY() - velocidade)
        else:
            cano.setY(self.pos_inicial)



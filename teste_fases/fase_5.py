import pygame

from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
import asteroids
from sujeira import Sujeira
from cloro import Cloro
from rede_neural import RedeNeural
import transicao_2

class Fase5:
    def __init__(self, janela, gerenciador, mouse):
        #necessário pra desenhar
        self.janela = janela
        #necessario para a troca de fases
        self.gerenciador = gerenciador
        #necessário para açôes com o mouse
        self.mouse = mouse

        self.proximaFase = None

        #OBJETOS DA FASE:

        # backgound (botão, mas não clicavel)
        self.background = Botao(0, 0, 160 * 8, 90 * 8, "imagens/tijolo_background5.png", self.janela, None)

        #tanque
        self.tanque = Botao(0, 0, 160 * 8, 90 * 8, "imagens/tanque_fase5.png", self.janela, None)
        #indicador do medidor de ph
        #self.medidor = Botao(32 * 8, 42 * 8, 2 * 8, 1 * 8, "imagens/medidor_ph.png", self.janela, None)

        #animação do cal sendo despejado
        cal_sheet_img = pygame.image.load("imagens/animacao_cal.png")
        self.cal_sheet = SpriteSheet(cal_sheet_img, 20)
        self.animacao_cal = ObjAnimado(self.janela, self.cal_sheet, 8, 8, 8, (243, 97, 255), 0)
        self.animacao_cal.anima(47 * 8, 6 * 8)
        self.animacao_cal.setRepetir()
        #self.indo = True    #determina a direção do obj animado

        """#animação da conclusão do uso do cal
        brilho_sheet_img = pygame.image.load("imagens/brilho_cal-sheet.png")
        self.brilho_sheet = SpriteSheet(brilho_sheet_img, 140)
        self.brilho = ObjAnimado(self.janela, self.brilho_sheet, 96 * 8, 44 * 8, 8, (243, 97, 255), 0)
        self.brilho.anima(37 * 8, 18 * 8)"""

        #canos
        self.canos = Botao(0, 0, 160 * 8, 90 * 8, "imagens/canos_fase5.png", self.janela, None)

        #agua
        self.agua = Botao(0, 0, 160 * 8, 90 * 8, "imagens/agua_fase2.png", self.janela, None)
        #sujeira da agua
        self.sujeira = Botao(0, 0, 160 * 8, 90 * 8, "imagens/sujeira_fase2.png", self.janela, None)
        self.opacidade = 50    #255 totalmente opaco - 0 transparente"""

        #borda dos itens selecionados
        self.borda_cal = Botao(39 * 8, 74 * 8, 18 * 8, 17 * 8, "imagens/cal_selecionado.png", self.janela, None)
        self.borda_cloro = Botao(105 * 8, 74 * 8, 18 * 8, 17 * 8, "imagens/cloro_selecionado.png", self.janela, None)
        #indicador de que o item ja foi usado
        self.concluido_cal = Botao(39 * 8, 74 * 8, 18 * 8, 17 * 8, "imagens/concluido.png", self.janela, None)
        self.concluido_cloro = Botao(105 * 8, 74 * 8, 18 * 8, 17 * 8, "imagens/concluido.png", self.janela, None)

        #inventario (obs: não é um inventario da classe inventario)
        self.inventario = Botao(10 * 8, 71 * 8, 140 * 8, 20 * 8, "imagens/inventario.png", self.janela, None)

        #itens (obs: não são itens da classe item)
        self.cal = Botao(40 * 8, 74 * 8, 16 * 8, 16 * 8, "imagens/cal.png", self.janela, None)
        self.cloro = Botao(106 * 8, 74 * 8, 16 * 8, 16 * 8, "imagens/cloro.png", self.janela, None)

        #determina se os itens foram utilizados
        self.cloro_usado = False
        self.cal_usado = False

        self.usando_cal = False     #serve para que o jogador tenha que apertar somente uma vez para a animação ocorrer

        #seletor (determina o item selecionado)
        self.selecionado = self.borda_cal

        #transição entre essa fase e a proxima
        self.permitir_transicao = False
        self.transicao = Botao(0, 0, 480*8, 90*8, "imagens/transicao_2-3.png", self.janela, (243, 97, 255))

        #CLORO
        self.funcionamento_cloro = False    #determina se os cloros estão funcionando ainda na agua
        self.fase_cloro = asteroids.Asteroids(self.janela, self.gerenciador, self.mouse)

        #funcionamento zoom
        self.multiplicador = 1      #variavel que determina o aumento do tanque

    def run(self):

        if self.funcionamento_cloro == False:
            #recebe todas a teclas pressionadas
            teclas = pygame.key.get_pressed()

            #aplica a opacidade a sujeira
            self.sujeira.setAlpha(self.opacidade)

            if not self.cloro_usado or not self.cal_usado:

                #desenha
                self.background.desenha()
                self.agua.desenha()
                self.sujeira.desenha()
                self.tanque.desenha()
                self.canos.desenha()
                self.inventario.desenha()
                self.cloro.desenha()
                self.cal.desenha()

                self.selecionado.desenha()
                if self.cal_usado:
                    self.concluido_cal.desenha()
                if self.cloro_usado:
                    self.concluido_cloro.desenha()


                if self.selecionado == self.borda_cal and not self.funcionamento_cloro:

                    self.animacao_cal.setVelocidade(0.5)

                    if (teclas[pygame.K_SPACE] or self.usando_cal) and not self.cal_usado:
                        if self.opacidade > 25:
                            self.usando_cal = True
                            self.animacao_cal.update()
                            if self.animacao_cal.getFrame() > 13:
                                print("sabado")
                                self.animacao_cal.setFrame(8)
                            self.opacidade = self.opacidade - 0.8
                        else:
                            print("facada")
                            self.usando_cal = False
                            self.cal_usado = True
                    else:
                        if self.opacidade <= 25:
                            self.animacao_cal.setRepetir()
                            self.animacao_cal.update()
                            self.opacidade = 20
                        if teclas[pygame.K_RIGHT]:
                            self.selecionado = self.borda_cloro
                else:

                    if teclas[pygame.K_SPACE]:
                        if not self.cloro_usado and self.cal_usado:
                            self.funcionamento_cloro = True
                        else:
                            print("use o cal primeiro")


                    if teclas[pygame.K_LEFT] and not self.funcionamento_cloro:
                        self.selecionado = self.borda_cal


            #transição
            else:
                if self.multiplicador > 1:
                    #desenha os outros objetos da fase
                    self.background.desenha()
                    self.canos.desenha()
                    self.inventario.desenha()
                    self.cloro.desenha()
                    self.cal.desenha()
                    #desenha os objetos redimencionados
                    self.agua.desenha()
                    self.sujeira.desenha()
                    self.tanque.desenha()
                    #aplica a alteração no tamanho
                    self.tanque.redimencionar(self.multiplicador)
                    self.sujeira.redimencionar(self.multiplicador)
                    self.agua.redimencionar(self.multiplicador)
                    self.multiplicador -= 0.05
                else:
                    self.transicao.desenha()
                    if self.transicao.getX() > (-160 * 8) - 1:

                        #Verifica se a seta para a direita está sendo pressionada
                        if teclas[pygame.K_RIGHT]:
                            self.transicao.setX(self.transicao.getX() - 3)
                    else:
                        self.proximaFase = transicao_2.Transicao_2(self.janela, self.gerenciador, self.mouse)
                        self.gerenciador.set_fase(self.proximaFase)

        else:
                if self.multiplicador < 2.7:
                    self.agua.desenha()
                    self.sujeira.desenha()
                    self.tanque.desenha()
                    self.tanque.redimencionar(self.multiplicador)
                    self.sujeira.redimencionar(self.multiplicador)
                    self.agua.redimencionar(self.multiplicador)
                    self.multiplicador += 0.05
                else:
                    self.funcionamento_cloro = self.fase_cloro.run()
                    self.cloro_usado = not self.funcionamento_cloro


import pygame

from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
import asteroids
from sujeira import Sujeira
from cloro import Cloro
from rede_neural import RedeNeural
import transicao_2

class Fase2:
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
        self.background = Botao(0, 0, 160 * 8, 90 * 8, "imagens/tijolo_background.png", self.janela, None)

        #tanque
        self.tanque = Botao(0, 0, 160 * 8, 90 * 8, "imagens/tanque_fase2.png", self.janela, None)
        #indicador do medidor de ph
        self.medidor = Botao(32 * 8, 42 * 8, 2 * 8, 1 * 8, "imagens/medidor_ph.png", self.janela, None)
        #animação que evidencia o ph ideal
        ph_ideal_sheet_img = pygame.image.load("imagens/ph_ideal-sheet.png")
        self.ph_ideal_sheet = SpriteSheet(ph_ideal_sheet_img, 5)
        self.ph_ideal = ObjAnimado(self.janela, self.ph_ideal_sheet, 160, 90, 8, (243, 97, 255), 0)
        self.ph_ideal.anima(0, 0)
        self.ph_ideal.setRepetir()  #permite o looping da animação

        #animação do cal sendo despejado
        cal_sheet_img = pygame.image.load("imagens/animacao_cal.png")
        self.cal_sheet = SpriteSheet(cal_sheet_img, 20)
        self.animacao_cal = ObjAnimado(self.janela, self.cal_sheet, 8, 8, 8, (243, 97, 255), 0)
        self.animacao_cal.anima(47 * 8, 6 * 8)
        self.animacao_cal.setRepetir()
        self.indo = True    #determina a direção do obj animado

        """#animação da conclusão do uso do cal
        brilho_sheet_img = pygame.image.load("imagens/brilho_cal-sheet.png")
        self.brilho_sheet = SpriteSheet(brilho_sheet_img, 140)
        self.brilho = ObjAnimado(self.janela, self.brilho_sheet, 96 * 8, 44 * 8, 8, (243, 97, 255), 0)
        self.brilho.anima(37 * 8, 18 * 8)"""

        #canos
        self.canos = Botao(0, 0, 160 * 8, 90 * 8, "imagens/canos_fase2.png", self.janela, None)

        #agua
        self.agua = Botao(0, 0, 160 * 8, 90 * 8, "imagens/agua_fase2.png", self.janela, None)
        #sujeira da agua
        self.sujeira = Botao(0, 0, 160 * 8, 90 * 8, "imagens/sujeira_fase2.png", self.janela, None)
        self.opacidade = 160    #255 totalmente opaco - 0 transparente"""

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

        #para o bom funcionamento dos sons
        self.toca = True

    def carrega_audios(self):
        click = pygame.mixer.Sound('sons/blipSelect.wav')
        cano_errado = pygame.mixer.Sound('sons/cano errado.wav')
        cano_correto = pygame.mixer.Sound('sons/cano_correto.wav')
        erro_cal = pygame.mixer.Sound('sons/use_o_cal_primeiro.mp3')

        return (click, cano_errado, cano_correto, erro_cal)

    def run(self):

        (click, erro, acerto, erro_cal) = self.carrega_audios()

        narracao = pygame.mixer.Channel(0)

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

                self.medidor.desenha()

                if self.selecionado == self.borda_cal and not self.funcionamento_cloro:

                    #permite a animação do indicador do ph ideal
                    self.ph_ideal.setVelocidade(0.5)
                    self.animacao_cal.setVelocidade(0.5)
                    if self.medidor.getY() < 48 * 8:
                        self.ph_ideal.update()
                    else:
                        self.cal_usado = True

                    if teclas[pygame.K_SPACE] or self.usando_cal:

                        if self.medidor.getY() < 48 * 8:

                            if self.toca:
                                acerto.play()
                            self.toca = False

                            self.usando_cal = True
                            self.animacao_cal.update()
                            if self.animacao_cal.getFrame() > 13:
                                self.animacao_cal.setFrame(8)
                            self.animacao_cal.setX(self.animacao_cal.getX() + 6)
                            self.medidor.setY(self.medidor.getY() + 0.5)
                            self.opacidade = self.opacidade - 0.6
                        else:
                            self.usando_cal = False
                    else:
                        self.toca = True
                        if self.medidor.getY() >= 48 * 8:
                            self.animacao_cal.setRepetir()
                            self.animacao_cal.update()
                            self.opacidade = 100
                            """self.brilho.setVelocidade(10)
                            self.brilho.update()"""
                        if teclas[pygame.K_RIGHT]:
                            click.play()
                            self.selecionado = self.borda_cloro
                else:

                    #inibe a animação do indicador do ph ideal
                    self.ph_ideal.setFrame(0)

                    if teclas[pygame.K_SPACE]:
                        if not self.cloro_usado and self.cal_usado:
                            if self.toca:
                                acerto.play()
                            self.toca = False
                            self.funcionamento_cloro = True
                        else:
                            if narracao.get_busy() == False:
                                narracao.play(erro_cal)
                                erro.play()
                            #print("use o cal primeiro")


                    if teclas[pygame.K_LEFT] and not self.funcionamento_cloro:
                        click.play()
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


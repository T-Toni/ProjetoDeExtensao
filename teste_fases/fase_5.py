import pygame

from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
import cloro_fase5
from sujeira import Sujeira
from cloro import Cloro
from rede_neural import RedeNeural
import menu

class Fase5:
    def __init__(self, janela, gerenciador, mouse, mixer):
        #inicializa o mixer
        self.mixer = mixer


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
        self.inventario = Botao(10 * 8, 70 * 8, 140 * 8, 20 * 8, "imagens/inventario.png", self.janela, None)

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
        self.transicao = Botao(0, 0, 640*8, 90*8, "imagens/transicao_5-fim.png", self.janela, (243, 97, 255))

        #CLORO
        self.funcionamento_cloro = False    #determina se os cloros estão funcionando ainda na agua
        self.fase_cloro = cloro_fase5.Cloro(self.janela, self.gerenciador, self.mouse)

        #funcionamento zoom
        self.multiplicador = 1      #variavel que determina o aumento do tanque

        #animação da agua indo para as casas
        casas_sheet_img = pygame.image.load("imagens/animacao_casas-sheet.png")
        casas_sheet_img = SpriteSheet(casas_sheet_img, 46)
        self.animacao_casas = ObjAnimado(self.janela, casas_sheet_img, 160, 90, 8, (243, 97, 255), 0.3)

        #tela final
        self.tela_final = Botao(0, 0, 160*8, 90*8, "imagens/tela_final.png", self.janela, (243, 97, 255))
        self.botao_menu = Botao(21 * 8, 51 * 8, 49*8, 13*8, "imagens/botao_menu.png", self.janela, (243, 97, 255))

        #para o bom funcionamento dos efeitos sonoros
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


                if self.selecionado == self.borda_cal and not self.funcionamento_cloro:

                    self.animacao_cal.setVelocidade(0.5)

                    if (teclas[pygame.K_SPACE] or self.usando_cal) and not self.cal_usado:

                        if self.toca:
                            acerto.play()
                        self.toca = False

                        if self.opacidade > 25:
                            self.usando_cal = True
                            self.animacao_cal.update()
                            if self.animacao_cal.getFrame() > 13:
                                self.animacao_cal.setFrame(8)
                            self.opacidade = self.opacidade - 0.8
                        else:
                            self.usando_cal = False
                            self.cal_usado = True
                    else:
                        self.toca = True
                        if self.opacidade <= 25:
                            self.animacao_cal.setRepetir()
                            self.animacao_cal.update()
                            self.opacidade = 20
                        if teclas[pygame.K_RIGHT]:
                            click.play()
                            self.selecionado = self.borda_cloro
                else:

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
                            print("use o cal primeiro")


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
                    if self.transicao.getX() > (-480 * 8) - 1:

                        #Verifica se a seta para a direita está sendo pressionada
                        if teclas[pygame.K_RIGHT]:
                            self.transicao.setX(self.transicao.getX() - 3)
                    else:
                        if self.animacao_casas.getFrame() >= 45:
                            self.tela_final.desenha()
                            self.botao_menu.desenha()
                            if teclas[pygame.K_SPACE] or (self.botao_menu.mouse_dentro(self.mouse.getX(), self.mouse.getY()) and self.mouse.getPressionado()):
                                self.proximaFase = menu.Menu(self.janela, self.gerenciador, self.mouse, self.mixer)
                                self.gerenciador.set_fase(self.proximaFase)
                        else:
                            self.animacao_casas.anima(0, 0)
                            self.animacao_casas.update()

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


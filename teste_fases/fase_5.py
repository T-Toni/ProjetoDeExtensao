import pygame

from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
import cloro_fase5
from sujeira import Sujeira
from cloro import Cloro
from rede_neural import RedeNeural
import menu
import texto

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
        self.transicao = Botao(0, 0, 640*8, 90*8, "imagens/transicao_5-fim(2).png", self.janela, (243, 97, 255))

        #CLORO
        self.funcionamento_cloro = False    #determina se os cloros estão funcionando ainda na agua
        self.fase_cloro = cloro_fase5.Cloro(self.janela, self.gerenciador, self.mouse, self.mixer)

        #funcionamento zoom
        self.multiplicador = 1      #variavel que determina o aumento do tanque

        #animação da agua indo para as casas
        casas_sheet_img = pygame.image.load("imagens/final_casa-sheet.png")
        casas_sheet_img = SpriteSheet(casas_sheet_img, 23)
        self.animacao_casas = ObjAnimado(self.janela, casas_sheet_img, 160, 90, 8, (243, 97, 255), 0.2)

        #tela final
        self.tela_final = Botao(0, 0, 160*8, 90*8, "imagens/tela_final.png", self.janela, (243, 97, 255))
        self.botao_menu = Botao(21 * 8, 51 * 8, 49*8, 13*8, "imagens/botao_menu.png", self.janela, (243, 97, 255))

        #para o bom funcionamento dos efeitos sonoros
        self.toca = True

        # INTRODUCAO ( tamanho maximo(para25):
        # ---------'água, desde a represa até água chegar em sua casa!')
        texto1_1 = 'Muito bem, nós chegamos na ultima etapa do'
        texto1_2 = 'tratamento!!'
        texto1_3 = None
        texto1_4 = None

        texto2_1 = 'Nessa etapa, chamada de Pós-cloração e Ajuste final'
        texto2_2 = 'do pH, nós devemos adicionar uma pequena quantidade'
        texto2_3 = 'de cal e cloro na água, para garantir que fique'
        texto2_4 = 'potável.'

        texto3_1 = 'Muito bem, o pH foi regulado com sucesso!'
        texto3_2 = 'Agora adicione o cloro.'
        texto3_3 = None
        texto3_4 = None

        texto4_1 = 'Você deve usar o cal primeiro.'
        texto4_2 = None
        texto4_3 = None
        texto4_4 = None

        # etapa do cloro
        texto5_1 = 'Você controla o cloro como na última fase,'
        texto5_2 = 'mas cuidado, as sujeiras restantes são menores'
        texto5_3 = 'e mais difíceis de serem pegas.'
        texto5_4 = None

        # fim do cloro
        texto6_1 = 'Muito bem!!!!'
        texto6_2 = 'Agora que você eliminou as sujeiras, a água já'
        texto6_3 = 'está limpa. Pressione a seta para a direita'
        texto6_4 = 'para seguir.'

        # resevatorio
        texto7_1 = 'Esse é o reservatório, onde a água limpa fica'
        texto7_2 = 'guardada para ser direcionada às nossas casas.'
        texto7_3 = None
        texto7_4 = None

        # fim do jogo
        texto8_1 = 'E por fim, a água é enviada por meio de canos'
        texto8_2 = 'para as casas!'
        texto8_3 = None
        texto8_4 = None

        self.intro1 = texto.Texto(texto1_1, texto1_2, texto1_3, texto1_4, 2, self.janela, 1)
        self.intro2 = texto.Texto(texto2_1, texto2_2, texto2_3, texto2_4, 2, self.janela, 2)
        self.pos_cal = texto.Texto(texto3_1, texto3_2, texto3_3, texto3_4, 2, self.janela, 1)
        self.intro_cloro = texto.Texto(texto5_1, texto5_2, texto5_3, texto5_4, 2, self.janela, 3)
        self.fim = texto.Texto(texto6_1, texto6_2, texto6_3, texto6_4, 2, self.janela, 1)
        self.erro = texto.Texto(texto4_1, texto4_2, texto4_3, texto4_4, 2, self.janela, 2)
        self.reservatorio = texto.Texto(texto7_1, texto7_2, texto7_3, texto7_4, 0, self.janela, 2)
        self.conclusao = texto.Texto(texto8_1, texto8_2, texto8_3, texto8_4, 2, self.janela, 1)

        #booleanos para controlar as falas
        self.concluiu_intro1 = False
        self.concluiu_intro2 = False
        self.concluiu_cal = False
        self.concluiu_intro_cloro = False
        self.concluiu_fim = False
        self.concluiu_reservatorio = False
        self.concluiu_conclusao = False

    def run(self):

        # recebe todas a teclas pressionadas
        teclas = pygame.key.get_pressed()

        # função para pular falas
        self.mixer.update(teclas)

        # aplica a opacidade a sujeira
        self.sujeira.setAlpha(self.opacidade)

        if not self.concluiu_intro1:
            self.mixer.toca_fala('introducao5.1')
            self.concluiu_intro1 = True
        elif not self.concluiu_intro2 and not self.mixer.tocando_falas():
            self.mixer.toca_fala('introducao5.2')
            self.concluiu_intro2 = True

        if self.funcionamento_cloro == False and not self.mixer.get_audio_atual(0) == 'introducao5.2' and self.concluiu_intro2:

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
                    if not self.concluiu_cal:
                        self.mixer.toca_fala('pos_cal_fase2')
                        self.concluiu_cal = True
                    self.concluido_cal.desenha()
                if self.cloro_usado:
                    self.concluido_cloro.desenha()


                if self.selecionado == self.borda_cal and not self.funcionamento_cloro:

                    self.animacao_cal.setVelocidade(0.5)

                    if (teclas[pygame.K_SPACE] or self.usando_cal) and not self.cal_usado:

                        if self.toca:
                            self.mixer.toca_som('acerto')
                            #acerto.play()
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
                            self.mixer.toca_som('click')
                            #click.play()
                            self.selecionado = self.borda_cloro
                else:

                    if teclas[pygame.K_SPACE]:
                        if not self.cloro_usado and self.cal_usado:
                            if self.toca:
                                self.mixer.toca_som('acerto')
                                #acerto.play()
                            self.toca = False
                            self.funcionamento_cloro = True
                        else:
                            if self.mixer.tocando_falas() == False:
                                self.mixer.toca_fala('use_o_cal_primeiro')
                                #narracao.play(erro_cal)
                                self.mixer.toca_som('erro')
                                #erro.play()


                    if teclas[pygame.K_LEFT] and not self.funcionamento_cloro:
                        self.mixer.toca_som('click')
                        #click.play()
                        self.selecionado = self.borda_cal


            #transição
            else:
                self.mixer.acao = False #troca a trilha

                if not self.concluiu_fim:
                    self.mixer.toca_fala('fim_fase5')
                    self.concluiu_fim = True

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

                    if self.transicao.getX() < (-140 * 8) - 1 and not self.concluiu_reservatorio:
                        self.mixer.toca_fala('reservatorio')
                        self.concluiu_reservatorio = True


                    if self.transicao.getX() < (-440 * 8) - 1 and not self.concluiu_conclusao and not self.mixer.tocando_falas():
                        self.mixer.toca_fala('conclusao')
                        self.concluiu_conclusao = True


                    if self.transicao.getX() > (-480 * 8) - 1:

                        #Verifica se a seta para a direita está sendo pressionada
                        if teclas[pygame.K_RIGHT]:
                            self.transicao.setX(self.transicao.getX() - 3)
                    else:
                        if self.animacao_casas.getFrame() >= 22 and not self.mixer.tocando_falas():
                            self.tela_final.desenha()
                            self.botao_menu.desenha()
                            if teclas[pygame.K_SPACE] or (self.botao_menu.mouse_dentro(self.mouse.getX(), self.mouse.getY()) and self.mouse.getPressionado()):
                                self.proximaFase = menu.Menu(self.janela, self.gerenciador, self.mouse, self.mixer)
                                self.gerenciador.set_fase(self.proximaFase)
                        else:
                            self.animacao_casas.anima(0, 0)
                            self.animacao_casas.update()

        elif not self.mixer.get_audio_atual(0) == 'introducao5.2' and self.concluiu_intro2:
            if self.multiplicador < 2.7:
                self.agua.desenha()
                self.sujeira.desenha()
                self.tanque.desenha()
                self.tanque.redimencionar(self.multiplicador)
                self.sujeira.redimencionar(self.multiplicador)
                self.agua.redimencionar(self.multiplicador)
                self.multiplicador += 0.05
            else:
                if not self.concluiu_intro_cloro:
                    self.mixer.toca_fala('intro_cloro_fase5')
                    self.concluiu_intro_cloro = True
                self.mixer.acao = True  #troca a trilha
                self.funcionamento_cloro = self.fase_cloro.run()
                self.cloro_usado = not self.funcionamento_cloro

        #desenha o fundo para a introdução:
        else:
            self.background.desenha()
            self.agua.desenha()
            self.sujeira.desenha()
            self.tanque.desenha()
            self.canos.desenha()
            self.inventario.desenha()
            self.cloro.desenha()
            self.cal.desenha()



        # escreve as falas
        if self.mixer.get_audio_atual(0) == 'introducao5.1':
            self.intro1.escreve()

        if self.mixer.get_audio_atual(0) == 'introducao5.2':
            self.intro2.escreve()

        if self.mixer.get_audio_atual(0) == 'pos_cal_fase2':
            self.pos_cal.escreve()

        if self.mixer.get_audio_atual(0) == 'intro_cloro_fase5':
            self.intro_cloro.escreve()

        if self.mixer.get_audio_atual(0) == 'fim_fase5':
            self.fim.escreve()

        if self.mixer.get_audio_atual(0) == 'use_o_cal_primeiro':
            self.erro.escreve()

        if self.mixer.get_audio_atual(0) == 'reservatorio':
            self.reservatorio.escreve()

        if self.mixer.get_audio_atual(0) == 'conclusao':
            self.conclusao.escreve()

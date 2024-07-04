import pygame

from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
import asteroids
from sujeira import Sujeira
from cloro import Cloro
from rede_neural import RedeNeural
import transicao_2
import texto

class Fase2:
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

        # INTRODUCAO ( tamanho maximo(para25):
        # ---------'água, desde a represa até água chegar em sua casa!')
        texto1_1 = 'Essa é a etapa de Pré-cloração e Ajuste de PH.'
        texto1_2 = 'E nessa etapa nós adicionamos o cal e o cloro'
        texto1_3 = 'na agua suja.'
        texto1_4 = None

        texto2_1 = 'O cal serve para controlar o ph e o cloro serve'
        texto2_2 = 'para eliminar as sujeiras.'
        texto2_3 = 'Adicione primeiro o cal, que é esse pó branco'
        texto2_4 = 'na esquerda.'

        texto3_1 = 'Muito bem, O PH foi regulado com sucesso!'
        texto3_2 = 'Agora adicione o cloro.'
        texto3_3 = None
        texto3_4 = None

        texto4_1 = 'Você deve usar o cal primeiro.'
        texto4_2 = None
        texto4_3 = None
        texto4_4 = None

        #etapa do cloro
        texto5_1 = 'Agora voce controla o Cloro, use as setas da'
        texto5_2 = 'esquerda e direita para controlar a nave,'
        texto5_3 = 'e se aproxime das sujeiras para eliminá-las.'
        texto5_4 = None

        #fim do cloro
        texto6_1 = 'Muito bem! Agora que voce eliminou as'
        texto6_2 = 'sujeiras a água já está mais limpa.'
        texto6_3 = 'Pressione a [SETA->] para a direita'
        texto6_4 = 'para seguir com o tratamento.'

        self.intro1 = texto.Texto(texto1_1, texto1_2, texto1_3, texto1_4, 2, self.janela)
        self.intro2 = texto.Texto(texto2_1, texto2_2, texto2_3, texto2_4, 2, self.janela)
        self.pos_cal = texto.Texto(texto3_1, texto3_2, texto3_3, texto3_4, 2, self.janela)
        self.intro_cloro = texto.Texto(texto5_1, texto5_2, texto5_3, texto5_4, 2, self.janela)
        self.fim = texto.Texto(texto6_1, texto6_2, texto6_3, texto6_4, 2, self.janela)
        self.erro = texto.Texto(texto4_1, texto4_2, texto4_3, texto4_4, 2, self.janela)

        #variaveis para o bom funcionamento da narração
        self.concluiu_intro1 = False
        self.concluiu_intro2 = False
        self.concluiu_cal = False
        self.concluiu_intro_cloro = False
        self.concluiu_fim = False



    def run(self):

        #recebe todas a teclas pressionadas
        teclas = pygame.key.get_pressed()

        # aplica a opacidade a sujeira
        self.sujeira.setAlpha(self.opacidade)

        # função para pular falas
        self.mixer.update(teclas)

        if not self.concluiu_intro1:
            self.mixer.toca_fala('introducao2.1')
            self.concluiu_intro1 = True
        elif not self.concluiu_intro2 and not self.mixer.tocando_falas():
            self.mixer.toca_fala('introducao2.2')
            self.concluiu_intro2 = True


        if self.funcionamento_cloro == False and not self.mixer.get_audio_atual(0) == 'introducao2.2' and self.concluiu_intro2:

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
                                self.mixer.toca_som('cano_errado')
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
                            self.mixer.toca_som('click')
                            self.selecionado = self.borda_cloro
                else:

                    #inibe a animação do indicador do ph ideal
                    self.ph_ideal.setFrame(0)

                    if teclas[pygame.K_SPACE]:
                        if not self.cloro_usado and self.cal_usado:
                            if self.toca:
                                self.mixer.toca_som('cano_correto')
                            self.toca = False
                            self.funcionamento_cloro = True
                        else:
                            if not self.mixer.tocando_falas():
                                self.mixer.toca_fala('use_o_cal_primeiro')
                                self.mixer.toca_som('cano_errado')
                            #print("use o cal primeiro")


                    if teclas[pygame.K_LEFT] and not self.funcionamento_cloro:
                        self.mixer.toca_som('click')
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

                    if not self.concluiu_fim:
                        self.mixer.toca_fala('fim_fase2')
                        self.concluiu_fim = True

                    if self.transicao.getX() > (-160 * 8) - 1 and self.concluiu_fim:

                        #Verifica se a seta para a direita está sendo pressionada
                        if teclas[pygame.K_RIGHT]:
                            self.transicao.setX(self.transicao.getX() - 3)
                    elif not self.mixer.tocando_falas():
                        self.proximaFase = transicao_2.Transicao_2(self.janela, self.gerenciador, self.mouse, self.mixer)
                        self.gerenciador.set_fase(self.proximaFase)

        elif not self.mixer.get_audio_atual(0) == 'introducao2.2' and self.concluiu_intro2:
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
                    self.mixer.toca_fala('intro_cloro_fase2')
                    self.concluiu_intro_cloro = True
                self.funcionamento_cloro = self.fase_cloro.run()
                self.cloro_usado = not self.funcionamento_cloro

        else:
            # desenha
            self.background.desenha()
            self.agua.desenha()
            self.sujeira.desenha()
            self.tanque.desenha()
            self.canos.desenha()
            self.inventario.desenha()
            self.cloro.desenha()
            self.cal.desenha()
            self.selecionado.desenha()
            self.medidor.desenha()


        # escreve as falas
        if self.mixer.get_audio_atual(0) == 'introducao2.1':
            self.intro1.escreve()

        if self.mixer.get_audio_atual(0) == 'introducao2.2':
            self.intro2.escreve()

        if self.mixer.get_audio_atual(0) == 'pos_cal_fase2':
            self.pos_cal.escreve()

        if self.mixer.get_audio_atual(0) == 'intro_cloro_fase2':
            self.intro_cloro.escreve()

        if self.mixer.get_audio_atual(0) == 'fim_fase2':
            self.fim.escreve()

        if self.mixer.get_audio_atual(0) == 'use_o_cal_primeiro':
            self.erro.escreve()


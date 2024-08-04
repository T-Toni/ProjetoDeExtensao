import pygame


import fase_1
import fase_2
import fase_3
import fase_4
import fase_5
import asteroids
import cloro_fase5
from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
import math



class Menu:
    def __init__(self, janela, gerenciador, mouse, mixer):
        #inicializa o mixer
        self.mixer = mixer

        # necessário para desenhar
        self.janela = janela

        # necessário para mudar de fases
        self.gerenciador = gerenciador

        # necessário para tudo que envolve o mouse
        self.mouse = mouse

        #backgound (tambem é um botão, mas não clicavel)
        self.background = Botao(0, 0, 1280, 1440, "imagens/tijolo_background_longo.png", self.janela, None)
        #detalhes estéticos e titulo
        self.canos = Botao(0, 0, 1280, 1440, "imagens/canos_menu+fases.png", self.janela, None)

        #botões                                                             OBS: cada pixel da pixel-art vale 8
        #                        X       Y     Largura  Altura              por isso a multiplicação na declaração
        self.botao_fases = Botao(8 * 13, 8 * 36, 8 * 54, 8 * 13, "imagens/botao_fases.png", self.janela, None)
        self.botao_opcoes = Botao(8 * 13, 8 * 51, 8 * 54, 8 * 13, "imagens/botao_opcoes.png", self.janela, None)
        self.botao_sair = Botao(8 * 13, 8 * 67, 8 * 54, 8 * 13, "imagens/botao_sair.png", self.janela, None)
        self.botao_jogar = Botao(8 * 92, 8 * 48, 8 * 63, 8 * 36, "imagens/botao_jogar.png", self.janela, None)

        # ANIMAÇÕES!!!!
        # JOGAR
        # atribui a imagem do spritesheet a variavel
        jogar_sheet_img = pygame.image.load("imagens/botao_jogar-sheet.png")
        # cria um objeto "SpriteSheet" (spritesheet, numero total de frames)
        jogar_sheet_obj = SpriteSheet(jogar_sheet_img, 16)
        # cria um objeto "ObjAnimado" que é capaz de rodar a animação                            #codigo do rosa usado para transparencia
        self.obj_jogar = ObjAnimado(self.janela, jogar_sheet_obj, 63, 36, 8, (243, 97, 255), 0.3)

        # OPÇÕES
        opcoes_sheet_img = pygame.image.load("imagens/botao_opcoes-sheet.png")
        opcoes_sheet_obj = SpriteSheet(opcoes_sheet_img, 16)
        self.obj_opcoes = ObjAnimado(self.janela, opcoes_sheet_obj, 54, 13, 8, (243, 97, 255), 0.3)

        # FASES
        fases_sheet_img = pygame.image.load("imagens/botao_fases-sheet.png")
        fases_sheet_obj = SpriteSheet(fases_sheet_img, 16)
        self.obj_fases = ObjAnimado(self.janela, fases_sheet_obj, 54, 13, 8, (243, 97, 255), 0.3)

        self.descendo = False       # caso fases seja clicado inicia a decida para o menu de fases
        self.subindo = False
        self.deslocamento = 0       # conta quantos pixels a tela desceu para poder determinar a parada

        # SAIR
        sair_sheet_img = pygame.image.load("imagens/botao_sair-sheet.png")
        sair_sheet_obj = SpriteSheet(sair_sheet_img, 16)
        self.obj_sair = ObjAnimado(self.janela, sair_sheet_obj, 54, 13, 8, (243, 97, 255), 0.3)

        # TELA DAS FASES!!
        self.vel_botoes = 0.2   #determina a velocidade da animação dos botões

        #botões
        self.botao_fase1 = Botao(13 * 8, 97 * 8, 8 * 46, 8 * 13, "imagens/botao_fase1.png", self.janela, None)
        fase1_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase1_sheet_obj = SpriteSheet(fase1_sheet_img, 20)
        self.obj_fase1 = ObjAnimado(self.janela, fase1_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase1.anima(self.botao_fase1.getX(), self.botao_fase1.getY())      #inicia a animação
        self.obj_fase1.proximo = None

        self.botao_fase2 = Botao(13 * 8, 113 * 8, 8 * 46, 8 * 13, "imagens/botao_fase2.png", self.janela, None)
        fase2_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase2_sheet_obj = SpriteSheet(fase2_sheet_img, 20)
        self.obj_fase2 = ObjAnimado(self.janela, fase2_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase2.anima(self.botao_fase2.getX(), self.botao_fase2.getY())
        self.obj_fase2.proximo = self.obj_fase1

        self.botao_fase3 = Botao(13 * 8, 129 * 8, 8 * 46, 8 * 13, "imagens/botao_fase3.png", self.janela, None)
        fase3_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase3_sheet_obj = SpriteSheet(fase3_sheet_img, 20)
        self.obj_fase3 = ObjAnimado(self.janela, fase3_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase3.anima(self.botao_fase3.getX(), self.botao_fase3.getY())
        self.obj_fase3.proximo = self.obj_fase2

        self.botao_fase4 = Botao(13 * 8, 144 * 8, 8 * 46, 8 * 13, "imagens/botao_fase4.png", self.janela, None)
        fase4_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase4_sheet_obj = SpriteSheet(fase4_sheet_img, 20)
        self.obj_fase4 = ObjAnimado(self.janela, fase4_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase4.anima(self.botao_fase4.getX(), self.botao_fase4.getY())
        self.obj_fase4.proximo = self.obj_fase3

        self.botao_fase5 = Botao(13 * 8, 159 * 8, 8 * 46, 8 * 13, "imagens/botao_fase5.png", self.janela, None)
        fase5_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase5_sheet_obj = SpriteSheet(fase5_sheet_img, 20)
        self.obj_fase5 = ObjAnimado(self.janela, fase5_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase5.anima(self.botao_fase5.getX(), self.botao_fase5.getY())
        self.obj_fase5.proximo = self.obj_fase4

        """self.botao_central = Botao(75 * 8, 110 * 8, 8 * 10, 8 * 46, "imagens/botao_central.png", self.janela, None)
        fase5_sheet_img = pygame.image.load("imagens/botao_central-sheet.png")
        fase5_sheet_obj = SpriteSheet(fase5_sheet_img, 49)
        self.obj_central = ObjAnimado(self.janela, fase5_sheet_obj, 10, 46, 8, (243, 97, 255), 0)
        self.obj_central.anima(self.botao_central.getX(), self.botao_central.getY())
        self.obj_central.proximo = self.obj_fase5

        self.botao_fase6 = Botao(101 * 8, 97 * 8, 8 * 46, 8 * 13, "imagens/botao_fase6.png", self.janela, None)
        fase1_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase1_sheet_obj = SpriteSheet(fase1_sheet_img, 20)
        self.obj_fase6 = ObjAnimado(self.janela, fase1_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase6.anima(self.botao_fase6.getX(), self.botao_fase6.getY())  # inicia a animação
        self.obj_fase6.proximo = self.obj_central

        self.botao_fase7 = Botao(101 * 8, 113 * 8, 8 * 46, 8 * 13, "imagens/botao_fase7.png", self.janela, None)
        fase2_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase2_sheet_obj = SpriteSheet(fase2_sheet_img, 20)
        self.obj_fase7 = ObjAnimado(self.janela, fase2_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase7.anima(self.botao_fase7.getX(), self.botao_fase7.getY())
        self.obj_fase7.proximo = self.obj_fase6

        self.botao_fase8 = Botao(101 * 8, 129 * 8, 8 * 46, 8 * 13, "imagens/botao_fase8.png", self.janela, None)
        fase3_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase3_sheet_obj = SpriteSheet(fase3_sheet_img, 20)
        self.obj_fase8 = ObjAnimado(self.janela, fase3_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase8.anima(self.botao_fase8.getX(), self.botao_fase8.getY())
        self.obj_fase8.proximo = self.obj_fase7

        self.botao_fase9 = Botao(101 * 8, 144 * 8, 8 * 46, 8 * 13, "imagens/botao_fase9.png", self.janela, None)
        fase4_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase4_sheet_obj = SpriteSheet(fase4_sheet_img, 20)
        self.obj_fase9 = ObjAnimado(self.janela, fase4_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase9.anima(self.botao_fase9.getX(), self.botao_fase9.getY())
        self.obj_fase9.proximo = self.obj_fase8

        self.botao_fase10 = Botao(101 * 8, 159 * 8, 8 * 46, 8 * 13, "imagens/botao_fase10.png", self.janela, None)
        fase5_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase5_sheet_obj = SpriteSheet(fase5_sheet_img, 20)
        self.obj_fase10 = ObjAnimado(self.janela, fase5_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase10.anima(self.botao_fase10.getX(), self.botao_fase10.getY())
        self.obj_fase10.proximo = self.obj_fase9"""

        self.botao_cloro1 = Botao(100 * 8, 110 * 8, 8 * 10, 8 * 46, "imagens/botao_cloro1.png", self.janela, None)
        cloro1_sheet_img = pygame.image.load("imagens/botao_central-sheet.png")
        cloro1_sheet_obj = SpriteSheet(cloro1_sheet_img, 49)
        self.obj_cloro1 = ObjAnimado(self.janela, cloro1_sheet_obj, 10, 46, 8, (243, 97, 255), 0)
        self.obj_cloro1.anima(self.botao_cloro1.getX(), self.botao_cloro1.getY())
        self.obj_cloro1.proximo = self.obj_fase5

        self.botao_cloro2 = Botao(132 * 8, 110 * 8, 8 * 10, 8 * 46, "imagens/botao_cloro2.png", self.janela, None)
        cloro2_sheet_img = pygame.image.load("imagens/botao_central-sheet.png")
        cloro2_sheet_obj = SpriteSheet(cloro2_sheet_img, 49)
        self.obj_cloro2 = ObjAnimado(self.janela, cloro2_sheet_obj, 10, 46, 8, (243, 97, 255), 0)
        self.obj_cloro2.anima(self.botao_cloro2.getX(), self.botao_cloro2.getY())
        self.obj_cloro2.proximo = self.obj_cloro1

        self.botao_voltar = Botao(1 * 8, 90 * 8, 8 * 9, 8 * 10, "imagens/botao_voltar.png", self.janela, None)
        fase5_sheet_img = pygame.image.load("imagens/botao_voltar-sheet.png")
        fase5_sheet_obj = SpriteSheet(fase5_sheet_img, 12)
        self.obj_botao_voltar = ObjAnimado(self.janela, fase5_sheet_obj, 9, 10, 8, (243, 97, 255), 0)
        self.obj_botao_voltar.anima(self.botao_voltar.getX(), self.botao_voltar.getY())


        #para a lógica da tela de opções
        self.opcoes = False
        self.tela_opcoes = Botao(0, 0, 8 * 160, 8 * 90, "imagens/tela_opcoes.png", self.janela, None)

        #logica para as fases dos cloros
        self.cloro1 = False
        self.funcionamento_cloro1 = False
        self.cloro2 = False
        self.funcionamento_cloro2 = False

        self.fase_cloro1 = None
        self.fase_cloro2 = None

        self.jogando = False

    """def carrega_audios(self):
        click = pygame.mixer.Sound('sons/blipSelect.wav')
        loop_agua = pygame.mixer.Sound('sons/loop_agua1.ogg')
        bolhas = pygame.mixer.Sound('sons/loop_bolhas.ogg')

        agua = pygame.mixer.Channel(0)

        return (click, loop_agua, bolhas, agua)"""

    #função que percorre todos os objetos animados da tela de fases para conferir que nenhum está sendo animado
    def podeDescer(self):
        i = self.obj_cloro2

        while i != None:

            if i.getFrame() != 0:
                return False

            i = i.proximo

        return True


    def run(self):

        if not self.cloro1 and not self.cloro2:

            if not self.opcoes:

                """if not self.audios_carregados:
                    (click, loop_agua, bolha, agua) = self.carrega_audios()"""

                # desenha todos os objetos graficos
                # menu
                if self.deslocamento < 720:     #desenha caso eles estejam visiveis
                    self.background.desenha()
                    self.canos.desenha()
                    self.botao_fases.desenha()
                    self.botao_opcoes.desenha()
                    self.botao_sair.desenha()
                    self.botao_jogar.desenha()

                # menu_fases
                if self.descendo:
                    #metade esquerda
                    self.obj_fase1.update()
                    self.botao_fase1.desenha()
                    self.obj_fase2.update()
                    self.botao_fase2.desenha()
                    self.obj_fase3.update()
                    self.botao_fase3.desenha()
                    self.obj_fase4.update()
                    self.botao_fase4.desenha()
                    self.obj_fase5.update()
                    self.botao_fase5.desenha()

                    """#botão do meio
                    self.obj_central.update()
                    self.botao_central.desenha()
    
                    #metade direita
                    self.obj_fase6.update()
                    self.botao_fase6.desenha()
                    self.obj_fase7.update()
                    self.botao_fase7.desenha()
                    self.obj_fase8.update()
                    self.botao_fase8.desenha()
                    self.obj_fase9.update()
                    self.botao_fase9.desenha()
                    self.obj_fase10.update()
                    self.botao_fase10.desenha()"""

                    self.obj_cloro1.update()
                    self.botao_cloro1.desenha()

                    self.obj_cloro2.update()
                    self.botao_cloro2.desenha()

                    #metade da direita


                    #botão voltar
                    self.botao_voltar.desenha()
                    self.obj_botao_voltar.update()

                # inicia as animações dos botões
                if self.botao_jogar.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                    self.mixer.toca_som('bolhas1')
                    # permite a animação
                    self.obj_jogar.anima(8 * 92, 8 * 48)

                if self.botao_opcoes.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                    self.mixer.toca_som('bolhas1')
                    # permite a animação
                    self.obj_opcoes.anima(8 * 13, 8 * 51)

                if self.botao_fases.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                    self.mixer.toca_som('bolhas1')
                    # permite a animação
                    self.obj_fases.anima(8 * 13, 8 * 36)
                    self.descendo = True
                    self.subindo = False

                if self.botao_sair.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                    self.mixer.toca_som('bolhas1')
                    # permite a animação
                    self.obj_sair.anima(8 * 13, 8 * 67)

                # atualiza os objetos animados
                self.obj_jogar.update()
                self.obj_opcoes.update()
                self.obj_fases.update()
                self.obj_sair.update()

                # continua a funcionalidade dos botões pós animação
                if self.obj_jogar.fim_da_animacao():
                    self.mixer.para_sons()
                    proximaFase = fase_1.Fase1(self.janela, self.gerenciador, self.mouse, self.mixer)
                    self.gerenciador.set_fase(proximaFase)

                if self.obj_opcoes.fim_da_animacao():
                    self.opcoes = True

                if self.obj_sair.fim_da_animacao():
                    # sair do jogo
                    pygame.quit()
                    exit()

                if self.descendo and not self.subindo:
                    # desce tudo para a parte das fases

                    #função para determinar o valor do incremento
                    incremento = math.ceil((720 - self.deslocamento) / 45)

                    self.deslocamento += incremento
                    if self.deslocamento <= 720:
                        #menu
                        self.background.setY(self.background.getY() - incremento)
                        self.canos.setY(self.canos.getY() - incremento)
                        self.botao_fases.setY(self.botao_fases.getY() - incremento)
                        self.obj_fases.setY(self.obj_fases.getY() - incremento)
                        self.botao_opcoes.setY(self.botao_opcoes.getY() - incremento)
                        if self.obj_opcoes.getY():
                            self.obj_opcoes.setY(self.obj_opcoes.getY() - incremento)
                        self.botao_sair.setY(self.botao_sair.getY() - incremento)
                        if self.obj_sair.getY():
                            self.obj_sair.setY(self.obj_sair.getY() - incremento)
                        self.botao_jogar.setY(self.botao_jogar.getY() - incremento)
                        if self.obj_jogar.getY():
                            self.obj_jogar.setY(self.obj_jogar.getY() - incremento)

                        #botões das fases
                        self.botao_fase1.setY(self.botao_fase1.getY() - incremento)
                        self.obj_fase1.setY(self.obj_fase1.getY() - incremento)
                        self.botao_fase2.setY(self.botao_fase2.getY() - incremento)
                        self.obj_fase2.setY(self.obj_fase2.getY() - incremento)
                        self.botao_fase3.setY(self.botao_fase3.getY() - incremento)
                        self.obj_fase3.setY(self.obj_fase3.getY() - incremento)
                        self.botao_fase4.setY(self.botao_fase4.getY() - incremento)
                        self.obj_fase4.setY(self.obj_fase4.getY() - incremento)
                        self.botao_fase5.setY(self.botao_fase5.getY() - incremento)
                        self.obj_fase5.setY(self.obj_fase5.getY() - incremento)

                        """self.botao_central.setY(self.botao_central.getY() - incremento)
                        self.obj_central.setY(self.obj_central.getY() - incremento)
    
                        self.botao_fase6.setY(self.botao_fase6.getY() - incremento)
                        self.obj_fase6.setY(self.obj_fase6.getY() - incremento)
                        self.botao_fase7.setY(self.botao_fase7.getY() - incremento)
                        self.obj_fase7.setY(self.obj_fase7.getY() - incremento)
                        self.botao_fase8.setY(self.botao_fase8.getY() - incremento)
                        self.obj_fase8.setY(self.obj_fase8.getY() - incremento)
                        self.botao_fase9.setY(self.botao_fase9.getY() - incremento)
                        self.obj_fase9.setY(self.obj_fase9.getY() - incremento)
                        self.botao_fase10.setY(self.botao_fase10.getY() - incremento)
                        self.obj_fase10.setY(self.obj_fase10.getY() - incremento)"""

                        self.botao_cloro1.setY(self.botao_cloro1.getY() - incremento)
                        self.obj_cloro1.setY(self.obj_cloro1.getY() - incremento)
                        self.botao_cloro2.setY(self.botao_cloro2.getY() - incremento)
                        self.obj_cloro2.setY(self.obj_cloro2.getY() - incremento)

                        self.botao_voltar.setY(self.botao_voltar.getY() - incremento)
                        self.obj_botao_voltar.setY(self.obj_botao_voltar.getY() - incremento)

                        #pressionamento dos botões
                        if self.deslocamento == 720:
                            if self.botao_fase1.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                                self.obj_fase1.anima(self.obj_fase1.getX(), self.obj_fase1.getY())
                                self.obj_fase1.setVelocidade(self.vel_botoes)
                                self.mixer.toca_som('bolhas1')

                            if self.botao_fase2.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                                self.obj_fase2.letAnima()
                                self.obj_fase2.setVelocidade(self.vel_botoes)
                                self.mixer.toca_som('bolhas1')

                            if self.botao_fase3.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                                self.obj_fase3.letAnima()
                                self.obj_fase3.setVelocidade(self.vel_botoes)
                                self.mixer.toca_som('bolhas1')

                            if self.botao_fase4.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                                self.obj_fase4.letAnima()
                                self.obj_fase4.setVelocidade(self.vel_botoes)
                                self.mixer.toca_som('bolhas1')

                            if self.botao_fase5.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                                self.obj_fase5.letAnima()
                                self.obj_fase5.setVelocidade(self.vel_botoes)
                                self.mixer.toca_som('bolhas1')

                            """if self.botao_central.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                                self.obj_central.letAnima()
                                self.obj_central.setVelocidade(self.vel_botoes)
    
                            if self.botao_fase6.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                                self.obj_fase6.letAnima()
                                self.obj_fase6.setVelocidade(self.vel_botoes)
    
                            if self.botao_fase7.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                                self.obj_fase7.letAnima()
                                self.obj_fase7.setVelocidade(self.vel_botoes)
    
                            if self.botao_fase8.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                                self.obj_fase8.letAnima()
                                self.obj_fase8.setVelocidade(self.vel_botoes)
    
                            if self.botao_fase9.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                                self.obj_fase9.letAnima()
                                self.obj_fase9.setVelocidade(self.vel_botoes)
    
                            if self.botao_fase10.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                                self.obj_fase10.letAnima()
                                self.obj_fase10.setVelocidade(self.vel_botoes)"""

                            if self.botao_cloro1.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                                self.obj_cloro1.letAnima()
                                self.obj_cloro1.setVelocidade(self.vel_botoes)
                                self.mixer.toca_som('bolhas1')

                            if self.botao_cloro2.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                                self.obj_cloro2.letAnima()
                                self.obj_cloro2.setVelocidade(self.vel_botoes)
                                self.mixer.toca_som('bolhas1')

                            if self.botao_voltar.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                                if self.podeDescer():
                                    self.obj_botao_voltar.letAnima()
                                    self.obj_botao_voltar.setVelocidade(self.vel_botoes)
                                    self.subindo = True
                                    self.mixer.toca_som('bolhas1')

                    if self.obj_fase1.fim_da_animacao():
                        proximaFase = fase_1.Fase1(self.janela, self.gerenciador, self.mouse, self.mixer)
                        self.gerenciador.set_fase(proximaFase)

                    if self.obj_fase2.fim_da_animacao():
                        proximaFase = fase_2.Fase2(self.janela, self.gerenciador, self.mouse, self.mixer)
                        self.gerenciador.set_fase(proximaFase)

                    if self.obj_fase3.fim_da_animacao():
                        proximaFase = fase_3.Fase3(self.janela, self.gerenciador, self.mouse, self.mixer)
                        self.gerenciador.set_fase(proximaFase)

                    if self.obj_fase4.fim_da_animacao():
                        proximaFase = fase_4.Fase4(self.janela, self.gerenciador, self.mouse, self.mixer)
                        self.gerenciador.set_fase(proximaFase)

                    if self.obj_fase5.fim_da_animacao():
                        proximaFase = fase_5.Fase5(self.janela, self.gerenciador, self.mouse, self.mixer)
                        self.gerenciador.set_fase(proximaFase)

                    if self.obj_cloro1.fim_da_animacao_2():
                        self.cloro1 = True
                        print("fnaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf")

                    if self.obj_cloro2.fim_da_animacao_2():
                        self.cloro2 = True
                        print("fnaf2222222222222222222222222222222222222222")

                        '''else:
                            self.obj_fase1.setVelocidade(0)
                            self.obj_fase2.setVelocidade(0)
                            self.obj_fase3.setVelocidade(0)
                            self.obj_fase4.setVelocidade(0)
                            self.obj_fase5.setVelocidade(0)
                            self.obj_central.setVelocidade(0)
                            self.obj_fase6.setVelocidade(0)
                            self.obj_fase7.setVelocidade(0)
                            self.obj_fase8.setVelocidade(0)
                            self.obj_fase9.setVelocidade(0)
                            self.obj_fase10.setVelocidade(0)'''

                if self.subindo:
                    # desce tudo para a parte das fases

                    #função para determinar o valor do incremento
                    incremento = math.ceil((self.deslocamento) / 45) * -1

                    self.deslocamento += incremento
                    if self.deslocamento > 0:
                        #menu
                        self.background.setY(self.background.getY() - incremento)
                        self.canos.setY(self.canos.getY() - incremento)
                        self.botao_fases.setY(self.botao_fases.getY() - incremento)
                        self.obj_fases.setY(self.obj_fases.getY() - incremento)
                        self.botao_opcoes.setY(self.botao_opcoes.getY() - incremento)
                        if self.obj_opcoes.getY():
                            self.obj_opcoes.setY(self.obj_opcoes.getY() - incremento)
                        self.botao_sair.setY(self.botao_sair.getY() - incremento)
                        if self.obj_sair.getY():
                            self.obj_sair.setY(self.obj_sair.getY() - incremento)
                        self.botao_jogar.setY(self.botao_jogar.getY() - incremento)
                        if self.obj_jogar.getY():
                            self.obj_jogar.setY(self.obj_jogar.getY() - incremento)

                        #botões das fases
                        self.botao_fase1.setY(self.botao_fase1.getY() - incremento)
                        self.obj_fase1.setY(self.obj_fase1.getY() - incremento)
                        self.botao_fase2.setY(self.botao_fase2.getY() - incremento)
                        self.obj_fase2.setY(self.obj_fase2.getY() - incremento)
                        self.botao_fase3.setY(self.botao_fase3.getY() - incremento)
                        self.obj_fase3.setY(self.obj_fase3.getY() - incremento)
                        self.botao_fase4.setY(self.botao_fase4.getY() - incremento)
                        self.obj_fase4.setY(self.obj_fase4.getY() - incremento)
                        self.botao_fase5.setY(self.botao_fase5.getY() - incremento)
                        self.obj_fase5.setY(self.obj_fase5.getY() - incremento)

                        """self.botao_central.setY(self.botao_central.getY() - incremento)
                        self.obj_central.setY(self.obj_central.getY() - incremento)
    
                        self.botao_fase6.setY(self.botao_fase6.getY() - incremento)
                        self.obj_fase6.setY(self.obj_fase6.getY() - incremento)
                        self.botao_fase7.setY(self.botao_fase7.getY() - incremento)
                        self.obj_fase7.setY(self.obj_fase7.getY() - incremento)
                        self.botao_fase8.setY(self.botao_fase8.getY() - incremento)
                        self.obj_fase8.setY(self.obj_fase8.getY() - incremento)
                        self.botao_fase9.setY(self.botao_fase9.getY() - incremento)
                        self.obj_fase9.setY(self.obj_fase9.getY() - incremento)
                        self.botao_fase10.setY(self.botao_fase10.getY() - incremento)
                        self.obj_fase10.setY(self.obj_fase10.getY() - incremento)"""

                        self.botao_cloro1.setY(self.botao_cloro1.getY() - incremento)
                        self.obj_cloro1.setY(self.obj_cloro1.getY() - incremento)
                        self.botao_cloro2.setY(self.botao_cloro2.getY() - incremento)
                        self.obj_cloro2.setY(self.obj_cloro2.getY() - incremento)

                        self.botao_voltar.setY(self.botao_voltar.getY() - incremento)
                        self.obj_botao_voltar.setY(self.obj_botao_voltar.getY() - incremento)

                        if self.deslocamento <= 0:
                            self.descendo = False
                            self.deslocamento = 0

            else:
                self.tela_opcoes.desenha()

                #inicializa a fonte
                fonte = pygame.font.Font('fontes/Commodore Pixeled.ttf', 25)

                #cores
                branco = (255, 255, 255)
                preto = (0, 0, 0)

                #botões
                botao_voltar = Botao(43 * 8, 19 * 8, 8 * 23, 8 * 9, None, self.janela, None)

                x = 98 * 8
                y = 41 * 8
                incrementox = 15 * 8
                incrementoy = 14 * 8

                au_sons = Botao(x, y, 8 * 3, 8 * 6, "imagens/botao_fases.png", self.janela, None)
                ab_sons = Botao(x + incrementox, y, 8 * 3, 8 * 6, "imagens/botao_fases.png", self.janela, None)

                au_musica = Botao(x, y + incrementoy, 8 * 3, 8 * 6, "imagens/botao_fases.png", self.janela, None)
                ab_musica = Botao(x + incrementox, y + incrementoy, 8 * 3, 8 * 6, "imagens/botao_fases.png", self.janela, None)

                au_falas = Botao(x, y + incrementoy * 2, 8 * 3, 8 * 6, "imagens/botao_fases.png", self.janela, None)
                ab_falas = Botao(x + incrementox, y + incrementoy * 2, 8 * 3, 8 * 6, "imagens/botao_fases.png", self.janela, None)

                #renderiza os textos
                voltar = fonte.render("VOLTAR", 1, preto)

                vol_sons = fonte.render("VOLUME DOS EFEITOS:", 1, preto)
                vol_musica = fonte.render("VOLUME DA MUSICA:", 1, preto)
                vol_narracao = fonte.render("VOLUME DA NARRAÇÃO:", 1, preto)

                val_sons = fonte.render(str(self.mixer.get_volume_sons()), 1, preto)
                val_musica = fonte.render(str(self.mixer.get_volume_musica()), 1, preto)
                val_narracao = fonte.render(str(self.mixer.get_volume_falas()), 1, preto)


                #escreve os textos
                self.janela.blit(voltar, (54 * 8, 22 * 8))

                x = 45 * 8
                y = 43 * 8
                incremento = 14 * 8


                self.janela.blit(vol_sons, (x, y))
                self.janela.blit(vol_musica, (x, y + incremento))
                self.janela.blit(vol_narracao, (x, y + incremento * 2))

                x = 103 * 8

                self.janela.blit(val_sons, (x, y - 1*8))
                self.janela.blit(val_musica, (x, y + incremento - 1*8))
                self.janela.blit(val_narracao, (x, y - 1*8 + incremento * 2))

                #funcionnalidade dos botões

                if botao_voltar.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                        self.opcoes = False


                if au_sons.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                    if self.mixer.get_volume_sons() > 0:
                        self.mixer.set_volume_sons(self.mixer.get_volume_sons() - 0.1)
                        self.mixer.toca_som('click')
                    else:
                        self.mixer.toca_som('cano_errado')


                if ab_sons.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                    if self.mixer.get_volume_sons() < 1:
                        self.mixer.set_volume_sons(self.mixer.get_volume_sons() + 0.1)
                        self.mixer.toca_som('click')
                    """else:
                        self.mixer.toca_som('cano_errado')"""

                if au_musica.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                    if self.mixer.get_volume_musica() > 0:
                        self.mixer.set_volume_musica(self.mixer.get_volume_musica() - 0.1)
                        self.mixer.toca_som('click')
                    else:
                        self.mixer.toca_som('cano_errado')

                if ab_musica.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                    if self.mixer.get_volume_musica() < 1:
                        self.mixer.set_volume_musica(self.mixer.get_volume_musica() + 0.1)
                        self.mixer.toca_som('click')
                    else:
                        self.mixer.toca_som('cano_errado')

                if au_falas.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                    if self.mixer.get_volume_falas() > 0:
                        self.mixer.set_volume_falas(self.mixer.get_volume_falas() - 0.1)
                        self.mixer.toca_som('click')
                    else:
                        self.mixer.toca_som('cano_errado')

                if ab_falas.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                    if self.mixer.get_volume_falas() < 1:
                        self.mixer.set_volume_falas(self.mixer.get_volume_falas() + 0.1)
                        self.mixer.toca_som('click')
                    else:
                        self.mixer.toca_som('cano_errado')

        if self.cloro1:

            if self.jogando == False:
                self.fase_cloro1 = asteroids.Asteroids(self.janela, self.gerenciador, self.mouse)
                self.jogando = True


            self.funcionamento_cloro1 = self.fase_cloro1.run()
            if self.funcionamento_cloro1 == None:
                self.cloro1 = True
            else:
                self.cloro1 = self.funcionamento_cloro1


            #para corrigir a parede
            if not self.cloro1:
                self.background.desenha()
                self.canos.desenha()
                self.obj_cloro1.setFrame(0)
                #cancela a animação
                self.obj_cloro1.setVelocidade(0)
                self.obj_cloro1.update()
                self.jogando = False
                self.fase_cloro1 = None


        if self.cloro2:

            if self.jogando == False:
                self.fase_cloro2 = cloro_fase5.Cloro(self.janela, self.gerenciador, self.mouse)
                self.jogando = True

            self.funcionamento_cloro2 = self.fase_cloro2.run()
            if self.funcionamento_cloro2 == None:
                self.cloro2 = True
            else:
                self.cloro2 = self.funcionamento_cloro2


            #para corrigir a parede
            if not self.cloro2:
                self.background.desenha()
                self.canos.desenha()
                self.obj_cloro2.setFrame(0)
                self.obj_cloro2.setVelocidade(0)
                self.obj_cloro2.update()
                self.jogando = False
                self.fase_cloro2 = None



        #debug

        """print("cloro1: ")
        print(self.fase_cloro1.run())
        print("cloro2: ")
        print(self.cloro2)"""







import pygame
from pygame import QUIT

import fase_1
from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
import math



class Menu:
    def __init__(self, janela, gerenciador, mouse):
        # necessário para desenhar
        self.janela = janela

        # necessário para mudar de fases
        self.gerenciador = gerenciador

        # necessário para tudo que envolve o mouse
        self.mouse = mouse

        #backgound (tambem é um botão, mas não clicavel)
        self.background = Botao(0, 0, 1280, 1440, "imagens/tijolo_background_longo.png", self.janela, None)
        #detalhes estéticos e titulo
        self.canos = Botao(0, 0, 1280, 1440, "imagens/detalhes_menu+fases.png", self.janela, None)

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

        self.botao_fase2 = Botao(13 * 8, 113 * 8, 8 * 46, 8 * 13, "imagens/botao_fase2.png", self.janela, None)
        fase2_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase2_sheet_obj = SpriteSheet(fase2_sheet_img, 20)
        self.obj_fase2 = ObjAnimado(self.janela, fase2_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase2.anima(self.botao_fase2.getX(), self.botao_fase2.getY())

        self.botao_fase3 = Botao(13 * 8, 129 * 8, 8 * 46, 8 * 13, "imagens/botao_fase3.png", self.janela, None)
        fase3_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase3_sheet_obj = SpriteSheet(fase3_sheet_img, 20)
        self.obj_fase3 = ObjAnimado(self.janela, fase3_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase3.anima(self.botao_fase3.getX(), self.botao_fase3.getY())

        self.botao_fase4 = Botao(13 * 8, 144 * 8, 8 * 46, 8 * 13, "imagens/botao_fase4.png", self.janela, None)
        fase4_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase4_sheet_obj = SpriteSheet(fase4_sheet_img, 20)
        self.obj_fase4 = ObjAnimado(self.janela, fase4_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase4.anima(self.botao_fase4.getX(), self.botao_fase4.getY())

        self.botao_fase5 = Botao(13 * 8, 159 * 8, 8 * 46, 8 * 13, "imagens/botao_fase5.png", self.janela, None)
        fase5_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase5_sheet_obj = SpriteSheet(fase5_sheet_img, 20)
        self.obj_fase5 = ObjAnimado(self.janela, fase5_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase5.anima(self.botao_fase5.getX(), self.botao_fase5.getY())

        self.botao_central = Botao(75 * 8, 110 * 8, 8 * 10, 8 * 46, "imagens/botao_central.png", self.janela, None)
        fase5_sheet_img = pygame.image.load("imagens/botao_central-sheet.png")
        fase5_sheet_obj = SpriteSheet(fase5_sheet_img, 49)
        self.obj_central = ObjAnimado(self.janela, fase5_sheet_obj, 10, 46, 8, (243, 97, 255), 0)
        self.obj_central.anima(self.botao_central.getX(), self.botao_central.getY())

        self.botao_fase6 = Botao(101 * 8, 97 * 8, 8 * 46, 8 * 13, "imagens/botao_fase6.png", self.janela, None)
        fase1_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase1_sheet_obj = SpriteSheet(fase1_sheet_img, 20)
        self.obj_fase6 = ObjAnimado(self.janela, fase1_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase6.anima(self.botao_fase6.getX(), self.botao_fase6.getY())  # inicia a animação

        self.botao_fase7 = Botao(101 * 8, 113 * 8, 8 * 46, 8 * 13, "imagens/botao_fase7.png", self.janela, None)
        fase2_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase2_sheet_obj = SpriteSheet(fase2_sheet_img, 20)
        self.obj_fase7 = ObjAnimado(self.janela, fase2_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase7.anima(self.botao_fase7.getX(), self.botao_fase7.getY())

        self.botao_fase8 = Botao(101 * 8, 129 * 8, 8 * 46, 8 * 13, "imagens/botao_fase8.png", self.janela, None)
        fase3_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase3_sheet_obj = SpriteSheet(fase3_sheet_img, 20)
        self.obj_fase8 = ObjAnimado(self.janela, fase3_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase8.anima(self.botao_fase8.getX(), self.botao_fase8.getY())

        self.botao_fase9 = Botao(101 * 8, 144 * 8, 8 * 46, 8 * 13, "imagens/botao_fase9.png", self.janela, None)
        fase4_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase4_sheet_obj = SpriteSheet(fase4_sheet_img, 20)
        self.obj_fase9 = ObjAnimado(self.janela, fase4_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase9.anima(self.botao_fase9.getX(), self.botao_fase9.getY())

        self.botao_fase10 = Botao(101 * 8, 159 * 8, 8 * 46, 8 * 13, "imagens/botao_fase10.png", self.janela, None)
        fase5_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase5_sheet_obj = SpriteSheet(fase5_sheet_img, 20)
        self.obj_fase10 = ObjAnimado(self.janela, fase5_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase10.anima(self.botao_fase10.getX(), self.botao_fase10.getY())

        self.botao_voltar = Botao(1 * 8, 90 * 8, 8 * 9, 8 * 10, "imagens/botao_voltar.png", self.janela, None)
        fase5_sheet_img = pygame.image.load("imagens/botao_voltar-sheet.png")
        fase5_sheet_obj = SpriteSheet(fase5_sheet_img, 12)
        self.obj_botao_voltar = ObjAnimado(self.janela, fase5_sheet_obj, 9, 10, 8, (243, 97, 255), 0)
        self.obj_botao_voltar.anima(self.botao_voltar.getX(), self.botao_voltar.getY())



    def run(self):

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

            #botão do meio
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
            self.botao_fase10.desenha()

            #botão voltar
            self.botao_voltar.desenha()
            self.obj_botao_voltar.update()

        # inicia as animações dos botões
        if self.botao_jogar.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
            # permite a animação
            self.obj_jogar.anima(8 * 92, 8 * 48)  # permite o loop de animacao

        if self.botao_opcoes.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
            # permite a animação
            self.obj_opcoes.anima(8 * 13, 8 * 51)

        if self.botao_fases.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
            # permite a animação
            self.obj_fases.anima(8 * 13, 8 * 36)
            self.descendo = True

        if self.botao_sair.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
            # permite a animação
            self.obj_sair.anima(8 * 13, 8 * 67)

        # atualiza os objetos animados
        self.obj_jogar.update()
        self.obj_opcoes.update()
        self.obj_fases.update()
        self.obj_sair.update()

        # continua a funcionalidade dos botões pós animação
        if self.obj_jogar.fim_da_animacao():
            proximaFase = fase_1.Fase1(self.janela, self.gerenciador, self.mouse)
            self.gerenciador.set_fase(proximaFase)

        if self.obj_sair.fim_da_animacao():
            # sair do jogo
            pygame.quit()
            exit()

        if self.descendo:
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

                self.botao_central.setY(self.botao_central.getY() - incremento)
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
                self.obj_fase10.setY(self.obj_fase10.getY() - incremento)

                self.botao_voltar.setY(self.botao_voltar.getY() - incremento)
                self.obj_botao_voltar.setY(self.obj_botao_voltar.getY() - incremento)

                #pressionamento dos botões
                if self.deslocamento == 720:
                    if self.botao_fase1.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                        self.obj_fase1.letAnima()
                        self.obj_fase1.setVelocidade(self.vel_botoes)

                    if self.botao_fase2.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                        self.obj_fase2.letAnima()
                        self.obj_fase2.setVelocidade(self.vel_botoes)

                    if self.botao_fase3.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                        self.obj_fase3.letAnima()
                        self.obj_fase3.setVelocidade(self.vel_botoes)

                    if self.botao_fase4.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                        self.obj_fase4.letAnima()
                        self.obj_fase4.setVelocidade(self.vel_botoes)

                    if self.botao_fase5.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                        self.obj_fase5.letAnima()
                        self.obj_fase5.setVelocidade(self.vel_botoes)

                    if self.botao_central.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
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
                        self.obj_fase10.setVelocidade(self.vel_botoes)

                    if self.botao_voltar.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                        self.obj_botao_voltar.letAnima()
                        self.obj_botao_voltar.setVelocidade(self.vel_botoes)



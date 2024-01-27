import pygame
from pygame import QUIT

import fase_1
from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado



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

        #botões
        self.botao_fase2 = Botao(13 * 8, 113 * 8, 8 * 46, 8 * 13, "imagens/botao_fase2.png", self.janela, None)
        fase2_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase2_sheet_obj = SpriteSheet(fase2_sheet_img, 20)
        self.obj_fase2 = ObjAnimado(self.janela, fase2_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase2.anima(self.botao_fase2.getX(), self.botao_fase2.getY())  # inicia a animação
        #self.botao_fase2.setProximo(self.botao_fase3)

        self.botao_fase1 = Botao(13 * 8, 97 * 8, 8 * 46, 8 * 13, "imagens/botao_fase1.png", self.janela, None)
        fase1_sheet_img = pygame.image.load("imagens/animacao_fases-sheet.png")
        fase1_sheet_obj = SpriteSheet(fase1_sheet_img, 20)
        self.obj_fase1 = ObjAnimado(self.janela, fase1_sheet_obj, 46, 13, 8, (243, 97, 255), 0)
        self.obj_fase1.anima(self.botao_fase1.getX(), self.botao_fase1.getY())      #inicia a animação
        self.botao_fase1.setProximo(self.botao_fase2)




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
            self.obj_fase1.update()
            self.botao_fase1.desenha()
            self.obj_fase2.update()
            self.botao_fase2.desenha()


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
            if self.deslocamento <= 360:
                incremento = 16
            elif self.deslocamento <= 540:
                incremento = 12
            else:
                incremento = 8
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

                #fases
                self.botao_fase1.setY(self.botao_fase1.getY() - incremento)
                self.obj_fase1.setY(self.obj_fase1.getY() - incremento)
                self.botao_fase2.setY(self.botao_fase2.getY() - incremento)
                self.obj_fase2.setY(self.obj_fase2.getY() - incremento)


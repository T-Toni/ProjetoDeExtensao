import pygame
from pygame import QUIT

import fase_1
from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
from inventario import Inventario
from item import Item


class Menu:
    def __init__(self, janela, gerenciador, mouse):
        # necessário para desenhar
        self.janela = janela

        # necessário para mudar de fases
        self.gerenciador = gerenciador

        # necessário para tudo que envolve o mouse
        self.mouse = mouse

        #backgound (tambem é um botão, mas não clicavel)
        self.background = Botao(0, 0, 1280, 720, "imagens/tijolo_background.png", self.janela, None)
        #detalhes estéticos e titulo
        self.canos = Botao(0, 0, 1280, 720, "imagens/detalhes_menu.png", self.janela, None)

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
        jogar_sheet_obj = SpriteSheet(jogar_sheet_img, 15)
        # cria um objeto "ObjAnimado" que é capaz de rodar a animação                            #codigo do rosa usado para transparencia
        self.obj_jogar = ObjAnimado(self.janela, jogar_sheet_obj, 63, 36, 8, (243, 97, 255), 0.2)

        # OPÇÕES
        opcoes_sheet_img = pygame.image.load("imagens/botao_opcoes-sheet.png")
        opcoes_sheet_obj = SpriteSheet(opcoes_sheet_img, 16)
        self.obj_opcoes = ObjAnimado(self.janela, opcoes_sheet_obj, 54, 13, 8, (243, 97, 255), 0.3)

        # FASES
        fases_sheet_img = pygame.image.load("imagens/botao_fases-sheet.png")
        fases_sheet_obj = SpriteSheet(fases_sheet_img, 16)
        self.obj_fases = ObjAnimado(self.janela, fases_sheet_obj, 54, 13, 8, (243, 97, 255), 0.3)

        # SAIR
        sair_sheet_img = pygame.image.load("imagens/botao_sair-sheet.png")
        sair_sheet_obj = SpriteSheet(sair_sheet_img, 16)
        self.obj_sair = ObjAnimado(self.janela, sair_sheet_obj, 54, 13, 8, (243, 97, 255), 0.3)




    def run(self):

        # desenha todos os objetos graficos
        self.background.desenha()
        self.canos.desenha()
        self.botao_fases.desenha()
        self.botao_opcoes.desenha()
        self.botao_sair.desenha()
        self.botao_jogar.desenha()

        # inicia as animações dos botões
        if self.botao_jogar.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
            # permite a animação
            self.obj_jogar.anima()  # permite o loop de animacao

        if self.botao_opcoes.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
            # permite a animação
            self.obj_opcoes.anima()

        if self.botao_fases.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
            # permite a animação
            self.obj_fasesS.anima()

        if self.botao_sair.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
            # permite a animação
            self.obj_sair.anima()

        # atualiza os objetos animados
        self.obj_jogar.update(8 * 92, 8 * 48)
        self.obj_opcoes.update(8 * 13, 8 * 51)
        self.obj_fases.update(8 * 13, 8 * 36)
        self.obj_sair.update(8 * 13, 8 * 67)

        # continua a funcionalidade dos botões pós animação
        if self.obj_jogar.fim_da_animacao():
            proximaFase = fase_1.Fase1(self.janela, self.gerenciador, self.mouse)
            self.gerenciador.set_fase(proximaFase)

        if self.obj_sair.fim_da_animacao():
            # sair da fase
            pygame.quit()
            exit()




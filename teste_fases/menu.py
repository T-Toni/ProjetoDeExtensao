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


    def run(self):
        '''
        # colore a tela
        self.janela.fill('blue')
        '''


        # desenha todos os objetos graficos
        self.background.desenha()
        self.canos.desenha()
        self.botao_fases.desenha()
        self.botao_opcoes.desenha()
        self.botao_sair.desenha()
        self.botao_jogar.desenha()

        # teste para a mudança de fases e botao
        if self.botao_jogar.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
            proximaFase = fase_1.Fase1(self.janela, self.gerenciador, self.mouse)
            self.gerenciador.set_fase(proximaFase)

        if self.botao_sair.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
            #sair da fase
            pygame.quit()
            exit()

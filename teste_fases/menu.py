import pygame
import fase_1
from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
from inventario import Inventario
from item import Item


class Menu:
    def __init__(self, janela, gerenciador):
        self.janela = janela
        self.gerenciador = gerenciador

        self.botao = Botao(100, 100, 200, 200, "imagens/botao_generico.jpg", self.janela, None)

        #teste da animacao
        '''
        #atribui a imagem do spritesheet a variavel
        self.spritesheet = pygame.image.load("imagens/projetil/projetil_sheet.png")

        #cria um objeto "SpriteSheet" (spritesheet, numero total de frames)
        self.fogo = SpriteSheet(self.spritesheet, 23)

        #cria um objeto "ObjAnimado" que é capaz de rodar a animação
        self.obj_fogo = ObjAnimado(self.janela, self.fogo, 32, 32, 10, "black", 0.3)
        '''

        #teste do inventario
        item1 = Item("imagens/verde.jpg", self.janela, None)
        item2 = Item("imagens/verde.jpg", self.janela, None)
        item3 = Item("imagens/verde.jpg", self.janela, None)
        item4 = Item("imagens/verde.jpg", self.janela, None)
        item5 = Item("imagens/verde.jpg", self.janela, None)

        self.inventario = Inventario(self.janela)
        self.inventario.adicionar_item(item1)
        self.inventario.adicionar_item(item2)
        self.inventario.adicionar_item(item3)
        self.inventario.adicionar_item(item4)
        self.inventario.adicionar_item(item5)


    def run(self, mouseX, mouseY, pressionado):
        #colore a tela
        self.janela.fill('blue')

        #apresenta o botão (funcional)
        self.botao.desenha()


        #teste para o inventario
        self.inventario.desenha()


        #teste da animacao
        '''
        if pressionado:
            self.obj_fogo.anima()        #permite o loop de animacao


        self.obj_fogo.update(300, 300)   #atualiza o estado do objeto
        '''

        #teste para a mudança de fases e botao
        if self.botao.clicado(mouseX, mouseY, pressionado):
            proximaFase = fase_1.Fase1(self.janela, self.gerenciador)
            self.gerenciador.set_fase(proximaFase)

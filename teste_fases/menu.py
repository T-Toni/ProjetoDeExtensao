import pygame
import fase_1
from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
from inventario import Inventario
from item import Item


class Menu:
    def __init__(self, janela, gerenciador, mouse):
        self.janela = janela
        self.gerenciador = gerenciador
        self.mouse = mouse

        #teste para os itens
        self.dentro = False


        self.botao = Botao(100, 100, 200, 200, "imagens/botao_generico.jpg", self.janela, None)

        '''
        #teste da animacao
        #atribui a imagem do spritesheet a variavel
        self.spritesheet = pygame.image.load("imagens/projetil/projetil_sheet.png")

        #cria um objeto "SpriteSheet" (spritesheet, numero total de frames)
        self.fogo = SpriteSheet(self.spritesheet, 23)

        #cria um objeto "ObjAnimado" que é capaz de rodar a animação
        self.obj_fogo = ObjAnimado(self.janela, self.fogo, 32, 32, 10, "black", 0.3)
        '''

        #teste do inventario
        self.item1 = Item("item1", "imagens/botao_generico.jpg", self.janela, None, self.mouse)
        self.item2 = Item("item2", "imagens/botao_generico.jpg", self.janela, None, self.mouse)
        self.item3 = Item("item3", "imagens/botao_generico.jpg", self.janela, None, self.mouse)

        self.inventario = Inventario(self.janela)
        self.inventario.adicionar_item(self.item1)
        self.inventario.adicionar_item(self.item2)
        self.inventario.adicionar_item(self.item3)



    def run(self, mouseX, mouseY):
        #colore a tela
        self.janela.fill('blue')



        #teste para os itens
        pygame.draw.rect(self.janela, (130, 30, 30), (100, 100, 100, 100))
        if mouseX > 100 and mouseX < 200 and mouseY > 100 and mouseY < 200:
            self.dentro = True
        else:
            self.dentro = False


        #teste para o inventario
        self.inventario.desenha(self.mouse.getPressionado(), mouseX, mouseY, self.dentro)


        #confere individualmente se os itens atingiram o alvo

        if self.item1:      #confere se o item existe
            if self.item1.atingiuOAlvo:         #confere se atingiu o alvo

                #ação desencadeada pelo item
                #...
                #...

                #print("item " + self.item1.nome + " foi excluido")
                self.inventario.remover_itens(self.item1)
                self.item1 = None

        if self.item2:      #confere se o item existe
            if self.item2.atingiuOAlvo:         #confere se atingiu o alvo

                #ação desencadeada pelo item
                #...
                #...

                #print("item " + self.item2.nome + " foi excluido")
                self.inventario.remover_itens(self.item2)
                self.item2 = None

        if self.item3:      #confere se o item existe
            if self.item3.atingiuOAlvo:         #confere se atingiu o alvo

                #ação desencadeada pelo item
                #...
                #...

                #print("item " + self.item3.nome + " foi excluido")
                self.inventario.remover_itens(self.item3)
                self.item3 = None




        #teste da animacao
        
        #apresenta o botão (funcional)
        self.botao.desenha()

        #teste obj animado

        """
        if self.mouse.getPressionado():
            self.obj_fogo.anima()        #permite o loop de animacao


        self.obj_fogo.update(300, 300)   #atualiza o estado do objeto
        """

        #teste para a mudança de fases e botao
        if self.botao.clicado(mouseX, mouseY, self.mouse.getPressionado()):
            proximaFase = fase_1.Fase1(self.janela, self.gerenciador, self.mouse)
            self.gerenciador.set_fase(proximaFase)


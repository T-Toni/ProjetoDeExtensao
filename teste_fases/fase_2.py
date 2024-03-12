import pygame

from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
import fase_3
import inventario
import item

class Fase2:
    def __init__(self, janela, gerenciador, mouse):
        #necessário pra desenhar
        self.janela = janela
        #necessario para a troca de fases
        self.gerenciador = gerenciador
        #necessário para açôes com o mouse
        self.mouse = mouse

        self.proximaFase = fase_3.Fase3(self.janela, self.gerenciador, self.mouse)

        #OBJETOS DA FASE:

        # backgound (botão, mas não clicavel)
        self.background = Botao(0, 0, 160 * 8, 90 * 8, "imagens/tijolo_background.png", self.janela, None)

        #tanque
        self.tanque = Botao(0, 0, 160 * 8, 90 * 8, "imagens/tanque_fase2.png", self.janela, None)

        #canos
        self.canos = Botao(0, 0, 160 * 8, 90 * 8, "imagens/canos_fase2.png", self.janela, None)

        #cria o inventario
        self.inventario = inventario.Inventario(janela, mouse)

        #parte transparente do tanque
        self.alvo = Botao(37 * 8, 18 * 8, 96 * 8, 44 * 8, "imagens/canos_fase2.png", self.janela, None)

        #guarda o nome do ultimo item a ser retirado
        self.item_retirado = None

        #cria os itens
        cal = item.Item("cal", "imagens/cal.png", janela, None, mouse)
        cloro = item.Item("cloro", "imagens/cloro.png", janela, None, mouse)

        #adiciona os itens ao inventario
        self.inventario.adicionar_item(cal)
        self.inventario.adicionar_item(cloro)

        #guarda se o mouse está sobre o tanque
        self.dentro = False

        self.permitir_transicao = False
        self.transicao = Botao(0, 0, 480*8, 90*8, "imagens/transicao_2-3.png", self.janela, (243, 97, 255))

    def run(self):

        if not self.permitir_transicao:
            #confere se o mouse está sobre o tanque
            if self.alvo.mouse_dentro(self.mouse.getX(), self.mouse.getY()):
                self.dentro = True
            else:
                self.dentro = False

            #remove todos os itens que atigiram o alvo

            i = self.inventario.remover_itens()
            if i != None:
                self.item_retirado = i
            if i == False:   #fim da fase
                self.permitir_transicao = True



            #desenha
            self.background.desenha()
            self.tanque.desenha()
            self.canos.desenha()
            self.inventario.desenha(self.dentro)

            print(self.item_retirado)

        #transição
        else:
            self.transicao.desenha()
            if self.transicao.getX() > (-320 * 8) - 1:
                self.transicao.setX(self.transicao.getX() - 2.7)
            else:
                self.gerenciador.set_fase(self.proximaFase)








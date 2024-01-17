import pygame
import menu
from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado

class Fase1:
    def __init__(self, janela, gerenciador, mouse):
        #necessário pra desenhar
        self.janela = janela
        #necessario para a troca de fases
        self.gerenciador = gerenciador
        #necessário para açôes com o mouse
        self.mouse = mouse

        #OBJETOS DA FASE:

        # backgound (tambem é um botão, mas não clicavel)
        self.background = Botao(0, 0, 1280, 720, "imagens/tijolo_background.png", self.janela, None)
        # botão de trocar de fase
        self.botao = Botao(0, 0, 200, 200, "imagens/botao_generico.jpg", self.janela, None)
        # tanque de agitação
        tanque_sheet_img = pygame.image.load("imagens/tanque_de_agitacao-sheet.png")
        # cria um objeto "SpriteSheet" (spritesheet, numero total de frames)
        self.tanque_sheet_obj = SpriteSheet(tanque_sheet_img, 22)
        # cria um objeto "ObjAnimado" que é capaz de rodar a animação                            #codigo do rosa usado para transparencia
        self.tanque = ObjAnimado(self.janela, self.tanque_sheet_obj, 71, 37, 8, (243, 97, 255), 0)

        #inicia o loop de animação
        self.tanque.anima(400, 200)

        #variaveis para controlar a agitação
        self.sendoSegurado = False
        self.Xinicial = 0
        self.Yinicial = 0
        self.agitacao = 0

    def run(self):

        # desenha todos os objetos graficos
        self.background.desenha()
        self.botao.desenha()
        self.tanque.update()
        #atualiza a posição do tanque
        self.tanque.update_movimentacao(self.mouse.getPressionado(), self.mouse.getX(), self.mouse.getY(), self.mouse.getItem())

        # logica para aumentar a variavel agitação conforme a movimentaçao do tanque
        if self.tanque.sendoSegurado:
            #só será executado na segunda vez que o código for rodado
            if self.sendoSegurado == True:
                #adiciona o valor absoluto da diferença entre a posiçao anterior e a atual
                self.agitacao += abs(self.Xinicial - self.mouse.getX())
                self.agitacao += abs(self.Yinicial - self.mouse.getY())
            #atualiza as posições
            self.Xinicial = self.mouse.getX()
            self.Yinicial = self.mouse.getY()
            self.sendoSegurado = True
        else:
            self.sendoSegurado = False

        #muda o sprite conforme o valor da variavel agitacao
        if self.tanque.spriteAtual < self.tanque_sheet_obj.numeroDeFrames - 0.1:
            self.tanque.setFrame(self.agitacao / 2000)
        else:
            self.tanque.setFrame(self.tanque_sheet_obj.numeroDeFrames - 0.1)







        if self.botao.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
            proximaFase = menu.Menu(self.janela, self.gerenciador, self.mouse)
            self.gerenciador.set_fase(proximaFase)              #muda a fase do gerenciador para a proxima






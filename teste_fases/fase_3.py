import pygame
import menu
from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado

class Fase3:
    def __init__(self, janela, gerenciador, mouse):
        #necessário pra desenhar
        self.janela = janela
        #necessario para a troca de fases
        self.gerenciador = gerenciador
        #necessário para açôes com o mouse
        self.mouse = mouse

        #OBJETOS DA FASE:

        # backgound (tambem é um botão, mas não clicavel)
        self.background = Botao(0, 0, 1280, 720, "imagens/background_3.png", self.janela, None)

        # tanque de agitação
        tanque_sheet_img = pygame.image.load("imagens/tanque_de_agitacao-sheet.png")
        # cria um objeto "SpriteSheet" (spritesheet, numero total de frames)
        self.tanque_sheet_obj = SpriteSheet(tanque_sheet_img, 22)
        # cria um objeto "ObjAnimado" que é capaz de rodar a animação                            #codigo do rosa usado para transparencia
        self.tanque = ObjAnimado(self.janela, self.tanque_sheet_obj, 71, 37, 8, (243, 97, 255), 0)

        #coordenadas do tanque
        self.tanqueX = 43 * 8
        self.tanqueY = 22 * 8

        #medidor de agitação externo
        medidor_sheet_img = pygame.image.load("imagens/medidor_externo_agitacao-sheet.png")
        self.medidor_sheet_obj = SpriteSheet(medidor_sheet_img, 26)
        self.medidor = ObjAnimado(self.janela, self.medidor_sheet_obj, 15, 30, 8, (243, 97, 255), 0)

        #canos
        canos_sheet_img = pygame.image.load("imagens/canos_agitacao-sheet.png")
        self.canos_sheet_obj = SpriteSheet(canos_sheet_img, 5)
        self.canos = ObjAnimado(self.janela, self.canos_sheet_obj, 160, 90, 8, (243, 97, 255), 0.05)

        #botão para a proxima fase
        self.botao = Botao(130 * 8, 45 * 8, 11*8, 11*8, "imagens/botao_cano.png", self.janela, (243, 97, 255))

        #seta para sinalizar o botão
        self.seta = Botao(128 * 8, 57 * 8, 15*8, 22*8, "imagens/seta_verde.png", self.janela, (243, 97, 255))

        #inicia o loop de animação
        self.tanque.anima(self.tanqueX, self.tanqueY)
        self.medidor.anima(122 * 8, 5 * 8)
        self.canos.anima(0, 0)

        #variaveis para controlar a agitação
        self.sendoSegurado = False
        self.Xinicial = 0
        self.Yinicial = 0
        self.agitacao = 0
        self.agitado = False    # se o tanque ja terminou de ser agitado
        self.divisor = 1000     # numero que vai dividor a agitação para selecionar o frame
        self.i = 0              #usada pra animação da seta

    def run(self):

        #executa a animação dos canos ao inicio da fase
        if self.canos.spriteAtual < self.canos_sheet_obj.numeroDeFrames - 0.1 and self.canos.velocidade != 0:
            self.background.desenha()
            self.botao.desenha()
            self.tanque.update()
            self.medidor.update()
            self.canos.update()
            self.botao.desenha()

        #é executado após o fim da animação de inicio da fase
        else:
            if self.canos.velocidade != 0:
                self.canos.velocidade = 0
                self.canos.spriteAtual = self.canos_sheet_obj.numeroDeFrames - 1

            # desenha todos os objetos graficos
            self.background.desenha()
            self.botao.desenha()
            self.medidor.update()
            self.canos.update()
            self.botao.desenha()
            self.tanque.update()


            #atualiza a posição do tanque
            if self.agitado == False:
                self.tanque.update_movimentacao(self.mouse.getPressionado(), self.mouse.getX(), self.mouse.getY(), self.mouse.getItem())
            #retorna o tanque a posição original
            else:
                velocidadeDeRetornoX = 5
                #caso x seja menor que o original
                if self.tanque.getX() < self.tanqueX:
                    if self.tanqueX - self.tanque.getX() >= velocidadeDeRetornoX:
                        self.tanque.setX(self.tanque.getX() + velocidadeDeRetornoX)
                    else:
                        self.tanque.setX(self.tanqueX)
                # caso x seja maior que o original
                if self.tanque.getX() > self.tanqueX:
                    if self.tanque.getX() - self.tanqueX >= velocidadeDeRetornoX:
                        self.tanque.setX(self.tanque.getX() - velocidadeDeRetornoX)
                    else:
                        self.tanque.setX(self.tanqueX)

                velocidadeDeRetornoY = 1.5
                # caso Y seja menor que o original
                if self.tanque.getY() < self.tanqueY:
                    if self.tanqueY - self.tanque.getY() >= velocidadeDeRetornoY:
                        self.tanque.setY(self.tanque.getY() + velocidadeDeRetornoY)
                    else:
                        self.tanque.setY(self.tanqueY)

                # caso Y seja maior que o original
                if self.tanque.getY() > self.tanqueY:
                    if self.tanque.getY() - self.tanqueY >= velocidadeDeRetornoY:
                        self.tanque.setY(self.tanque.getY() - velocidadeDeRetornoY)
                    else:
                        self.tanque.setY(self.tanqueY)



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
            if self.tanque.spriteAtual < self.tanque_sheet_obj.numeroDeFrames - 1:
                if self.agitacao / self.divisor < 21:
                    self.tanque.setFrame(self.agitacao / self.divisor)
                    self.medidor.setFrame(self.agitacao / self.divisor)
                else:
                    self.tanque.setFrame(self.tanque_sheet_obj.numeroDeFrames - 1)
                    self.medidor.setFrame(self.tanque_sheet_obj.numeroDeFrames - 1)

            else:
                self.agitado = True
                self.tanque.setFrame(self.tanque_sheet_obj.numeroDeFrames - 0.1)
                self.medidor.altLoop(23, 26, 0.1)

                #confere a posição do tanque para fazer  a animação dos canos se fechando
                if self.tanque.getX() == self.tanqueX and self.tanque.getY() == self.tanqueY:
                    if self.medidor.spriteAtual > 0:
                        self.canos.revLoop(0, 4, 0.05)
                    else:
                        self.canos.setFrame(0)

                    if self.canos.spriteAtual == 0:
                        #permite o pressionamento do botão
                        if self.botao.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
                            proximaFase = menu.Menu(self.janela, self.gerenciador, self.mouse)
                            self.gerenciador.set_fase(proximaFase)  # muda a fase do gerenciador para a proxima

                        # desenha a seta
                        self.seta.desenha()

                        #logica para animação da seta
                        if self.seta.y <= (57 * 8):
                            self.i = 1
                        if self.seta.y >= (67 * 8):
                            self.i = 0

                        if 1 == self.i:
                            self.seta.y = self.seta.y + 2
                        else:
                            self.seta.y = self.seta.y - 2












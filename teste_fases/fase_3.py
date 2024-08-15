import pygame
import transicao_3
from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
import texto

class Fase3:
    def __init__(self, janela, gerenciador, mouse, mixer):
        #inicializa o mixer
        self.mixer = mixer

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
        self.tanqueXInicial = 43 * 8
        self.tanqueYInicial = 22 * 8

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
        self.posicao = 0    #para controlar a movimentação do tanque pelas setas (1 = direita, 0 centro, -1 esquerda)
        self.agitacao = 0
        self.agitado = False    # se o tanque ja terminou de ser agitado
        self.divisor = 1000     # numero que vai dividor a agitação para selecionar o frame
        self.i = 0              #usada pra animação da seta

        #fim da fase
        self.fase_completa = False
        self.transicao = Botao(0, 0, 480*8, 90*8, "imagens/transicao_3-4.png", self.janela, (243, 97, 255))

        # INTRODUCAO ( tamanho maximo(para25):
        # ---------'água, desde a represa até água chegar em sua casa!')
        texto1_1 = 'Essa etapa é conhecida como Coagulação, e resume-'
        texto1_2 = 'se em agitar vigorosamente o tanque para garantir'
        texto1_3 = 'a mistura dos químicos adicionados na etapa'
        texto1_4 = 'anterior à água.'

        texto2_1 = 'Pressione as setas da direita e depois a da'
        texto2_2 = 'esquerda rapidamente para agitar o tanque.'
        texto2_3 = None
        texto2_4 = None

        texto3_1 = 'Parabéns!!! A água foi agitada corretamente.'
        texto3_2 = 'Pressione a seta para a direita para continuar.'
        texto3_3 = None
        texto3_4 = None

        self.intro1 = texto.Texto(texto1_1, texto1_2, texto1_3, texto1_4, 0, self.janela, 2)
        self.intro2 = texto.Texto(texto2_1, texto2_2, texto2_3, texto2_4, 0, self.janela, 3)
        self.outro = texto.Texto(texto3_1, texto3_2, texto3_3, texto3_4, 0, self.janela, 1)

        self.intro1_iniciada = False
        self.intro2_iniciada = False
        self.outro_iniciado = False

    def run(self):
        teclas = pygame.key.get_pressed()

        # função para pular falas
        self.mixer.update(teclas)

        #executa a animação dos canos ao inicio da fase
        if self.canos.spriteAtual < self.canos_sheet_obj.numeroDeFrames - 0.1 and self.canos.velocidade != 0:

            #toca a intro
            if not self.intro1_iniciada:
                self.mixer.toca_fala('introducao3.1')
                self.intro1_iniciada = True

            self.background.desenha()
            self.botao.desenha()
            self.tanque.update()
            self.medidor.update()
            self.canos.update()
            self.botao.desenha()

        elif not self.intro2_iniciada:
            if not self.mixer.tocando_falas():
                self.mixer.toca_fala('introducao3.2')
                self.intro2_iniciada = True


        #é executado após o fim da animação de inicio da fase
        elif not self.fase_completa:
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
                # atualiza a posição do tanque
                self.tanque.setX(self.tanqueX)

                # logica para a movimentação do tanque

                offset = 6 * 8
                incremento = 50
                divisor = 4

                if teclas[pygame.K_LEFT] and self.posicao != -1 and not teclas[pygame.K_RIGHT]:

                    if self.tanqueX >= self.tanqueXInicial - incremento / 2:

                        self.tanqueX -= incremento / divisor
                        self.agitacao += incremento


                if teclas[pygame.K_RIGHT] and self.posicao != 1 and not teclas[pygame.K_LEFT]:

                    if self.tanqueX <= self.tanqueXInicial + incremento / 2:

                        self.tanqueX += incremento / divisor
                        self.agitacao += incremento





            #retorna o tanque a posição original
            else:
                velocidadeDeRetornoX = 1
                #caso x seja menor que o original
                if self.tanque.getX() < self.tanqueXInicial:
                    if self.tanqueXInicial - self.tanque.getX() >= velocidadeDeRetornoX:
                        self.tanque.setX(self.tanque.getX() + velocidadeDeRetornoX)
                    else:
                        self.tanque.setX(self.tanqueX)
                # caso x seja maior que o original
                if self.tanque.getX() > self.tanqueXInicial:
                    if self.tanque.getX() - self.tanqueXInicial >= velocidadeDeRetornoX:
                        self.tanque.setX(self.tanque.getX() - velocidadeDeRetornoX)
                    else:
                        self.tanque.setX(self.tanqueX)

                """velocidadeDeRetornoY = 1.5
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
                        self.tanque.setY(self.tanqueY)"""



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
                #toca o audio de fim da fase
                if not self.outro_iniciado:
                    self.mixer.toca_fala('fim_fase3')
                    self.outro_iniciado = True
                self.tanque.setFrame(self.tanque_sheet_obj.numeroDeFrames - 0.1)
                self.medidor.altLoop(23, 26, 0.1)

                #confere a posição do tanque para fazer  a animação dos canos se fechando
                if self.tanque.getX() == self.tanqueXInicial and self.tanque.getY() == self.tanqueYInicial:
                    if self.medidor.spriteAtual > 0:
                        self.canos.revLoop(0, 4, 0.05)
                    else:
                        self.canos.setFrame(0)

                    if self.canos.spriteAtual == 0:
                        self.fase_completa = True   #determina que a fase terminou

        else:


            self.medidor.altLoop(23, 26, 0.1)

            self.transicao.desenha()
            self.medidor.update()

            #logica para transicao de fases
            velocidade = 3

            if self.transicao.getX() >= -160 * 8:
                if teclas[pygame.K_RIGHT]:
                    self.transicao.setX(self.transicao.getX() - velocidade)
                    self.medidor.setX(self.medidor.getX() - velocidade)

            else:
                self.proximaFase = transicao_3.Transicao_3(self.janela, self.gerenciador, self.mouse, self.mixer)
                self.gerenciador.set_fase(self.proximaFase)



        if self.mixer.get_audio_atual(0) == 'introducao3.1':
            self.intro1.escreve()

        if self.mixer.get_audio_atual(0) == 'introducao3.2':
            self.intro2.escreve()

        if self.mixer.get_audio_atual(0) == 'fim_fase3':
            self.outro.escreve()






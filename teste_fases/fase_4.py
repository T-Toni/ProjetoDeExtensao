import pygame
import menu
from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
import transicao_4
import texto

class Fase4:
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
        self.background = Botao(0, 0, 1280, 720, "imagens/tijolo_background3.png", self.janela, None)

        #coordenadas do tanque
        self.tanqueXInicial = 61 * 8
        self.tanqueYInicial = 10 * 8

        # tanque de agitação
        self.tanque = Botao(self.tanqueXInicial, self.tanqueYInicial, 39*8, 71*8, "imagens/tanque_fase4.png", self.janela, (243, 97, 255))

        self.tanqueX = self.tanqueXInicial
        self.tanqueY = self.tanqueYInicial

        #medidor de progressão
        medidor_sheet_img = pygame.image.load("imagens/medidor_fase4-sheet.png")
        self.medidor_progressao_sheet_obj = SpriteSheet(medidor_sheet_img, 24)
        self.medidor_progressao = ObjAnimado(self.janela, self.medidor_progressao_sheet_obj, 160, 90, 8, (243, 97, 255), 0)

        #medidor de velocidade
        self.medidor_velocidade = Botao(0 * 8, 0 * 8, 34*8, 33*8, "imagens/medidor_velocidade.png", self.janela, (243, 97, 255))

        #canos
        canos_sheet_img = pygame.image.load("imagens/canos_fase4-sheet.png")
        self.canos_sheet_obj = SpriteSheet(canos_sheet_img, 5)
        self.canos = ObjAnimado(self.janela, self.canos_sheet_obj, 160, 90, 8, (243, 97, 255), 0.05)

        #ponteiro do medidor de velocidade
        imagem_ponteiro = pygame.image.load("imagens/ponteiro.png")
        self.ponteiro = pygame.transform.scale(imagem_ponteiro, (2*8, 20*8))
        self.ponteiro_rect = self.ponteiro.get_rect(center=(18 * 8, 17 * 8))
        #copia o ponteiro
        self.copia = self.ponteiro.copy()
        self.copia_rect = self.copia.get_rect(center=(18 * 8, 17 * 8))   #rect da copia do ponteiro

        self.angulo = 0                 #controla o angulo da rotacao

        self.ajuste_angulo = 0          #ajusta o angulo

        #inicia o loop de animação
        self.medidor_progressao.anima(0, 0)
        self.canos.anima(0, 0)

        #variaveis para controlar a agitação
        self.posicao = 0    #para controlar a movimentação do tanque pelas setas (1 = direita, 0 centro, -1 esquerda)
        self.agitacao = 0
        self.agitado = False    # se o tanque ja terminou de ser agitado
        self.progresso = 0

        #transição:
        self.permite_Transicao = False
        self.transicao = Botao(0, 0, 480*8, 90*8, "imagens/transicao_4-5.png", self.janela, (243, 97, 255))
        self.decrescimo = 0

        # INTRODUCAO ( tamanho maximo(para25):
        # ---------'água, desde a represa até água chegar em sua casa!')
        texto1_1 = 'Essa etapa chama-se Floculação e é parecida com a'
        texto1_2 = 'anterior, mas agora você deve agitar o tanque em'
        texto1_3 = 'uma velocidade moderada, nem muito rápido nem'
        texto1_4 = 'muito devagar.'

        texto2_1 = 'Tente manter o medidor no canto superior esquerdo'
        texto2_2 = 'da tela no verde. Pressione as setas para cima e'
        texto2_3 = 'para baixo para agitar o tanque.'
        texto2_4 = None

        texto3_1 = 'Muito bem! Agora a água deve ficar um pouco em'
        texto3_2 = 'repouso para a sujeira se juntar no fundo do'
        texto3_3 = 'tanque e a água da parte de cima poder'
        texto3_4 = 'seguir para a próxima etapa.'

        texto4_1 = 'Pressione a seta para a direita para seguir com'
        texto4_2 = 'o tratamento'
        texto4_3 = None
        texto4_4 = None

        self.intro1 = texto.Texto(texto1_1, texto1_2, texto1_3, texto1_4, 0, self.janela, 2)
        self.intro2 = texto.Texto(texto2_1, texto2_2, texto2_3, texto2_4, 0, self.janela, 2)
        self.outro1 = texto.Texto(texto3_1, texto3_2, texto3_3, texto3_4, 0, self.janela, 1)
        self.outro2 = texto.Texto(texto4_1, texto4_2, texto4_3, texto4_4, 0, self.janela, 2)

        self.intro1_iniciada = False
        self.intro2_iniciada = False
        self.outro1_iniciado = False
        self.outro2_iniciado = False



    def run(self):

        teclas = pygame.key.get_pressed()

        # função para pular falas
        self.mixer.update(teclas)

        if not self.intro1_iniciada:
            self.mixer.toca_fala('introducao4.1')
            self.intro1_iniciada = True
        elif not self.intro2_iniciada and not self.mixer.tocando_falas():
            self.mixer.toca_fala('introducao4.2')
            self.intro2_iniciada = True

        if not self.permite_Transicao:

            #executa a animação dos canos ao inicio da fase
            if self.canos.spriteAtual < self.canos_sheet_obj.numeroDeFrames - 0.1 and self.canos.velocidade != 0:
                self.background.desenha()
                self.medidor_progressao.update()
                self.medidor_velocidade.desenha()
                self.canos.update()
                self.tanque.desenha()
                self.janela.blit((self.copia), self.copia_rect.topleft)

            #é executado após o fim da animação de inicio da fase
            else:
                if self.canos.velocidade != 0:
                    self.canos.velocidade = 0
                    self.canos.spriteAtual = self.canos_sheet_obj.numeroDeFrames - 1

                # desenha todos os objetos graficos
                self.background.desenha()
                self.medidor_progressao.update()
                self.medidor_velocidade.desenha()
                self.canos.update()
                self.tanque.desenha()
                self.janela.blit((self.copia), self.copia_rect.topleft)


                #atualiza a posição do tanque
                if self.agitado == False:
                    # atualiza a posição do tanque
                    self.tanque.setX(self.tanqueX)

                    offset = 3 * 8
                    incremento = 120
                    divisor = 1.5         #valor que divide o offset para dar a velocidade de movimentacao do tanque


                    if teclas[pygame.K_UP] and self.posicao != -1 and not teclas[pygame.K_DOWN]:

                        if self.tanque.y >= self.tanqueYInicial - offset:

                            self.tanque.y -= offset / divisor
                            self.agitacao += incremento     # incrementa a variavel de agitação

                    elif teclas[pygame.K_DOWN] and self.posicao != 1 and not teclas[pygame.K_UP]:

                        if self.tanque.y <= self.tanqueYInicial + offset:
                            self.tanque.y += offset / divisor
                            self.agitacao += incremento


                    #limita a variavel de agitacao
                    limite = 5000

                    self.agitacao -= incremento / 2.5    #decresce a variavel de agitação
                    if self.agitacao > limite:
                        self.agitacao = limite
                    if self.agitacao <= 0:
                        self.agitacao = 0

                    #AJUSTE
                    i = self.agitacao / (limite / 2)

                    if i < 1 and i >= 0:
                        ajuste = i
                    else:
                        ajuste = abs(i - 2)

                    #print("ajuste: " + str(ajuste))

                    self.progresso += incremento/3 * ajuste

                    #("progresso: " + str(self.progresso))

                    #muda o sprite conforme o valor da variavel agitacao
                    if self.medidor_progressao.spriteAtual < self.medidor_progressao_sheet_obj.numeroDeFrames - 4:

                        divisor = 1000

                        if self.progresso / divisor < self.medidor_progressao_sheet_obj.numeroDeFrames - 4:
                            self.medidor_progressao.setFrame(self.progresso / divisor)
                        else:
                            self.medidor_progressao.setFrame(self.medidor_progressao_sheet_obj.numeroDeFrames - 4)

                    else:
                        self.agitado = True


                    #ROTACIONA O PONTEIRO
                    if i < 1 and i >= 0:
                        self.angulo = (i * 170) - 170
                    else:
                        self.angulo = ((abs(i - 2) * 170) - 170) * -1

                    self.copia = pygame.transform.rotate(self.ponteiro, -self.angulo)
                    self.copia_rect = self.copia.get_rect(center = self.ponteiro_rect.center)


                #retorna o tanque a posição original
                else:

                    #toca as falas do fim da fase
                    if not self.outro1_iniciado:
                        self.mixer.toca_fala('fim_fase4.1')
                        self.outro1_iniciado = True

                    #inicia o loop alternativo de animação do medidor
                    self.medidor_progressao.altLoop(21, 24, 0.1)

                    #retorna o ponteiro para a sua posição inicial

                    if self.angulo > -170:
                        self.angulo = self.angulo - 3
                        self.copia = pygame.transform.rotate(self.ponteiro, -self.angulo)
                        self.copia_rect = self.copia.get_rect(center = self.ponteiro_rect.center)
                    else:
                        self.angulo = -170
                        self.copia = pygame.transform.rotate(self.ponteiro, -self.angulo)
                        self.copia_rect = self.copia.get_rect(center = self.ponteiro_rect.center)


                    velocidadeDeRetorno = 1
                    #caso x seja menor que o original
                    if self.tanque.getY() < self.tanqueYInicial:
                        if self.tanqueYInicial - self.tanque.getY() >= velocidadeDeRetorno:
                            self.tanque.setY(self.tanque.getY() + velocidadeDeRetorno)
                        else:
                            self.tanque.setY(self.tanqueY)
                    # caso x seja maior que o original
                    if self.tanque.getY() > self.tanqueYInicial:
                        if self.tanque.getY() - self.tanqueYInicial >= velocidadeDeRetorno:
                            self.tanque.setY(self.tanque.getY() - velocidadeDeRetorno)
                        else:
                            self.tanque.setY(self.tanqueY)



                    #confere a posição do tanque para fazer  a animação dos canos se fechando
                    if self.tanque.getX() == self.tanqueXInicial and self.tanque.getY() == self.tanqueYInicial:
                        if self.canos.spriteAtual > 0:
                            self.canos.revLoop(0, 4, 0.05)
                        else:
                            self.canos.setFrame(0)

                        if self.canos.spriteAtual == 0:
                            self.permite_Transicao = True
        else:
            self.medidor_progressao.altLoop(21, 24, 0.05)
            self.transicao.desenha()
            self.medidor_progressao.update()
            self.medidor_velocidade.desenha()
            self.janela.blit((self.copia), (15 * 8 + self.decrescimo, 7 * 8))

            #toca a ultima fala da fase
            if not self.outro2_iniciado and not self.mixer.tocando_falas() and self.outro1_iniciado:
                self.mixer.toca_fala('fim_fase4.2')
                self.outro2_iniciado = True

            if self.transicao.getX() > (-160 * 8) - 1:

                #Verifica se a seta para a direita está sendo pressionada
                if teclas[pygame.K_RIGHT]:
                    velocidade = 3

                    self.transicao.setX(self.transicao.getX() - velocidade)
                    self.medidor_progressao.setX(self.medidor_progressao.getX() - velocidade)
                    self.medidor_velocidade.setX(self.medidor_velocidade.getX() - velocidade)
                    self.decrescimo -= velocidade

            else:
                proximaFase = transicao_4.Transicao_4(self.janela, self.gerenciador, self.mouse, self.mixer)
                self.gerenciador.set_fase(proximaFase)  # muda a fase do gerenciador para a proxima



        if self.mixer.get_audio_atual(0) == 'introducao4.1':
            self.intro1.escreve()

        if self.mixer.get_audio_atual(0) == 'introducao4.2':
            self.intro2.escreve()

        if self.mixer.get_audio_atual(0) == 'fim_fase4.1':
            self.outro1.escreve()

        if self.mixer.get_audio_atual(0) == 'fim_fase4.2':
            self.outro2.escreve()



    """ def rotaciona_esq(self):
        self.copia = pygame.transform.rotate(self.ponteiro, -90)
        self.copia_rect = self.copia.get_rect(center = self.ponteiro_rect.center)

    def rotaciona_dir(self):
        print("dor")
        self.copia = pygame.transform.rotate(self.ponteiro, 90)
        self.copia_rect = self.copia.get_rect(center = self.ponteiro_rect.center)"""

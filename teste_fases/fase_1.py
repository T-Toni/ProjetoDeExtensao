import pygame

from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
import fase_3
import fase_2
import transicao_1
import narracao
import texto


class Fase1:
    def __init__(self, janela, gerenciador, mouse, mixer):
        #inicializa o mixer
        self.mixer = mixer


        #necessário pra desenhar
        self.janela = janela
        #necessario para a troca de fases
        self.gerenciador = gerenciador
        #necessário para açôes com o mouse
        self.mouse = mouse

        self.proximaFase = transicao_1.Transicao_1(self.janela, self.gerenciador, self.mouse, self.mixer)

        #OBJETOS DA FASE:

        # backgound (obj animado)
        represa_sheet_img = pygame.image.load("imagens/represa-sheet.png")
        # cria um objeto "SpriteSheet" (spritesheet, numero total de frames)
        self.represa_sheet_obj = SpriteSheet(represa_sheet_img, 41)
        # cria um objeto "ObjAnimado" que é capaz de rodar a animação                            #codigo do rosa usado para transparencia
        self.represa = ObjAnimado(self.janela, self.represa_sheet_obj, 160, 90, 8, (243, 97, 255), 0)

        self.represa.anima(0, 0)

        #botão para liberar o fluxo
        self.botao = Botao(130 * 8, 46 * 8, 17*8, 17*8, None, self.janela, (243, 97, 255))

        #imagem de transição
        self.permitir_transicao = False
        self.transicao = Botao(0, 0, 480*8, 90*8, "imagens/transicao_1-2.png", self.janela, (243, 97, 255))

        #sons

        #TIRAR
        self.agua = pygame.mixer.Channel(0)
        self.agua.stop()    #para o som da tela anterior

        #variaveis booleanas para controlar os eventos
        self.concluiu_intro1 = False
        self.concluiu_intro2 = False
        self.concluiu_intro3 = False
        self.concluiu_intro = False

        self.pressionou = False


        self.concluiu_fim = False

        #INTRODUCAO ( tamanho maximo(para25): 'água, desde a represa até água chegar em sua casa!')
        texto1_1 = 'Olá, eu me chamo Sabrino e eu trabalho aqui'
        texto1_2 = 'na estação de tratamento de agua!'
        texto1_3 = 'E vou te mostrar todas as etapas do tratamento da'
        texto1_4 = 'água, desde a represa até água chegar em sua casa!'

        texto2_1 = 'Essa água que está na represa está suja,'
        texto2_2 = 'e precisa ser limpa, para se tornar'
        texto2_3 = 'potável e poder ser utilizada.'
        texto2_4 = None

        texto3_1 = 'Aperte [ESPAÇO] para liberar a passagem da água'
        texto3_2 = 'da represa para a estação de tratamento.'
        texto3_3 = None
        texto3_4 = None

        texto4_1 = 'Para transportar a água, são usados canos chamados'
        texto4_2 = 'de tubulação hidráulica! Pressione a [SETA->]'
        texto4_3 = 'para a direita para seguir com o tratamento.'
        texto4_4 = None


        self.intro1 = texto.Texto(texto1_1, texto1_2, texto1_3, texto1_4, 2, self.janela)
        self.intro2 = texto.Texto(texto2_1, texto2_2, texto2_3, texto2_4, 2, self.janela)
        self.intro3 = texto.Texto(texto3_1, texto3_2, texto3_3, texto3_4, 2, self.janela)

        self.pos_pressionamento = texto.Texto(texto4_1, texto4_2, texto4_3, texto4_4, 0, self.janela)

    def run(self):

        teclas = pygame.key.get_pressed()

        #desenha
        self.represa.update()
        self.botao.desenha()

        #função para pular falas
        self.mixer.update(teclas)

        if not self.concluiu_intro1:
            self.mixer.toca_fala('introducao1')
            self.concluiu_intro1 = True
        elif not self.concluiu_intro2 and not self.mixer.tocando_falas():
            self.mixer.toca_fala('introducao2')
            self.concluiu_intro2 = True
        elif not self.concluiu_intro3 and not self.mixer.tocando_falas():
            self.mixer.toca_fala('introducao3')
            self.concluiu_intro3 = True


        if not self.mixer.tocando_falas() and self.concluiu_intro3:
            self.concluiu_intro = True



        if self.concluiu_intro:

            if (self.botao.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()) or teclas[pygame.K_SPACE]) and not self.pressionou:
                #self.agua.play(self.bolha, 0)
                self.mixer.toca_som('bolhas1')
                self.represa.setVelocidade(0.15)
                self.pressionou = True

            if self.represa.getFrame() >= self.represa_sheet_obj.numeroDeFrames - 1 or self.permitir_transicao:
                self.permitir_transicao = True
                self.transicao.desenha()


                #toca o audio
                if not self.concluiu_fim:
                    #self.finalizacao.play()
                    self.mixer.toca_fala('pos_pressionamento')
                    self.concluiu_fim = True

                if self.mixer.tocando_falas():
                    self.pos_pressionamento.escreve()

                #confere se ja chegou na proxima tela
                if self.transicao.getX() > (-160 * 8) - 1:
                    teclas = pygame.key.get_pressed()

                    #Verifica se a seta para a direita está sendo pressionada
                    if teclas[pygame.K_RIGHT]:
                        self.transicao.setX(self.transicao.getX() - 3)

                else:
                    self.gerenciador.set_fase(self.proximaFase)


        else:
            if not self.concluiu_intro2:
                self.intro1.escreve()

            elif not self.concluiu_intro3:
                self.intro2.escreve()

            else:
                self.intro3.escreve()





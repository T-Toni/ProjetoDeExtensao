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

        self.concluiu_intro = False

        self.concluiu_fim = False

        #teste fonte ( tamanho maximo: Essa água que está na represa está suja, e precisa ser limpa)
        texto1 = 'Essa água que está na represa está suja, e precisa ser limpa'
        texto2 = 'para se tornar potável e poder ser utilizada.'
        texto3 = 'Aperte espaço para liberar a passagem da água da represa'
        texto4 = 'para a estação de tratamento.'

        self.texto = texto.Texto(texto1, texto2, texto3, texto4, 1, self.janela)

    def run(self):

        teclas = pygame.key.get_pressed()

        #desenha
        self.represa.update()
        self.botao.desenha()

        #função para pular falas
        self.mixer.update(teclas)

        if not self.concluiu_intro:
            #self.introducao.play()
            self.mixer.toca_fala('introducao')
            self.concluiu_intro = True
        else:
            if not self.mixer.tocando_falas():

                if self.botao.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()) or teclas[pygame.K_SPACE]:
                    #self.agua.play(self.bolha, 0)
                    self.mixer.toca_som('bolhas1')
                    self.represa.setVelocidade(0.15)

                if self.represa.getFrame() >= self.represa_sheet_obj.numeroDeFrames - 1 or self.permitir_transicao:
                    self.permitir_transicao = True
                    self.transicao.desenha()


                    #toca o audio
                    if not self.concluiu_fim:
                        #self.finalizacao.play()
                        self.mixer.toca_fala('pos_pressionamento')
                        self.concluiu_fim = True
                    """else:
                        if not self.finalizacao.tocando():"""

                    #confere se ja chegou na proxima tela
                    if self.transicao.getX() > (-160 * 8) - 1:
                        teclas = pygame.key.get_pressed()

                        #Verifica se a seta para a direita está sendo pressionada
                        if teclas[pygame.K_RIGHT]:
                            self.transicao.setX(self.transicao.getX() - 3)

                    else:
                        self.gerenciador.set_fase(self.proximaFase)


            else:
                self.texto.escreve()




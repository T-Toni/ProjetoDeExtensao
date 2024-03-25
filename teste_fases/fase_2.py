import pygame

from botao import Botao
from SpriteSheet import SpriteSheet
from obj_animado import ObjAnimado
import fase_3
from sujeira import Sujeira
from cloro import Cloro
from Rede_Neural import RedeNeural

class Fase2:
    def __init__(self, janela, gerenciador, mouse):
        #necessário pra desenhar
        self.janela = janela
        #necessario para a troca de fases
        self.gerenciador = gerenciador
        #necessário para açôes com o mouse
        self.mouse = mouse

        self.proximaFase = None

        #OBJETOS DA FASE:

        # backgound (botão, mas não clicavel)
        self.background = Botao(0, 0, 160 * 8, 90 * 8, "imagens/tijolo_background.png", self.janela, None)

        #tanque
        self.tanque = Botao(0, 0, 160 * 8, 90 * 8, "imagens/tanque_fase2.png", self.janela, None)
        #indicador do medidor de ph
        self.medidor = Botao(32 * 8, 42 * 8, 2 * 8, 1 * 8, "imagens/medidor_ph.png", self.janela, None)
        #animação que evidencia o ph ideal
        ph_ideal_sheet_img = pygame.image.load("imagens/ph_ideal-sheet.png")
        self.ph_ideal_sheet = SpriteSheet(ph_ideal_sheet_img, 5)
        self.ph_ideal = ObjAnimado(self.janela, self.ph_ideal_sheet, 160, 90, 8, (243, 97, 255), 0)
        self.ph_ideal.anima(0, 0)
        self.ph_ideal.setRepetir()  #permite o looping da animação

        #animação do cal sendo despejado
        cal_sheet_img = pygame.image.load("imagens/animacao_cal.png")
        self.cal_sheet = SpriteSheet(cal_sheet_img, 20)
        self.animacao_cal = ObjAnimado(self.janela, self.cal_sheet, 8, 8, 8, (243, 97, 255), 0)
        self.animacao_cal.anima(47 * 8, 6 * 8)
        self.animacao_cal.setRepetir()
        self.indo = True    #determina a direção do obj animado

        """#animação da conclusão do uso do cal
        brilho_sheet_img = pygame.image.load("imagens/brilho_cal-sheet.png")
        self.brilho_sheet = SpriteSheet(brilho_sheet_img, 140)
        self.brilho = ObjAnimado(self.janela, self.brilho_sheet, 96 * 8, 44 * 8, 8, (243, 97, 255), 0)
        self.brilho.anima(37 * 8, 18 * 8)"""

        #canos
        self.canos = Botao(0, 0, 160 * 8, 90 * 8, "imagens/canos_fase2.png", self.janela, None)

        #agua
        self.agua = Botao(0, 0, 160 * 8, 90 * 8, "imagens/agua_fase2.png", self.janela, None)
        #sujeira da agua
        self.sujeira = Botao(0, 0, 160 * 8, 90 * 8, "imagens/sujeira_fase2.png", self.janela, None)
        self.opacidade = 160    #255 totalmente opaco - 0 transparente"""

        #borda dos itens selecionados
        self.borda_cal = Botao(39 * 8, 74 * 8, 18 * 8, 17 * 8, "imagens/cal_selecionado.png", self.janela, None)
        self.borda_cloro = Botao(105 * 8, 74 * 8, 18 * 8, 17 * 8, "imagens/cloro_selecionado.png", self.janela, None)
        #indicador de que o item ja foi usado
        self.concluido_cal = Botao(39 * 8, 74 * 8, 18 * 8, 17 * 8, "imagens/concluido.png", self.janela, None)
        self.concluido_cloro = Botao(105 * 8, 74 * 8, 18 * 8, 17 * 8, "imagens/concluido.png", self.janela, None)

        #inventario (obs: não é um inventario da classe inventario)
        self.inventario = Botao(10 * 8, 71 * 8, 140 * 8, 20 * 8, "imagens/inventario.png", self.janela, None)

        #itens (obs: não são itens da classe item)
        self.cal = Botao(40 * 8, 74 * 8, 16 * 8, 16 * 8, "imagens/cal.png", self.janela, None)
        self.cloro = Botao(106 * 8, 74 * 8, 16 * 8, 16 * 8, "imagens/cloro.png", self.janela, None)

        #determina se os itens foram utilizados
        self.cloro_usado = False
        self.cal_usado = False

        #seletor (determina o item selecionado)
        self.selecionado = self.borda_cal

        #transição entre essa fase e a proxima
        self.permitir_transicao = False
        self.transicao = Botao(0, 0, 480*8, 90*8, "imagens/transicao_2-3.png", self.janela, (243, 97, 255))

        #CLORO

        #determina o limite de onde as sujeiras podem andar
        limite_inferior = 62 * 8 - 8
        limite_superior = 19 * 8 + 13 * 8 #soma para garantir que a parte superior do tanque esteja sem sujeiras
        limite_esquerdo = 38 * 8 + 8
        limite_direito = 133 * 8 - 8

        sujeira1 = Sujeira(1*8, 1*8, "imagens/sujeira.png", self.janela, (243, 97, 255), limite_esquerdo, limite_direito, limite_superior, limite_inferior)
        sujeira2 = Sujeira(1*8, 1*8, "imagens/sujeira.png", self.janela, (243, 97, 255), limite_esquerdo, limite_direito, limite_superior, limite_inferior)
        sujeira3 = Sujeira(1*8, 1*8, "imagens/sujeira.png", self.janela, (243, 97, 255), limite_esquerdo, limite_direito, limite_superior, limite_inferior)
        sujeira4 = Sujeira(1*8, 1*8, "imagens/sujeira.png", self.janela, (243, 97, 255), limite_esquerdo, limite_direito, limite_superior, limite_inferior)
        sujeira5 = Sujeira(1*8, 1*8, "imagens/sujeira.png", self.janela, (243, 97, 255), limite_esquerdo, limite_direito, limite_superior, limite_inferior)
        sujeira6 = Sujeira(1*8, 1*8, "imagens/sujeira.png", self.janela, (243, 97, 255), limite_esquerdo, limite_direito, limite_superior, limite_inferior)
        sujeira7 = Sujeira(1*8, 1*8, "imagens/sujeira.png", self.janela, (243, 97, 255), limite_esquerdo, limite_direito, limite_superior, limite_inferior)
        sujeira8 = Sujeira(1*8, 1*8, "imagens/sujeira.png", self.janela, (243, 97, 255), limite_esquerdo, limite_direito, limite_superior, limite_inferior)
        sujeira9 = Sujeira(1*8, 1*8, "imagens/sujeira.png", self.janela, (243, 97, 255), limite_esquerdo, limite_direito, limite_superior, limite_inferior)
        sujeira10 = Sujeira(1*8, 1*8, "imagens/sujeira.png", self.janela, (243, 97, 255), limite_esquerdo, limite_direito, limite_superior, limite_inferior)
        #garda todas as sujeiras num vetor
        self.vetor_sujeiras = [sujeira1, sujeira2, sujeira3, sujeira4, sujeira5, sujeira6, sujeira7, sujeira8, sujeira9, sujeira10]

        cloro1 = Cloro(41 * 8, 22 * 8, 1 * 8, 1 * 8, "imagens/particula_cloro.png", janela, (243, 97, 255))
        cloro2 = Cloro(41 * 8, 22 * 8, 1 * 8, 1 * 8, "imagens/particula_cloro.png", janela, (243, 97, 255))
        cloro3 = Cloro(41 * 8, 22 * 8, 1 * 8, 1 * 8, "imagens/particula_cloro.png", janela, (243, 97, 255))
        cloro4 = Cloro(41 * 8, 22 * 8, 1 * 8, 1 * 8, "imagens/particula_cloro.png", janela, (243, 97, 255))
        cloro5 = Cloro(41 * 8, 22 * 8, 1 * 8, 1 * 8, "imagens/particula_cloro.png", janela, (243, 97, 255))
        cloro6 = Cloro(41 * 8, 22 * 8, 1 * 8, 1 * 8, "imagens/particula_cloro.png", janela, (243, 97, 255))
        cloro7 = Cloro(41 * 8, 22 * 8, 1 * 8, 1 * 8, "imagens/particula_cloro.png", janela, (243, 97, 255))
        cloro8 = Cloro(41 * 8, 22 * 8, 1 * 8, 1 * 8, "imagens/particula_cloro.png", janela, (243, 97, 255))
        cloro9 = Cloro(41 * 8, 22 * 8, 1 * 8, 1 * 8, "imagens/particula_cloro.png", janela, (243, 97, 255))
        cloro10 = Cloro(41 * 8, 22 * 8, 1 * 8, 1 * 8, "imagens/particula_cloro.png", janela, (243, 97, 255))
        #guarda todos os cloros num vetor
        self.vetor_cloros = [cloro1, cloro2, cloro3, cloro4, cloro5, cloro6, cloro7, cloro8, cloro9, cloro10]
        self.funcionamento_cloro = False    #determina se os cloros estão funcionando ainda na agua
        self.redeNeural = RedeNeural()


    def desenha_sujeiras(self):
        for sujeira in self.vetor_sujeiras:
            if sujeira:
                sujeira.desenha()

    def desenha_cloros(self):
        for cloro in self.vetor_cloros:
            if cloro:
                cloro.desenha()

    def move_cloros(self):
        i = 0
        velocidade = 3.5 #multiplicador no movimento do cloro
        for cloro in self.vetor_cloros:
            if cloro and self.vetor_sujeiras[i]:
                mov = self.redeNeural.encontra_direcao(cloro.x, cloro.y, self.vetor_sujeiras[i].x, self.vetor_sujeiras[i].y)
                if abs(cloro.x - self.vetor_sujeiras[i].x) > velocidade or abs(cloro.y - self.vetor_sujeiras[i].y) > velocidade:
                    cloro.x = cloro.x + mov[0] * velocidade
                    cloro.y = cloro.y + mov[1] * velocidade
                else:
                    cloro.x = cloro.x + mov[0]
                    cloro.y = cloro.y + mov[1]

                #apaga os cloros e as sujeiras quando se encontrarem
                if abs(cloro.x - self.vetor_sujeiras[i].x) < 2 and abs(cloro.y - self.vetor_sujeiras[i].y) < 2:
                    self.vetor_cloros[i] = None
                    self.vetor_sujeiras[i] = None

            i+=1

    #retorna true caso algum cloro ainda exista
    def confere_cloros(self):
        i = 0
        for cloro in self.vetor_cloros:
            if cloro:
                i+=1

        return i



    def run(self):

        #recebe todas a teclas pressionadas
        teclas = pygame.key.get_pressed()

        #aplica a opacidade a sujeira
        self.sujeira.setAlpha(self.opacidade)

        if not self.cloro_usado or not self.cal_usado:

            #desenha
            self.background.desenha()
            self.agua.desenha()
            self.tanque.desenha()
            self.canos.desenha()
            self.inventario.desenha()
            self.cloro.desenha()
            self.cal.desenha()

            self.selecionado.desenha()
            if self.cal_usado:
                self.concluido_cal.desenha()
            if self.cloro_usado:
                self.concluido_cloro.desenha()

            self.medidor.desenha()

            #desenha todas as sujeiras
            self.desenha_sujeiras()


            """if not self.cloro_usado:
                self.cloro.desenha()
            if not self.cal_usado:
                self.cal.desenha()"""

            if self.selecionado == self.borda_cal and not self.funcionamento_cloro:

                #permite a animação do indicador do ph ideal
                self.ph_ideal.setVelocidade(0.5)
                self.animacao_cal.setVelocidade(0.5)
                if self.medidor.getY() < 48 * 8:
                    self.ph_ideal.update()
                else:
                    self.cal_usado = True

                if teclas[pygame.K_SPACE] and self.medidor.getY() < 48 * 8:
                    self.animacao_cal.update()
                    if self.animacao_cal.getFrame() > 13:
                        self.animacao_cal.setFrame(8)
                    self.animacao_cal.setX(self.animacao_cal.getX() + 6)
                    self.medidor.setY(self.medidor.getY() + 0.5)
                    self.opacidade = self.opacidade - 0.6
                    print(self.opacidade)
                else:
                    if self.medidor.getY() >= 48 * 8:
                        self.animacao_cal.setRepetir()
                        self.animacao_cal.update()
                        self.opacidade = 100
                        """self.brilho.setVelocidade(10)
                        self.brilho.update()"""
                    if teclas[pygame.K_RIGHT]:
                        self.selecionado = self.borda_cloro
            else:

                #inibe a animação do indicador do ph ideal
                self.ph_ideal.setFrame(0)

                if teclas[pygame.K_SPACE] or self.funcionamento_cloro:
                    self.funcionamento_cloro = True
                    self.desenha_cloros()
                    self.move_cloros()

                if teclas[pygame.K_LEFT] and not self.funcionamento_cloro:
                    self.selecionado = self.borda_cal

                if not self.confere_cloros():
                    self.funcionamento_cloro = False
                    self.cloro_usado = True


            #desenha o filtro da sujeira depois de tudo para que ele afete os cloros tambem
            self.sujeira.desenha()


        #transição
        else:
            self.transicao.desenha()
            if self.transicao.getX() > (-320 * 8) - 1:

                #Verifica se a seta para a direita está sendo pressionada
                if teclas[pygame.K_RIGHT]:
                    self.transicao.setX(self.transicao.getX() - 3)
            else:
                self.proximaFase = fase_3.Fase3(self.janela, self.gerenciador, self.mouse)
                self.gerenciador.set_fase(self.proximaFase)



"""if __name__ == "__fase_2__":  #roda a classe jogo
    jogo = Fase2()
    jogo.run()"""




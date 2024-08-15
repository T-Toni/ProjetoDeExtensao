import pygame
from pygame.locals import *

from sys import exit
import gerenciador_de_fases
import menu
import asteroids
import transicao_3
import fase_4
import fase_5
import transicao_4
import mouse
import transicao_2
import mixer


#Dados relevantes pra inicialização do pygame
LARGURA, ALTURA = 1280, 720
FPS = 60


class Jogo:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.janela = pygame.display.set_mode((LARGURA, ALTURA), SRCALPHA)
        self.clock = pygame.time.Clock()
        self.gerenciador = gerenciador_de_fases.GerenciadorDeFases(None)
        self.faseAtual = None
        self.mouse = mouse.Mouse()

        self.mixer = mixer.Mixer()

        # Muda o nome da janela
        pygame.display.set_caption("Jornada D'água")

        # Carrega o ícone
        icon = pygame.image.load("imagens/ideia_narrador1.png")

        # Define o ícone da janela
        pygame.display.set_icon(icon)


    def rodar(self):

        #inicializa a classe (fase) menu
        self.faseAtual = menu.Menu(self.janela, self.gerenciador, self.mouse, self.mixer)
        #self.faseAtual = asteroids.Asteroids(self.janela, self.gerenciador, self.mouse, self.mixer)
        #self.faseAtual = transicao_4.Transicao_4(self.janela, self.gerenciador, self.mouse, self.mixer)
        #self.faseAtual = fase_4.Fase4(self.janela, self.gerenciador, self.mouse, self.mixer)
        #self.faseAtual = fase_5.Fase5(self.janela, self.gerenciador, self.mouse, self.mixer)
        #self.faseAtual = transicao_3.Transicao_3(self.janela, self.gerenciador, self.mouse, self.mixer)

        self.gerenciador.set_fase(self.faseAtual)                       #a atribui ao gerenciador de fases

        while True:     #loop principal
            #botão de fechar janela
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()

            """#apague
            a = self.mixer.get_volume_sons()
            print("sons: " + str(a))

            b = self.mixer.get_volume_musica()
            print("musica: " + str(b))

            c = self.mixer.get_volume_falas()
            print("falas: " + str(c))"""

            #inicializador e executor de fazes
            self.faseAtual = self.gerenciador.get_fase()                #recebe a fase do gerenciador
            self.faseAtual.run()         #roda a fase do gerenciador

            #atualiza as informações do mouse (x, y e estado do botão esquerdo)
            self.mouse.update()         #guarda corretamente o estado do mouse (deve estar depois da função run da fase)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":  #roda a classe jogo
    jogo = Jogo()
    jogo.rodar()

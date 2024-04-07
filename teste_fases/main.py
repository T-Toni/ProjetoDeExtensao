import pygame
from pygame.locals import *
from sys import exit
import gerenciador_de_fases
import menu
import asteroids
import transicao_1
import fase_3
import mouse
import transicao_2

#Dados relevantes pra inicialização do pygame
LARGURA, ALTURA = 1280, 720
FPS = 60


class Jogo:
    def __init__(self):
        pygame.init()
        self.janela = pygame.display.set_mode((LARGURA, ALTURA))
        self.clock = pygame.time.Clock()
        self.gerenciador = gerenciador_de_fases.GerenciadorDeFases(None)
        self.faseAtual = None
        self.mouse = mouse.Mouse()

    def rodar(self):

        self.faseAtual = menu.Menu(self.janela, self.gerenciador, self.mouse)       #inicializa a classe (fase) menu
        #self.faseAtual = asteroids.Asteroids(self.janela, self.gerenciador, self.mouse)
        #self.faseAtual = transicao_2.Transicao_2(self.janela, self.gerenciador, self.mouse)
        self.gerenciador.set_fase(self.faseAtual)                       #a atribui ao gerenciador de fases

        while True:     #loop principal
            #botão de fechar janela
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()


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

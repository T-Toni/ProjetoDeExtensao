import pygame
from pygame.locals import *

from sys import exit
import gerenciador_de_fases
import menu
import asteroids
import transicao_1
import fase_3
import fase_5
import transicao_4
import mouse
import transicao_2

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

    def carrega_audios(self):
        click = pygame.mixer.Sound('sons/blipSelect.wav')
        cano_errado = pygame.mixer.Sound('sons/cano errado.wav')
        cano_correto = pygame.mixer.Sound('sons/cano_correto.wav')
        cano_movimento = pygame.mixer.Sound('sons/cano_movimento.wav')
        morte_aguda = pygame.mixer.Sound('sons/morte_aguda.wav')
        morte_grave = pygame.mixer.Sound('sons/morte_grave.wav')
        grito_agudo = pygame.mixer.Sound('sons/grito_agudo.wav')
        grito_grave = pygame.mixer.Sound('sons/grito_grave.wav')

        return (click, cano_correto, cano_errado, cano_movimento, morte_grave, morte_aguda, grito_grave, grito_agudo)

    def rodar(self):

        #inicializa a classe (fase) menu
        self.faseAtual = menu.Menu(self.janela, self.gerenciador, self.mouse)
        #self.faseAtual = asteroids.Asteroids(self.janela, self.gerenciador, self.mouse)
        #self.faseAtual = transicao_4.Transicao_4(self.janela, self.gerenciador, self.mouse)
        #self.faseAtual = fase_3.Fase3(self.janela, self.gerenciador, self.mouse)
        #self.faseAtual = fase_5.Fase5(self.janela, self.gerenciador, self.mouse)
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

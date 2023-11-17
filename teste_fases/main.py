import pygame
from pygame.locals import *
from sys import exit
import gerenciador_de_fases
import menu

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

    def rodar(self):

        self.faseAtual = menu.Menu(self.janela, self.gerenciador)       #inicializa a classe (fase) menu
        self.gerenciador.set_fase(self.faseAtual)                       #a atribui ao gerenciador de fases

        BEM_pressionado = False    #Botão Esquerdo do Mouse Pressionado: serve para a logica do clique funcionar corretamente(não ficar clicando a cada iteração)

        while True:     #loop principal

            #botão de fechar janela
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()

            #inicialização e atualização de variaveis relevantes
            mouseX, mouseY = pygame.mouse.get_pos()


            #inicializador e executor de fazes
            self.faseAtual = self.gerenciador.get_fase()                #recebe a fase do gerenciador
            self.faseAtual.run(mouseX, mouseY, BEM_pressionado)         #roda a fase do gerenciador


            if pygame.mouse.get_pressed()[0]:                           #guarda corretamente o estado do mouse (deve estar depois da função run da fase)
                BEM_pressionado = True
            else:
                BEM_pressionado = False

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":  #roda a classe jogo
    jogo = Jogo()
    jogo.rodar()

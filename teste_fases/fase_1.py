import pygame
import menu
from botao import Botao

class Fase1:
    def __init__(self, janela, gerenciador):
        self.janela = janela
        self.gerenciador = gerenciador

        self.botao = Botao(100, 100, 200, 200, "imagens/botao_generico.jpg", self.janela, None)

    def run(self, mouseX, mouseY, pressionado):
        self.janela.fill('red')

        self.botao.desenha()

        if self.botao.clicado(mouseX, mouseY, pressionado):
            proximaFase = menu.Menu(self.janela, self.gerenciador)
            self.gerenciador.set_fase(proximaFase)              #muda a fase do gerenciador para a proxima




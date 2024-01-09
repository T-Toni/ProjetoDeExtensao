import pygame
import menu
from botao import Botao

class Fase1:
    def __init__(self, janela, gerenciador, mouse):
        self.janela = janela
        self.gerenciador = gerenciador
        self.mouse = mouse

        self.botao = Botao(100, 100, 200, 200, "imagens/botao_generico.jpg", self.janela, None)

    def run(self):
        self.janela.fill('red')

        self.botao.desenha()

        if self.botao.clicado(self.mouse.getX(), self.mouse.getY(), self.mouse.getPressionado()):
            proximaFase = menu.Menu(self.janela, self.gerenciador, self.mouse)
            self.gerenciador.set_fase(proximaFase)              #muda a fase do gerenciador para a proxima




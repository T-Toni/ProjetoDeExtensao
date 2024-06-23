import pygame

class Texto:

    def __init__(self, texto1, texto2, texto3, texto4, posicao, tela):
        #inicializa
        self.posicao = posicao
        self.fonte = pygame.font.Font('fontes/minecraft.ttf', 32)
        self.tela = tela

        #inicializa o texto
        branco = (255, 255, 255)
        self.texto1 = self.fonte.render(texto1, 1, branco)
        if texto2:
            self.texto2 = self.fonte.render(texto2, 1, branco)
        else:
            self.texto2 = None
        if texto3:
            self.texto3 = self.fonte.render(texto3, 1, branco)
        else:
            self.texto3 = None
        if texto4:
            self.texto4 = self.fonte.render(texto4, 1, branco)
        else:
            self.texto4 = None

        #carrega a imagem da caixa de diálogo
        self.caixa = pygame.image.load('imagens/caixa_texto.png')  #!!!DEVE SER CARREGADO ASSIM, CASO CONTRARIO SERÁ UMA STRING
        self.caixa = pygame.transform.scale(self.caixa, (160 * 8, 90 * 8))
        self.caixa.set_colorkey((243, 97, 255))  #torna transparente a cor dana no parametro



    def escreve(self):
        #desenha a caixa de diálogo
        self.tela.blit(self.caixa, (0, 0))

        x = 19 * 8
        y = 51 * 8

        distancia = 7*8

        #desenha o primeiro texto
        self.tela.blit(self.texto1, (x, y))

        #desenha os seguintes textos caso eles existam

        if self.texto2:
            self.tela.blit(self.texto2, (x, y + distancia))
        if self.texto3:
            self.tela.blit(self.texto3, (x, y + distancia * 2))
        if self.texto4:
            self.tela.blit(self.texto4, (x, y + distancia * 3))







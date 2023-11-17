import pygame

class ObjAnimado:
    def __init__(self, tela, sheet, largura, altura, escala, cor, velocidade):  #sheet = obj SpriteSheet
        self.tela = tela
        self.sheet = sheet
        self.animacao = False           #variavel que determina se a animação está ou não ocorrendo
        self.spriteAtual = 0            #variavel que determina o frame
        self.largura = largura
        self.altura = altura
        self.escala = escala
        self.cor = cor
        self.imagem = None              #variavel que aguarda o frame atual
        self.velocidade = velocidade    #velocidade da animação
        self.repetir = False            #determina se a animação vai ficar em loop

    #permite a animacao
    def anima(self):
        self.animacao = True

    #atualiza a imagem
    def update(self, x, y):
        if self.animacao == True:
            self.spriteAtual += self.velocidade

            if self.spriteAtual >= self.sheet.numeroDeFrames:   #confere se a animacao chegou ao
                self.spriteAtual = 0
                if self.repetir == False:
                    self.animacao = False           #cancela o looping

            self.imagem = self.sheet.get_image(self.spriteAtual, self.largura, self.altura, self.escala, self.cor)
            self.tela.blit(self.imagem, (x, y))

    #inverte o valor de "repetir" para permitir ou cancelar o loop de animacao
    def loop(self):
        self.repetir = not self.repetir



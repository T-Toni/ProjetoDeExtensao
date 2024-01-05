import pygame

class ObjAnimado:
    def __init__(self, tela, sheet, largura, altura, escala, cor, velocidade):  #sheet = obj SpriteSheet

        #dimensões
        self.largura = largura
        self.altura = altura
        self.escala = escala

        #spritesheet (obj que guarda as imagens da animação)
        self.sheet = sheet

        #demais variaveis
        self.animacao = False           # variavel que determina se a animação está ou não ocorrendo
        self.spriteAtual = 0            # variavel que determina o frame
        self.cor = cor                  # cor a ser excluida da imagem
        self.imagem = None              # variavel que aguarda o frame atual
        self.velocidade = velocidade    # velocidade da animação
        self.repetir = False            # determina se a animação vai ficar em loop

        # necessário para desenhar na tela
        self.tela = tela


    #permite a animacao
    def anima(self):
        self.animacao = True

    #atualiza a imagem
    def update(self, x, y):
        if self.animacao == True:
            self.spriteAtual += self.velocidade

            # confere se a animacao chegou ao fim
            if self.spriteAtual >= self.sheet.numeroDeFrames:
                self.spriteAtual = 0

                # cancela o looping
                if self.repetir == False:
                    self.animacao = False

            self.imagem = self.sheet.get_image(self.spriteAtual, self.largura, self.altura, self.escala, self.cor)
            self.tela.blit(self.imagem, (x, y))

    #inverte o valor de "repetir" para permitir ou cancelar o loop de animacao
    def loop(self):
        self.repetir = not self.repetir



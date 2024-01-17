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

        #coordenadas
        self.x = None
        self.y = None


    #permite a animacao
    def anima(self, x, y):
        self.animacao = True
        self.x = x
        self.y = y

    #atualiza a imagem
    def update(self):
        if self.animacao == True:
            self.spriteAtual += self.velocidade

            # confere se a animacao chegou ao fim
            if self.spriteAtual >= self.sheet.numeroDeFrames:
                self.spriteAtual = 0

                # cancela o looping
                if self.repetir == False:
                    self.animacao = False

            self.imagem = self.sheet.get_image(self.spriteAtual, self.largura, self.altura, self.escala, self.cor)
            self.tela.blit(self.imagem, (self.x, self.y))



    #inverte o valor de "repetir" para permitir ou cancelar o loop de animacao
    def loop(self):
        self.repetir = not self.repetir

    def fim_da_animacao(self):
        # confere se a animacao chegou ao fim
        if self.spriteAtual + 0.1 >= self.sheet.numeroDeFrames:
            return 1
        else:
            return 0

    def setFrame(self, frame):
        self.spriteAtual = frame

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    #função para arrastar
    def update_movimentacao(self, pressionado, mouseX, mouseY):      #pressionado = botão esquerdo do mouse pressionado
        if mouseX > self.x and mouseX < self.x + self.largura * self.escala  and mouseY > self.y and mouseY < self.y + self.altura * self.escala:    #confere se o cursor está dentro do item
            if pressionado:             #confere se clico
                self.x = mouseX - (self.largura * self.escala / 2)
                self.y = mouseY - (self.altura * self.escala  / 2)



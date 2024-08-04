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
        self.sendoSegurado = False      # determina se o objeto está sendo arrastado pelo mouse
        self.reverse = False            # ativada quando inicia-se a animação invertida

        # necessário para desenhar na tela
        self.tela = tela

        #coordenadas
        self.x = None
        self.y = None

        # para fazer uma lista encadeada ser possivel
        self.proximo = None


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

    #remendo porco
    def fim_da_animacao_2(self):
        # confere se a animacao chegou ao fim
        if self.spriteAtual + 0.1 >= self.sheet.numeroDeFrames - 2:
            return 1
        else:
            return 0

    def setFrame(self, frame):
        self.spriteAtual = frame

    def getFrame(self):
        return self.spriteAtual

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    #função para arrastar                                   # se o mouse está segurando algo
    def update_movimentacao(self, pressionado, mouseX, mouseY, mouseSegurandoAlgo):      #pressionado = botão esquerdo do mouse pressionado
        if (mouseX > self.x and mouseX < self.x + self.largura * self.escala  and mouseY > self.y and mouseY < self.y + self.altura * self.escala) or self.sendoSegurado:    #confere se o cursor está dentro do item
            if not mouseSegurandoAlgo or self.sendoSegurado:
                if pressionado:
                    self.x = mouseX - (self.largura * self.escala / 2)
                    self.y = mouseY - (self.altura * self.escala / 2)
                    self.sendoSegurado = True
                else:
                    self.sendoSegurado = False

    #define um loop personalizado
    def altLoop(self, frameInicial, frameFinal, velocidade):
        #zera a velocidade
        if self.velocidade > 0:
            self.velocidade = 0

        # executa o loop
        if self.spriteAtual < frameFinal - 0.1:
            self.spriteAtual += velocidade
        else:
            self.spriteAtual = frameInicial

    #anda por todos os frames as avessas
    def revLoop(self, frameInicial, frameFinal, velocidade):
        # zera a velocidade
        if self.velocidade > 0:
            self.velocidade = 0

        #executa o loop invertido
        if not self.reverse:
            self.spriteAtual = frameFinal
            self.reverse = True
        elif self.spriteAtual > 0:
            self.spriteAtual -= velocidade
        else:
            self.spriteAtual = 0

    def setVelocidade(self, velocidade):
        self.velocidade = velocidade

    def getVelocidade(self):
        return self.velocidade

    def letAnima(self):
        self.animacao = True;

    def setRepetir(self):
        self.repetir = not self.repetir




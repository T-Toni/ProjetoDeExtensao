import pygame

class Item:

    #metodo construtor para itens (contem tamanho fixo)
    def __init__(self, imagem, tela, cor):
        self.x = 0
        self.y = 0
        self.largura = 100
        self.altura = 100
        self.imagem = pygame.image.load(imagem)  #!!!DEVE SER CARREGADO ASSIM, CASO CONTRARIO SERÁ UMA STRING
        self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))
        self.imagem.set_colorkey(cor)  #torna transparente a cor dana no parametro
        self.tela = tela
        self.atingiuOAlvo = False

        self.proximo = None     #para poder fazer uma lista encadeada (assim como em c)

    def desenha(self):
        self.tela.blit(self.imagem, (self.x, self.y))

    def update(self, pressionado, mouseX, mouseY, dentro): #pressionado = botão esquerdo do mouse pressionado

        i = False   #variavel que vai garantir que o alvo so será atingido caso o item seja solto dentro dele

        if mouseX > self.x and mouseX < self.x + self.largura and mouseY > self.y and mouseY < self.y + self.altura:    #confere se o cursor está dentro do item
            if pressionado:     #confere se clicou
                i = True
                self.x = mouseX - (self.largura / 2)
                self.y = mouseY - (self.altura / 2)
            else:
                if dentro and i:
                    self.atingiuOAlvo = True

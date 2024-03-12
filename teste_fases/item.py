import pygame

class Item:

    #metodo construtor para itens (contem tamanho fixo)
    def __init__(self, nome, imagem, tela, cor, mouse):

        #nome do item
        self.nome = nome

        #posições
        self.x = 0
        self.InvX = -1   #guarda sua posição x inicial no inventario
        self.y = 0
        self.InvY = -1   #guarda sua posição y inicial no inventario

        #caracteristicas estéticas
        self.largura = 16 * 8
        self.altura = 16 * 8
        self.imagem = pygame.image.load(imagem)     #!!!DEVE SER CARREGADO ASSIM, CASO CONTRARIO SERÁ UMA STRING
        self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))
        self.imagem.set_colorkey(cor)   #torna transparente a cor dada no parametro

        #variaveis
        self.sendoSegurado = False      #guarda se o item está sendo arrastado pelo mouse
        self.atingiuOAlvo = False
        self.proximo = None             #para poder fazer uma lista encadeada (assim como em c)

        # ferramentas necessarias para o funcionamento
        self.tela = tela        #necessário para desenhar na tela
        self.mouse = mouse      #contem todas as informações do mouse

    def desenha(self):
        if self.InvY == -1 and self.InvX == -1:     #guarda a posição do item no inventário
            self.InvX = self.x
            self.InvY = self.y
        self.tela.blit(self.imagem, (self.x, self.y))

    def update(self, dentro):      #pressionado = botão esquerdo do mouse pressionado

        if self.mouse.getX() > self.x and self.mouse.getX() < self.x + self.largura and self.mouse.getY() > self.y and self.mouse.getY() < self.mouse.getY() + self.altura or self.sendoSegurado:    #confere se o cursor está dentro do item

            if not self.mouse.getItem() or self.sendoSegurado:
                if self.mouse.pressionado:             #confere se clicou
                    i = True
                    self.mouse.setItem(True)
                    self.sendoSegurado = True
                    self.x = self.mouse.getX() - (self.largura / 2)
                    self.y = self.mouse.getY() - (self.altura / 2)
                else:
                    self.mouse.setItem(False)
                    self.sendoSegurado = False
                    if dentro:
                        self.atingiuOAlvo = True
                    else:
                        # confere se o objeto foi movido para retorna-lo para sua posição no inventario
                        if self.x != self.InvX or self.y != self.InvY:
                            self.x = self.InvX
                            self.y = self.InvY


    def atingiuOAlvo(self):
        return self.atingiuOAlvo


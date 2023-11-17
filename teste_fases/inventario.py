import pygame

class Inventario:

    def __init__ (self, tela):
        self.tela = tela
        self.largura = 1080
        self.altura = 100
        self.x = 100
        self.y = 620

        self.numeroDeItens = 0

        self.itens = None
        #self.imagem = pygame.image.load("caminhoDaImagem.png")


    def adicionar_item(self, item):

        #centraliza o objeto relativo ao eixo y (não se altera)
        item.y = self.y + (self.altura / 2) - (item.altura/2)

        if self.itens == None:

            #centraliza o objeto no inventario
            item.x = self.x + (self.largura / (self.numeroDeItens + 2))

            #adiciona o objeto a lista
            self.itens = item
            self.numeroDeItens = self.numeroDeItens + 1             #incrementa o contador


        else:
            i = self.itens

            #roda o laço para encontrar o ultimo item da lista
            while i.proximo != None:
                i = i.proximo

            #adiciona o item na lista
            i.proximo = item
            self.numeroDeItens += 1                                 #incrementa o contador

            #centraliza os objetos no inventario
            distancia = (self.largura / (self.numeroDeItens + 1))   #armazena a distancia entre um objeto e outro

            i = self.itens                                          #reinicializa a variavel i

            #roda o laço para centralizar todos os itens
            numeroDoItem = 1                                        #guarda o numero do item da esquerda para a direita
            while i != None:
                i.x = self.x + (distancia * numeroDoItem)
                numeroDoItem = numeroDoItem + 1
                i = i.proximo

    #remove todos os itens que foram usados (atingiram o alvo)
    def remover_itens(self):
        if self.itens.atingiuOAlvo == True:
            self.itens = self.itens.proximo
            self.numeroDeItens -= 1
        else:
            item_atual = self.itens.proximo
            item_anterior = self.itens

            while item_atual != None:
                if item_atual.atingiuOAlvo == True:
                    item_anterior.proximo = item_atual.proximo
                    item_atual = None
                    self.numeroDeItens -= 1



    def desenha(self):
        #self.tela.blit(self.imagem, (self.x, self.y))
        pygame.draw.rect(self.tela, (30, 30, 30), (self.x, self.y, self.largura, self.altura))

        #desenha todos os itens da lista
        if self.itens.proximo == None:
            self.itens.desenha()
        else:
            i = self.itens
            while i != None:
                i.desenha()
                i = i.proximo







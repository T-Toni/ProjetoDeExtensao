import pygame

class Inventario:

    def __init__ (self, tela):

        #dimensões e coordenadas (fixas)
        self.largura = 1080
        self.altura = 100
        self.x = 100
        self.y = 620

        #demais variaveis
        self.numeroDeItens = 0
        self.itens = None       #vetor que guarda os itens
        #self.imagem = pygame.image.load("caminhoDaImagem.png")

        #necessário para desenhar na tela
        self.tela = tela


    def adicionar_item(self, item):

        #centraliza o objeto relativo ao eixo y (não se altera)
        item.y = self.y + (self.altura / 2) - (item.altura/2)

        if self.itens == None:

            #centraliza o objeto no inventario
            item.x = self.x + (self.largura / (self.numeroDeItens + 2)) - (item.largura / 2)

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
                i.x = self.x + (distancia * numeroDoItem) - (item.largura / 2)
                numeroDoItem = numeroDoItem + 1
                i = i.proximo

    #remove todos os itens que foram usados (atingiram o alvo)
    def remover_itens(self, item):

        #confere se a lista está vazia
        if self.itens == None:
            return

        i = self.itens      #i recebe o primeiro item da lista

        #confere se o primeiro item é o desejado
        if i.nome == item.nome:
            self.itens = self.itens.proximo     #avança na lista encadeada para não perder os demais itens
            del item                            #exclui o item
            return
        else:
            anterior = None     #guarda o item anterior ao i
            while i != None and i.nome != item.nome:
                anterior = i
                i = i.proximo
            if i == None:
                #print("item não encontrado")
                return
            else:
                anterior.proximo = i.proximo        #avança na lista encadeada para não perder os demais itens
                del item                            #exclui o item
        return







    def desenha(self, pressionado, mouseX, mouseY, dentro):

        #self.tela.blit(self.imagem, (self.x, self.y))
        pygame.draw.rect(self.tela, (30, 30, 30), (self.x, self.y, self.largura, self.altura))

        if self.itens != None:
            #desenha todos os itens da lista
            if self.itens.proximo == None:
                self.itens.desenha()
                self.itens.update(pressionado, mouseX, mouseY, dentro)
            else:
                i = self.itens
                while i != None:
                    i.desenha()
                    i.update(pressionado, mouseX, mouseY, dentro)

                    i = i.proximo
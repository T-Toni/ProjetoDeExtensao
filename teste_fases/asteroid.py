import pygame
import random
import math

class Asteroid:

    def __init__(self, x, y):
        self.largura = 16 * 8
        self.altura = 16 * 8

        self.largura_tela = 1280
        self.altura_tela = 720

        if x == None and y == None:
            self.x = random.randint(0 - self.largura*5, 1280 + self.largura*5)
            if self.x <= -self.largura or self.x >= 1280 + self.largura:
                self.y = random.randint(0 - self.altura*5, 720 + self.altura*5)
            else:
                self.y = random.choice([random.randint(0 - self.altura*5, 0 - self.altura), random.randint(720 + self.altura, 720 + self.altura*5)])
        else:
            self.x = x
            self.y = y

        velocidade = 4

        self.direcaox = random.random()*-velocidade
        self.direcaoy = random.random()*velocidade

        self.limite = random.uniform(2, 6)

        """if self.x >= self.largura_tela / 2:
            self.direcaox = random.random()*-velocidade
        else:
            self.direcaox = random.random()*velocidade

        if self.y >= self.altura_tela / 2:
            self.direcaoy = random.random()*-velocidade
        else:
            self.direcaoy = random.random()*velocidade"""

        self.imagem = pygame.image.load("imagens/sujeira_grande.png")
        self.imagem = pygame.transform.scale(self.imagem, (self.largura,self.altura))
        self.imagem.set_colorkey([243, 97, 255])   #torna transparente a cor dana no parametro
        self.rect = self.imagem.get_rect()
        self.mask = pygame.mask.from_surface(self.imagem)

        # variaveis para o bom funcionamento da comunicação entre sujeiras
        self.ultimo_encontro = 0            #guarda ultimo momento de detecção da nave
        #self.nave_rect = nave_rect
        self.maior_valor = 0                #guarda o maior valor de ultimo_encontro de qualquer sujeira que entrar em contato

        #variaveis que guardam as posições da nave com o offset
        self.navex = None
        self.navey = None

        #variaveis para o bom funcionamento do sensor
        self.raio = 16 * 8  #determina o raio do sensor



    def desenha(self, tela, offset, nave_rect):
        #atualiza a posição com o offset
        self.x -= offset.x
        self.y -= offset.y

        #mantem o rect na mesa posição da imagem
        self.rect.x = self.x
        self.rect.y = self.y

        cor = (255, 255, 255)

        # TEXTO
        # define a cor do texto (em RGB)
        cor_texto = (255, 255, 255)

        # define a fonte e o tamanho do texto
        fonte = pygame.font.Font(None, 36)

        # Renderiza o texto
        texto_renderizado = fonte.render(str(self.ultimo_encontro), True, cor_texto)

        # pega o rect do texto renderizado
        texto_rect = texto_renderizado.get_rect()

        # determine a posição do texto
        texto_rect.topleft = (self.x - self.largura / 2, self.y - self.largura / 2)

        # desenha o texto
        tela.blit(texto_renderizado, texto_rect)
        # FIM DO TEXTO

        #atualiza a posição do ultimo registro da nave tambem
        if self.navex:
            self.navex -= offset.x
            self.navey -= offset.y
            pygame.draw.circle(tela, cor, (self.navex + self.raio / 4, self.navey + self.raio / 4), self.raio / 8, 2)
            tela.blit(texto_renderizado, (self.navex + self.raio / 4, self.navey + self.raio / 4))

        #troca a cor para vermelho se o sensor detectar a nave
        if self.sensor(nave_rect):
            cor = (255, 0, 0)

        pygame.draw.circle(tela, cor, (self.x + self.raio/2, self.y + self.raio/2), self.raio, 2)


        #desenha
        tela.blit(self.imagem, (self.x, self.y))



    def sensor(self, nave_rect):
        #determina o centro do circulo
        centro_x = self.x + self.raio/2
        centro_y = self.y + self.raio/2

        #verifica se algum ponto da nave está dentro do circulo, utilizando os quatro cantos do seu retangulo
        for ponto in [(nave_rect.left, nave_rect.top),
                      (nave_rect.right, nave_rect.top),
                      (nave_rect.left, nave_rect.bottom),
                      (nave_rect.right, nave_rect.bottom)]:
            #calcula uma reta a partir de todas as extremidades do retangulo
            distancia = math.sqrt((centro_x - ponto[0]) ** 2 + (centro_y - ponto[1]) ** 2)
            #confere se essa reta é maior que o raio (indicando se está dentro ou não
            if distancia <= self.raio:
                return True

        # Se nenhum ponto estiver dentro do círculo, não há colisão
        return False

    def update(self, nave_rect, timer):
        #acrescenta a direção a sua posição para que ele se mova
        self.x += self.direcaox
        self.y += self.direcaoy

        """print(self.x)
        print(self.y)"""

        #MOVIMENTAÇÃO ESTILO ASTEROIDS
        acrecimoObjeto = 16 * 8 * 2 * 2
        acrecimoComparacao = 16 * 8 * 2 * 2 + 1

        #faz com que a sujeira volte em outro canto da tela
        if self.x > self.largura_tela + acrecimoComparacao:
            self.x -= self.largura_tela + acrecimoObjeto * 2      #esquerda
        elif self.x < 0 - acrecimoComparacao:
            self.x += self.largura_tela + acrecimoObjeto        #direita

        if self.y > self.altura_tela + acrecimoComparacao:
            self.y -= self.altura_tela + acrecimoObjeto * 2       #cima
        elif self.y < 0 - acrecimoComparacao:
            self.y += self.altura_tela + acrecimoObjeto         #baixo

        #funcionamento do sensor
        self.movimentacao(nave_rect, timer)

        #funcionamento do movimento por propagação
        self.contato = False


    def movimentacao(self, nave_rect, timer):

        if self.sensor(nave_rect):

            self.navex = nave_rect.center[0] - 7*4
            self.navey = nave_rect.center[1] - 5*4

            #atualiza o maior valor
            self.maior_valor = timer
            self.ultimo_encontro = timer
            #mudar para o rect

        if self.navex != None:
            #determina a velocidade da alteração do trajeto
            velocidade = 0.2

            #ajusta a movimentação para o eixo x
            if self.x < self.navex:
                    self.direcaox -= velocidade
            else:
                    self.direcaox += velocidade

            #ajusta a movimentação para o eixo x
            if self.y < self.navey:
                    self.direcaoy -= velocidade
            else:
                    self.direcaoy += velocidade

            #ajusta as velocidades para estarem dentro do limite
            if abs(self.direcaox) > self.limite:
                if self.direcaox > 0:
                    self.direcaox = self.limite
                else:
                    self.direcaox = -self.limite

            if abs(self.direcaoy) > self.limite:
                if self.direcaoy > 0:
                    self.direcaoy = self.limite
                else:
                    self.direcaoy = -self.limite


    """def movimento_propagacao(self):

        # determina a velocidade da alteração do trajeto
        velocidade = 0.1
        #determina um limite de velocidade menor do que o contato com a nave de fato
        limite = self.limite

        # ajusta a movimentação para o eixo x
        if self.x < self.navex:
            self.direcaox -= velocidade
        else:
            self.direcaox += velocidade

        # ajusta a movimentação para o eixo x
        if self.y < self.navey:
            self.direcaoy -= velocidade
        else:
            self.direcaoy += velocidade

        # ajusta as velocidades para estarem dentro do limite
        if abs(self.direcaox) > limite:
            if self.direcaox > 0:
                self.direcaox = limite
            else:
                self.direcaox = -limite

        if abs(self.direcaoy) > limite:
            if self.direcaoy > 0:
                self.direcaoy = limite
            else:
                self.direcaoy = -limite"""





class Particula:

    def __init__(self):

        self.largura = 8
        self.altura = 8

        self.largura_tela = 1280
        self.altura_tela = 720

        acrecimoObjeto = 16 * 8 * 2 * 2
        acrecimoComparacao = 16 * 8 * 2 * 2 + 1

        self.x = random.randint(0 - acrecimoObjeto, self.largura_tela + acrecimoObjeto)
        self.y = random.randint(0 - acrecimoObjeto, self.altura_tela + acrecimoObjeto)

        self.imagem = pygame.image.load("imagens/particula_cloro.png")
        self.imagem = pygame.transform.scale(self.imagem, (self.largura,self.altura))
        self.imagem.set_colorkey([243, 97, 255])


    def desenha(self, tela, offset):
        #atualiza a posição com o offset
        self.x -= offset.x
        self.y -= offset.y

        #desenha
        tela.blit(self.imagem, (self.x, self.y))

        acrecimoObjeto = 16 * 8 * 2 * 2
        acrecimoComparacao = 16 * 8 * 2 * 2 + 1

        #faz com que a sujeira volte em outro canto da tela
        if self.x > self.largura_tela + acrecimoComparacao:
            self.x -= self.largura_tela + acrecimoObjeto * 2      #esquerda
        elif self.x < 0 - acrecimoComparacao:
            self.x += self.largura_tela + acrecimoObjeto        #direita

        if self.y > self.altura_tela + acrecimoComparacao:
            self.y -= self.altura_tela + acrecimoObjeto * 2       #cima
        elif self.y < 0 - acrecimoComparacao:
            self.y += self.altura_tela + acrecimoObjeto         #baixo

import pygame

class SpriteSheet():
    def __init__(self, imagem, numeroDeFrames):
        self.sheet = imagem
        self.numeroDeFrames = numeroDeFrames

    #frame = numero que seleciona o frame do spritesheet
    def get_image(self, frame, largura, altura, escala, cor):
        imagem = pygame.Surface((largura, altura)).convert_alpha()
        imagem.blit((self.sheet), (0, 0), ((int(frame) * largura), 0, largura, altura))
        imagem = pygame.transform.scale(imagem, (largura * escala, altura * escala))
        imagem.set_colorkey(cor)
        return imagem


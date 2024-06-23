import pygame

class Mixer:
    def __init__(self):
        self.sons = {}
        self.falas = {}
        self.musicas = {}

        self.adicionaSons()
        self.adicionaFalas()

        self.mixer_falas = pygame.mixer.Channel(0)


    def adicionaSons(self):
        self.sons['click'] = pygame.mixer.Sound('sons/blipSelect.wav')
        self.sons['cano_errado'] = pygame.mixer.Sound('sons/cano errado.wav')
        self.sons['cano_certo'] = pygame.mixer.Sound('sons/cano_correto.wav')
        self.sons['movimento_cano'] = pygame.mixer.Sound('sons/cano_movimento.wav')
        self.sons['morte_grave'] = pygame.mixer.Sound('sons/morte_grave.wav')
        self.sons['morte_aguda'] = pygame.mixer.Sound('sons/morte_aguda.wav')
        self.sons['grito_grave'] = pygame.mixer.Sound('sons/grito_grave.wav')
        self.sons['grito_agudo'] = pygame.mixer.Sound('sons/grito_agudo.wav')
        self.sons['bolhas1'] = pygame.mixer.Sound('sons/bolha1.ogg')
        self.sons['use_o_cal_primeiro'] = pygame.mixer.Sound('sons/use_o_cal_primeiro.mp3')

    def adicionaFalas(self):

        self.falas['introducao'] = pygame.mixer.Sound('narracao/introducao.wav')
        self.falas['pos_pressionamento'] = pygame.mixer.Sound('narracao/pos_pressionamento_fase1.wav')


    def toca_som(self, som):
        if som in self.sons:
            self.sons[som].play()
        else:
            print("audio não encontrado")

    def toca_fala(self, fala):
        if fala in self.falas:
            self.mixer_falas.play(self.falas[fala])
        else:
            print("audio não encontrado2")

    def tocando_falas(self):
        return self.mixer_falas.get_busy()

    def para_fala(self):
        if self.mixer_falas.get_busy():
            self.mixer_falas.stop()

    #função que faz qualquer fala tocada parar com o pressionamento de enter esquerdo
    def update(self, teclas):
        if teclas[pygame.K_KP_ENTER] and self.mixer_falas.get_busy():
            self.mixer_falas.stop()





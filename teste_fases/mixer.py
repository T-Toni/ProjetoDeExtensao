import pygame

class Mixer:
    def __init__(self):
        self.sons = {}
        self.falas = {}
        self.musicas = {}
        #lista de sons sendo tocados
        self.tocando_agora = {}

        self.adicionaSons()
        self.adicionaFalas()

        self.mixer_falas = pygame.mixer.Channel(0)

        #variável que permite que o jogador pule um dialogo por vez
        self.pulou = False


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

    def adicionaFalas(self):

        #genericos
        self.falas['erro_transicao'] = pygame.mixer.Sound('narracao/erro_transicoes.wav')
        self.falas['acerto_transicao'] = pygame.mixer.Sound('narracao/acerto_transicoes.wav')

        #fase1
        self.falas['introducao1.1'] = pygame.mixer.Sound('narracao/introducao1.wav')
        self.falas['introducao1.2'] = pygame.mixer.Sound('narracao/introducao2.wav')
        self.falas['introducao1.3'] = pygame.mixer.Sound('narracao/introducao3.wav')
        self.falas['pos_pressionamento'] = pygame.mixer.Sound('narracao/pos_pressionamento.wav')

        #transicao1
        self.falas['transicao1'] = pygame.mixer.Sound('narracao/trans1_intro.wav')

        #fase2
        self.falas['introducao2.1'] = pygame.mixer.Sound('narracao/introducao2.1.wav')
        self.falas['introducao2.2'] = pygame.mixer.Sound('narracao/introducao2.2.wav')
        self.falas['pos_cal_fase2'] = pygame.mixer.Sound('narracao/pos_cal_fase2.wav')
        self.falas['intro_cloro_fase2'] = pygame.mixer.Sound('narracao/intro_cloro_fase2.wav')
        self.falas['fim_fase2'] = pygame.mixer.Sound('narracao/fim_fase2.wav')
        self.falas['use_o_cal_primeiro'] = pygame.mixer.Sound('narracao/use_o_cal_primeiro.wav')

        #demais transições
        self.falas['intro_transicoes'] = pygame.mixer.Sound('narracao/intro_transicoes.wav')

        #fase3
        self.falas['introducao3.1'] = pygame.mixer.Sound('narracao/introducao3.1.wav')
        self.falas['introducao3.2'] = pygame.mixer.Sound('narracao/introducao3.2.wav')
        self.falas['fim_fase3'] = pygame.mixer.Sound('narracao/fim_fase3.wav')

        #fase4
        self.falas['introducao4.1'] = pygame.mixer.Sound('narracao/introducao4.1.wav')
        self.falas['introducao4.2'] = pygame.mixer.Sound('narracao/introducao4.2.wav')
        self.falas['fim_fase4.1'] = pygame.mixer.Sound('narracao/fim_fase4.1.wav')
        self.falas['fim_fase4.2'] = pygame.mixer.Sound('narracao/fim_fase4.2.wav')

        #fase5
        self.falas['introducao5.1'] = pygame.mixer.Sound('narracao/introducao5.1.wav')
        self.falas['introducao5.2'] = pygame.mixer.Sound('narracao/introducao5.2.wav')
        #self.falas['pos_cal_fase2'] = pygame.mixer.Sound('narracao/pos_cal_fase2.wav')
        self.falas['intro_cloro_fase5'] = pygame.mixer.Sound('narracao/intro_cloro_fase5.wav')
        self.falas['fim_fase5'] = pygame.mixer.Sound('narracao/fim_fase5.wav')
        #self.falas['use_o_cal_primeiro'] = pygame.mixer.Sound('narracao/use_o_cal_primeiro.wav')

    def toca_som(self, som):
        if som in self.sons:
            self.sons[som].play()
        else:
            print("audio não encontrado")

    def toca_fala(self, fala):
        if fala in self.falas:
            self.mixer_falas.play(self.falas[fala])
            self.tocando_agora[0] = fala
        else:
            print("audio não encontrado2")

    def tocando_falas(self):
        return self.mixer_falas.get_busy()

    def para_fala(self):
        if self.mixer_falas.get_busy():
            self.mixer_falas.stop()

    #função que faz qualquer fala tocada parar com o pressionamento de enter esquerdo
    def update(self, teclas):
        if teclas[pygame.K_KP_ENTER]:
            if not self.pulou and self.mixer_falas.get_busy():
                self.mixer_falas.stop()
            self.pulou = True
        else:
            self.pulou = False

        #LIMPA O DICIONARIO "tocando agora"
        if not self.mixer_falas.get_busy():
            self.tocando_agora[0] = None

    #OBS: canal está ai para facilitar a modificação caso seja necessário o controle dos sons de das musicas alem das falas
    def get_audio_atual(self, canal):
        return self.tocando_agora[canal]







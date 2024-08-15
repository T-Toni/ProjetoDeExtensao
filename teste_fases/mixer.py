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
        self.adicionaMusicas()

        #variavel para manipular as musicas
        self.musica = 0

        self.mixer_falas = pygame.mixer.Channel(0)
        self.mixer_sons = pygame.mixer.Channel(1)
        self.mixer_musica = pygame.mixer.Channel(2)

        self.mixer_falas.set_volume(0.5)
        self.mixer_sons.set_volume(0.3)
        self.mixer_musica.set_volume(0.4)

        #variável que permite que o jogador pule um dialogo por vez
        self.pulou = False

        #variável que decide qual musica deve ser tocada
        self.acao = False


    def set_volume_falas(self, volume):  #valores validos de 0 - 1
        valor = self.arredonda(volume)
        self.mixer_falas.set_volume(valor)

    def get_volume_falas(self):
        return self.arredonda(self.mixer_falas.get_volume())


    def set_volume_sons(self, volume):  # valores validos de 0 - 1
        valor = self.arredonda(volume)
        #print(valor)
        self.mixer_sons.set_volume(valor)
        #print(self.mixer_sons.get_volume())

    def get_volume_sons(self):
        return self.arredonda(self.mixer_sons.get_volume())


    def set_volume_musica(self, volume):  # valores validos de 0 - 1
        valor = self.arredonda(volume)
        self.mixer_musica.set_volume(valor)

    def get_volume_musica(self):
        return self.arredonda(self.mixer_musica.get_volume())

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

        self.falas['reservatorio'] = pygame.mixer.Sound('narracao/reservatorio.wav')
        self.falas['conclusao'] = pygame.mixer.Sound('narracao/conclusao.wav')


    def adicionaMusicas(self):
        self.musicas['musica1'] = pygame.mixer.Sound('musicas/trilha_1.wav')
        self.musicas['musica2'] = pygame.mixer.Sound('musicas/trilha_2.wav')

    def toca_som(self, som):
        if som in self.sons:
            self.mixer_sons.play((self.sons[som]))
            self.tocando_agora[1] = som
        else:
            pass
            #print("audio não encontrado")

    def toca_fala(self, fala):
        if fala in self.falas:
            self.mixer_falas.play(self.falas[fala])
            self.tocando_agora[0] = fala
        else:
            pass
            #print("audio não encontrado2")

    def tocando_falas(self):
        return self.mixer_falas.get_busy()

    def para_fala(self):
        if self.mixer_falas.get_busy():
            self.mixer_falas.stop()

    def para_sons(self):
        if self.mixer_sons.get_busy():
            self.mixer_sons.stop()

    #função que faz qualquer fala tocada parar com o pressionamento de enter esquerdo
    def update(self, teclas):

        if teclas:
            if teclas[pygame.K_KP_ENTER]:
                if not self.pulou and self.mixer_falas.get_busy():
                    self.mixer_falas.stop()
                self.pulou = True
            else:
                self.pulou = False

        #faz com que a musica se repita
        if not self.acao:
            if not self.mixer_musica.get_busy() or self.tocando_agora[2] == 'musica2':
                self.mixer_musica.play(self.musicas['musica1'])
                self.tocando_agora[2] = 'musica1'
        else:
            if self.tocando_agora[2] == 'musica1' or not self.mixer_musica.get_busy():
                self.mixer_musica.play(self.musicas['musica2'])
                self.tocando_agora[2] = 'musica2'


        #LIMPA O DICIONARIO "tocando agora"
        if not self.mixer_falas.get_busy():
            self.tocando_agora[0] = None

    #OBS: canal está ai para facilitar a modificação caso seja necessário o controle dos sons de das musicas alem das falas
    def get_audio_atual(self, canal):
        return self.tocando_agora[canal]


    #para garantir a manipulação correta dos volumes
    def arredonda(self, volume):
        return round(volume * 10) / 10

    def toca_musica(self, musica):
        if musica == 1 and not self.mixer_musica.get_busy():
            self.mixer_musica.play(self.musicas['musica1'])
        elif musica == 0:
            self.mixer_musica.stop()







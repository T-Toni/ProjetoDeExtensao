class GerenciadorDeFases:
    def __init__(self, faseAtual):
        self.faseAtual = faseAtual

    def get_fase(self):
        return self.faseAtual

    def set_fase(self, novaFase):
        self.faseAtual = novaFase

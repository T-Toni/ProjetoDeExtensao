class GerenciadorDeFases:
    def __init__(self, faseAtual):
        self.faseAtual = faseAtual
        self.fase_congelada = None

    def get_fase(self):
        return self.faseAtual

    def set_fase(self, novaFase):
        self.faseAtual = novaFase

    def guarda_fase(self, fase):
        self.fase_congelada = fase


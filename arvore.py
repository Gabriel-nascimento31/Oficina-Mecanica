class No_arvore:
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []

    def adicionar_filho(self, filho_no):
        self.filhos.append(filho_no)
        
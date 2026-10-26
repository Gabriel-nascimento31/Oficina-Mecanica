class No_fila:
    def __init__(self, dado, ponteiro=None, proximo=None):
        self.dado = dado
        self.ponteiro = ponteiro
        self.proximo = proximo

class Fila:
    def __init__(self, inicio=None, fim=None):
        self.inicio = inicio
        self.fim = fim
        self.tamanho = 0

    def enfileirar(self, dado):
        novo_no = No_fila(dado)
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = self.inicio
        else:
            novo_no.proximo = self.fim
            self.fim.ponteiro = novo_no
            self.fim = novo_no
        self.tamanho += 1

    def desenfileirar(self):
        atual = self.inicio
        if self.tamanho == 1:
            self.tamanho -= 1
            self.inicio = None
            self.fim = None
        elif self.tamanho > 1:
            self.inicio = self.inicio.ponteiro
            self.inicio.proximo = None
            self.tamanho -= 1
        return atual

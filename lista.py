class No_lista:
    def __init__(self, dado=None, ponteiro=None):
        self.dado = dado
        self.ponteiro = ponteiro

class Lista:
    def __init__(self, inicio=None, fim=None):
        self.inicio = inicio
        self.fim = fim
        self.tamanho = 0
    
    def adicionar(self, dado):
        novo_no = No_lista()
        if self.fim:
            self.fim.ponteiro = novo_no
            self.fim = novo_no
        else:
            self.inicio = novo_no
            self.fim = novo_no
        self.tamanho += 1

    def deletar(self, dado):
        atual = self.inicio
        anterior = None
        while atual:
            if atual.dado == dado:
                if anterior is None:
                    self.inicio = atual.ponteiro
                    if self.inicio is None:
                        self.fim = None
                else:
                    anterior.ponteiro = atual.ponteiro
                    if atual == self.fim:
                        self.fim = anterior
                self.tamanho -= 1
                return True
            anterior = atual
            atual = atual.ponteiro
        return False

    def esvaziar_lista(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        





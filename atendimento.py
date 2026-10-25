from fila import Fila

class Atendimento:
    def __init__(self, placa, cliente, data_chegada, queixa_relatada):
        self.placa = placa
        self.cliente = cliente
        self.data_chegada = data_chegada
        self.queixa_relatada = queixa_relatada

fila_normal = Fila()
fila_prioritaria = Fila()

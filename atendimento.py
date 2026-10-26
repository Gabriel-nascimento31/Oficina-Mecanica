from fila import Fila
from datetime import datetime

class Atendimento:
    def __init__(self, placa=str, cliente=str, data_chegada=datetime.now, queixa_relatada=str):
        self.placa = placa
        self.cliente = cliente
        self.data_chegada = data_chegada
        self.queixa_relatada = queixa_relatada

atendimento1 = Atendimento('jwxlm', 'ricardo', 'problema no motor') 
atendimento2 = Atendimento('ABC1D23', 'Ana Silva', 'vazamento de óleo no motor')
atendimento3 = Atendimento('KJD4912', 'Carlos Oliveira', 'pedal do freio muito baixo')
atendimento4 = Atendimento('MNO9F87', 'Mariana Costa', 'ar-condicionado não gela')
atendimento5 = Atendimento('XYZ3E45', 'Roberto Souza', 'luz da injeção acesa no painel')
atendimento6 = Atendimento('QWE7890', 'Juliana Lima', 'bateria descarregando do nada')
atendimento7 = Atendimento('PLM2G34', 'Bruno Santos', 'farol esquerdo não acende')
atendimento8 = Atendimento('RTV5H67', 'Fernanda Ribeiro', 'carro puxando para a direita')
atendimento9 = Atendimento('JIW0192', 'Diego Almeida', 'barulho de estalo ao esterçar o volante')



fila_normal = Fila()
fila_prioritaria = Fila()

fila_normal.enfileirar(atendimento1)
fila_normal.enfileirar(atendimento2)
fila_normal.enfileirar(atendimento3)
fila_normal.enfileirar(atendimento4)
fila_normal.enfileirar(atendimento5)
fila_normal.enfileirar(atendimento6)
fila_prioritaria.enfileirar(atendimento7)
fila_prioritaria.enfileirar(atendimento8)
fila_prioritaria.enfileirar(atendimento9)

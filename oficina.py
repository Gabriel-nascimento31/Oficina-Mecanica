from fila import Fila
from lista import Lista
from atendimento import fila_normal, fila_prioritaria, Atendimento
from estoque import estoque
from ordem_de_servico import Ordem_servico
from cliente import clientes
from pagamento import Pagamento
from veiculo import Veiculo
from datetime import datetime

def chegada_veiculo():
    placa = input('Digite a placa do veículo: ')
    cliente = input('Digite o nome do cliente: ')
    queixa = input('Qual a queixa relatada pelo cliente: ')
    data_chegada = datetime.now()
    
    automovel = Atendimento(placa, cliente, data_chegada, queixa)
    guincho = input('O veículo veio guinchado?').strip().lower()
    if guincho == 'sim':
        fila_prioritaria.enfileirar(automovel)
        print('veículo adicionado na fila de atendimento prioritária!')
    elif guincho == 'não':
        fila_normal.enfileirar(automovel)
        print('veículo adicionado na fila de atendimento normal!')
    else:
        print('Opção inválida! Digite sim ou não!')

numero_os = 0
def abrir_ordem_servico():
    global numero_os
    numero_os += 1
    placa = input('Digite a placa do veículo: ')
    cliente = input('Digite o nome do cliente: ')
    mecanico = input('Digite o nome do mecânico responsável pela ordem: ')
    data_abertura = datetime.now()
    pecas_utilizadas = list(input('Digite as peças utiilizadas no concerto do veículo: '))
    servicos_utilizados = list(input('Digite os serviços realizados no concerto do veículo: '))

    nova_os = Ordem_servico(numero_os, placa, cliente, mecanico, data_abertura, pecas_utilizadas, servicos_utilizados)
    
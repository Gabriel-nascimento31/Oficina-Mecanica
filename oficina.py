from fila import Fila
from lista import Lista
from atendimento import fila_normal, fila_prioritaria, Atendimento
from estoque import estoque
from ordem_de_servico import Ordem_servico
from cliente import clientes
from pagamento import Pagamento
from veiculo import Veiculo
from datetime import datetime
from arvore import veiculo
from random import choice 

ordem_servicos_abertas = Lista()
pagamentos_realizados = Lista()

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
    atendimento_atual = None
    if fila_prioritaria.tamanho > 0:
        atendimento_atual = fila_prioritaria.desenfileirar()
        print('Atendendo veículo da fila prioritária (guincho)')
    elif fila_normal.tamanho > 0:
        atendimento_atual = fila_normal.desenfileirar()
        print('Atendendo veículo da fila normal')
    else:
        print('Não há veículos aguardando na fila de atendimento ')
        return

    veiculo_atendido = atendimento_atual.dado
    
    numero_os += 1
    placa = input('Digite a placa do veículo: ')
    cliente = input('Digite o nome do cliente: ')
    mecanico = input('Digite o nome do mecânico responsável pela ordem: ')
    data_abertura = datetime.now()
    pecas_utilizadas = input('Digite as peças utiilizadas no concerto do veículo: ')
    servicos_utilizados = input('Digite os serviços realizados no concerto do veículo: ')

    nova_os = Ordem_servico(numero_os, placa, cliente, mecanico, data_abertura, pecas_utilizadas, servicos_utilizados)
    print(f'Ordem de serviço {numero_os} aberta para o veículo {veiculo_atendido.placa}')
    ordem_servicos_abertas.adicionar(nova_os) 

def realizar_diagnostico():
    print('Realizando diagnóstico do veículo! ')
    veiculo.realizar_diagnostico_recursivo()
    print(veiculo)

def fechar_ordem_servico():
    numero = int(input('Digite o número da ordem para encerrá-la:'))
    ordem_servicos_abertas.deletar(numero)
    print('Ordem de serviço encerrada! ')

def realizar_pagamento():
    pagamento = Pagamento()
    cliente = input('Digite o nome do cliente: ')
    valor_pecas = float(input('Digite o valor das peças utilizadas na manutenção do veículo: '))
    valor_mao_obra = float(input('Digite o valor da mão de obra que foi utilizada no trabalho: '))
    valor_total = valor_pecas + valor_mao_obra
    print(f'O valor total ficou R${valor_total:.2f}')

    forma = input('Digite a forma de pagamento (PIX, Dinheiro ou Cartão)').lower
    if forma == 'PIX' or 'Dinheiro' or 'Cartão':
        pagamentos_realizados.adicionar(pagamento)
        print('Pagamento concluído com sucesso! ')
    else:
        print('Entrada Inválida! Digite uma das opções das formas de pagamento! ')

def adicionar_itens_estoque():
    item = input('Digite o nome do item que deseja adicionar ao estoque: ')
    codigo = input('Digite o código do item: ')
    fornecedor = input('Digite o nome do fornecedor: ')
    preco_compra = float(input('Digite o preço da compra do item: '))
    preco_venda = float(input('Digite o preço da venda do item: '))
    data_compra = datetime.now()
    data_validade = input('Digite a data de validade do item: ')
    quantidade = int(input('Digite a quantidade que deseja adicionar ao estoque: '))
    
    estoque.enfileirar(item)
    print(f'{item} adicionado ao estoque! ')

def remover_itens_estoque():
    item = input('Digite o nome do item que deseja dar baixa no estoque: ')
    estoque.desenfileirar()
    print(f'{item} dado baixa no estoque! ')

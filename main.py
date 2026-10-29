import oficina

while True:
    print('Oficina Mecânica ')
    print('1 - Inserir veículo para atendimento')
    print('2 - Abrir ordem de serviço')
    print('3 - Realizar o diagnóstico da queixa')
    print('4 - Fechar a ordem de serviço')
    print('5 - Realizar o pagamento')
    print('6 - Adicionar itens ao estoque')
    print('7 - Remover itens do estoque')
    print('8 - Encerrar o sistema')

    usuario = int(input('Digite a opção que deseja realizar: '))

    if usuario == 1:
        oficina.chegada_veiculo()
    
    elif usuario == 2:
        oficina.abrir_ordem_servico()
    
    elif usuario == 3:
        oficina.realizar_diagnostico()
    
    elif usuario == 4:
        oficina.fechar_ordem_servico()
    
    elif usuario == 5:
        oficina.realizar_pagamento()
    
    elif usuario == 6:
        oficina.adicionar_itens_estoque()
    
    elif usuario == 7:
        oficina.remover_itens_estoque()
    
    elif usuario == 8:
        print('Sistema encerrado! ')
        break
    
    else:
        print('Opção inválida! ')

class No_arvore:
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []

    def adicionar_filho(self, filho_no):
        self.filhos.append(filho_no)

    def __str__(self, nivel=0):
        resultado = " " * nivel + f"-{self.dado}\n"
        for filho in self.filhos:
            resultado += filho.__str__(nivel + 1)
        return resultado





veiculo = No_arvore("VEÍCULO (Automóvel)")


motor = No_arvore(" 1. Motor e Combustão")
bloco = No_arvore("Bloco do Motor")
for item in ["Cilindros", "Pistões", "Bielas", "Virabrequim"]:
    bloco.adicionar_filho(No_arvore(item))

cabecote = No_arvore("Cabeçote")
for item in ["Válvulas (Admissão / Escape)", "Comando de Válvulas", "Velas de Ignição"]:
    cabecote.adicionar_filho(No_arvore(item))

alimentacao = No_arvore("Alimentação de Combustível")
for item in ["Tanque", "Bomba de Combustível", "Filtro", "Bicos Injetores"]:
    alimentacao.adicionar_filho(No_arvore(item))

motor.adicionar_filho(bloco)
motor.adicionar_filho(cabecote)
motor.adicionar_filho(alimentacao)
veiculo.adicionar_filho(motor)


transmissao = No_arvore(" 2. Transmissão e Força")
for item in ["Embreagem (ou Conversor de Torque)", "Caixa de Câmbio (Marchas)", "Eixo Cardã / Semieixos (Homocinéticas)", "Diferencial"]:
    transmissao.adicionar_filho(No_arvore(item))
veiculo.adicionar_filho(transmissao)


freios = No_arvore(" 3. Sistema de Freios")
for item in ["Cilindro Mestre e Servofreio", "Freio Dianteiro (Discos e Pastilhas)", "Freio Traseiro (Tambores e Lonas)", "Freio de Mão (Estacionamento)"]:
    freios.adicionar_filho(No_arvore(item))
veiculo.adicionar_filho(freios)


susp_dir = No_arvore(" 4. Suspensão e Direção")
suspensao = No_arvore("Suspensão")
for item in ["Amortecedores", "Molas", "Barra Estabilizadora"]:
    suspensao.adicionar_filho(No_arvore(item))

direcao = No_arvore("Direção")
for item in ["Volante", "Caixa de Direção", "Terminais de Direção"]:
    direcao.adicionar_filho(No_arvore(item))

susp_dir.adicionar_filho(suspensao)
susp_dir.adicionar_filho(direcao)
veiculo.adicionar_filho(susp_dir)


eletrico = No_arvore(" 5. Sistema Elétrico e Eletrônico")
for item in ["Bateria", "Alternador", "Motor de Partida (Arranque)", "Central Eletrônica (ECU)"]:
    eletrico.adicionar_filho(No_arvore(item))
veiculo.adicionar_filho(eletrico)


arr_ex = No_arvore(" 6. Arrefecimento e Exaustão")
arrefecimento = No_arvore("Arrefecimento")
for item in ["Radiador", "Bomba d'Água", "Válvula Termostática", "Ventoinha"]:
    arrefecimento.adicionar_filho(No_arvore(item))

escapamento = No_arvore("Escapamento")
for item in ["Coletor de Escape", "Catalisador", "Silenciador"]:
    escapamento.adicionar_filho(No_arvore(item))

arr_ex.adicionar_filho(arrefecimento)
arr_ex.adicionar_filho(escapamento)
veiculo.adicionar_filho(arr_ex)


carroceria = No_arvore(" 7. Carroceria e Estrutura")
for item in ["Chassi / Monobloco", "Painéis Externos (Portas, Capô, Para-lamas)", "Vidros (Para-brisa, Laterais)", "Interior (Bancos, Painel, Pedais)"]:
    carroceria.adicionar_filho(No_arvore(item))
veiculo.adicionar_filho(carroceria)



print(veiculo)





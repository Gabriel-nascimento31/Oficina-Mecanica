from datetime import datetime
class Pagamento:
    def __init__(self, nome=str, numero_os=int, forma=str, valor_peças=float, valor_mao_obra=float, valor_total=float, data_pagamento=datetime.now()):
        self.nome = nome
        self.numero_os = numero_os
        self.forma = forma
        self.valor_peças = valor_peças
        self.valor_mao_obra = valor_mao_obra
        self.valor_total = valor_total
        self.data_pagamento = data_pagamento
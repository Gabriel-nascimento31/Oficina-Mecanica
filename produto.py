class Produto:
    def __init__(self, nome, codigo, fornecedor, preco_compra, preco_venda, data_compra, data_validade, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.fornecedor = fornecedor
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_validade = data_validade
        self.quantidade = quantidade

peça = Produto
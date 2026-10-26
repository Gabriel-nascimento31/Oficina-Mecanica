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

peça1 = Produto('parafuso', '1234', 'peças do joão', 2.50, 3.00, '09/10/2026', '20/12/2028', 500)
peça2 = Produto('pastilha de freio', '1020', 'autopeças paulista', 45.00, 89.90, '26/10/2026', '26/10/2031', 40)
peça3 = Produto('filtro de óleo', '3040', 'distribuidora lubrifika', 12.50, 28.00, '20/10/2026', '20/10/2028', 120)
peça4 = Produto('vela de ignição', '5060', 'velas ngk do brasil', 15.00, 32.50, '15/10/2026', '15/10/2031', 200)
peça5 = Produto('correia dentada', '7080', 'central de componentes', 35.20, 75.00, '18/10/2026', '18/10/2030', 35)
peça6 = Produto('amortecedor dianteiro', '9010', 'monroe distribuidora', 120.00, 249.90, '05/10/2026', '05/10/2032', 15)
peça7 = Produto('bomba de combustível', '1122', 'autopeças paulista', 85.00, 169.90, '26/10/2026', '26/10/2031', 25)
peça8 = Produto('disco de freio', '3344', 'metalúrgica fremax', 70.00, 145.00, '22/10/2026', '22/10/2032', 30)
peça9 = Produto('filtro de ar', '5566', 'distribuidora lubrifika', 9.80, 22.00, '20/10/2026', '20/10/2029', 80)
peça10 = Produto('bateria 60ah', '7788', 'baterias moura oficial', 190.00, 349.90, '10/10/2026', '10/10/2028', 12)
peça11 = Produto('junta do cabeçote', '9900', 'central de componentes', 28.50, 65.00, '18/10/2026', '18/10/2031', 45)
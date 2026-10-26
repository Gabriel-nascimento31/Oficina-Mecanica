from lista import Lista

class Cliente:
    def __init__(self, nome, cpf, telefone, veiculos_cadastrados):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.veiculos_cadastrados = []
    

clientes = Lista()
cliente1 = Cliente('Ronaldo', '012345678', '1935561678', [{'placa':'abc', 'modelo':'Corsa', 'marca':'Jaguar', 'ano':1990}])
cliente2 = Cliente('Melissa', '12345', '1950331428', [{'placa':'jbc', 'modelo':'palio', 'marca':'fiat', 'ano': 1991}])
cliente3 = Cliente('Mariana Silva', '456123789', '11999998888', [{'placa': 'ABC1D23', 'modelo': 'Uno', 'marca': 'Fiat', 'ano': 2010}])
cliente4 = Cliente('Rodrigo Souza', '789456123', '21988887777', [{'placa': 'XYZ9E87', 'modelo': 'Ka', 'marca': 'Ford', 'ano': 2015}])
cliente5 = Cliente('Camila Costa', '321654987', '31977776666', [{'placa': 'MNO5G43', 'modelo': 'HB20', 'marca': 'Hyundai', 'ano': 2019}])
cliente6 = Cliente('Bruno Alves', '654987321', '41966665555', [{'placa': 'QWE3R21', 'modelo': 'Sandero', 'marca': 'Renault', 'ano': 2014}])
cliente7 = Cliente('Amanda Lima', '147258369', '51955554444', [{'placa': 'KJL8H76', 'modelo': 'Fit', 'marca': 'Honda', 'ano': 2017}])
cliente8 = Cliente('Fernando Dias', '963258147', '19944443333', [{'placa': 'UIO2P90', 'modelo': 'Polo', 'marca': 'Volkswagen', 'ano': 2021}])
cliente9 = Cliente('Juliana Ribeiro', '852963741', '81933332222', [{'placa': 'ZXC4V56', 'modelo': 'Renegade', 'marca': 'Jeep', 'ano': 2018}])
cliente10 = Cliente('Ricardo Santos', '741852963', '71922221111', [{'placa': 'VBN6M78', 'modelo': 'Cruze', 'marca': 'Chevrolet', 'ano': 2016}])
cliente11 = Cliente('Larissa Rocha', '369258147', '92911110000', [{'placa': 'TYU9I87', 'modelo': 'Kicks', 'marca': 'Nissan', 'ano': 2020}])
cliente12 = Cliente('Gabriel Martins', '258147369', '48900009999', [{'placa': 'ASD5F43', 'modelo': '208', 'marca': 'Peugeot', 'ano': 2022}])


clientes.adicionar(cliente1)
clientes.adicionar(cliente2)
clientes.adicionar(cliente3)
clientes.adicionar(cliente4)
clientes.adicionar(cliente5)
clientes.adicionar(cliente6)
clientes.adicionar(cliente7)
clientes.adicionar(cliente8)
clientes.adicionar(cliente9)
clientes.adicionar(cliente10)
clientes.adicionar(cliente11)
clientes.adicionar(cliente12)
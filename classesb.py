# Classe Cliente
class Cliente:
    def __init__(self, nome, sobrenome, endereco, cpf, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.__cpf = cpf
        self.__email = email
        self.__senha = senha

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo):
        self.__cpf = novo
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, novo):
        self.__email = novo
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, novo):
        self.__senha = novo

    def to_dict(self):
        return {
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "endereco": self.endereco,
            "cpf": self.__cpf,
            "email": self.__email,
            "senha": self.__senha
        }

    def __str__(self):
        return f'''
Nome: {self.nome}
Sobrenome: {self.sobrenome}
Endereço: {self.endereco}
CPF: {self.__cpf}
Email: {self.__email}
Senha: {self.__senha}'''

# Classe Veiculo
class Veiculo:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, novo):
        self.__marca = novo
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, novo):
        self.__modelo = novo

    def to_dict(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "ano": self.ano,
            "preco": self.preco
        }

    def __str__(self):
        return f'''
Marca: {self.marca}
Modelo: {self.modelo}
Ano: {self.ano}
Preço: {self.preco}'''

# Classe Compra
class Compra:
    def __init__(self, cliente, veiculo, preco_final, data_compra=None):
        self.cliente = cliente  # Relacionamento do tipo associação com a classe Cliente
        self.veiculo = veiculo  # Relacionamento do tipo associação com a classe Veiculo
        self.preco_final = preco_final
        self.data_compra = data_compra or datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Data da compra
    
    def __str__(self):
        return f'''
Cliente: {self.cliente.nome} {self.cliente.sobrenome}
Veículo: {self.veiculo.marca} {self.veiculo.modelo} ({self.veiculo.ano})
Preço Final: R$ {self.preco_final}
Data da Compra: {self.data_compra}
'''

# Classe Loja
class Loja:
    def __init__(self):
        self._clientes = []
        self._veiculos = []
        self._compras = []

    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente) # Relacionamento do tipo agregação com a classe Cliente
    
    def adicionar_veiculo(self, veiculo):
        self._veiculos.append(veiculo) # Relacionamento do tipo agregação com a classe Veiculo

    def realizar_compra(self, cliente, veiculo):
        try:
            # Realiza a compra com preço final
            preco_final = veiculo.preco  # Pode ser alterado com descontos ou condições de pagamento
            compra = Compra(cliente, veiculo, preco_final)
            self._compras.append(compra) # Relacionamento do tipo agregação com a classe Compra
            print(f"Compra realizada com sucesso! {compra}")
        except Exception as e:
            print(f"Erro ao realizar a compra: {e}")
    
    def salvar_dados(self, arquivo):
        try:
            with open(arquivo, "w") as f:
                dados = {
                    "clientes": [cliente.to_dict() for cliente in self._clientes],
                    "veiculos": [veiculo.to_dict() for veiculo in self._veiculos],
                    "compras": [{
                        "cliente": compra.cliente.to_dict(),
                        "veiculo": compra.veiculo.to_dict(),
                        "preco_final": compra.preco_final,
                        "data_compra": compra.data_compra
                    } for compra in self._compras]
                }
                json.dump(dados, f, indent=4)
            print("Dados salvos com sucesso.")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

    def carregar_dados(self, arquivo):
        try:
            with open(arquivo, "r") as f:
                dados = json.load(f)
                # Carrega os clientes
                self._clientes = [Cliente(**c) for c in dados["clientes"]]
                # Carrega os veículos
                self._veiculos = [Veiculo(**v) for v in dados["veiculos"]]
                # Carrega as compras
                for c in dados["compras"]:
                    cliente = next(cliente for cliente in self._clientes if cliente.cpf == c["cliente"]["cpf"])
                    veiculo = next(veiculo for veiculo in self._veiculos if veiculo.modelo == c["veiculo"]["modelo"])
                    compra = Compra(cliente, veiculo, c["preco_final"], c["data_compra"])
                    self._compras.append(compra)
            print("Dados carregados com sucesso.")
        except FileNotFoundError:
            print(f"Arquivo '{arquivo}' não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
    
    def listar_veiculos(self):
        if not self._veiculos:
            print("Não há veículos disponíveis.")
        for veiculo in self._veiculos:
            print(veiculo)
    
    def listar_clientes(self):
        if not self._clientes:
            print("Não há clientes cadastrados.")
        for cliente in self._clientes:
            print(cliente)
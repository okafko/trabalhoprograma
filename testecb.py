from classesb import Cliente
from classesb import Veiculo
from classesb import Loja

print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}")

def remover_veiculo(self, modelo):
        try:
            veiculo = next(v for v in self._veiculos if v.modelo == modelo)
            self._veiculos.remove(veiculo)
            print(f"Veículo '{modelo}' removido com sucesso.")
        except StopIteration:
            print(f"Veículo '{modelo}' não encontrado.")

def salvar_dados(self, arquivo):
        try:
            with open(arquivo, "w") as f:
                dados = {
                    "veiculos": [veiculo.to_dict() for veiculo in self._veiculos],
                    "clientes": [cliente.to_dict() for cliente in self._clientes],
                }
                json.dump(dados, f, indent=4)
            print("Dados salvos com sucesso.")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

def carregar_dados(self, arquivo):
        try:
            with open(arquivo, "r") as f:
                dados = json.load(f)
                self._veiculos = [Veiculo(v["modelo"], v["ano"], v["preco"]) for v in dados["veiculos"]]
                self._clientes = [Cliente(c["nome"], c["cpf"]) for c in dados["clientes"]]
            print("Dados carregados com sucesso.")
        except FileNotFoundError:
            print(f"Arquivo '{arquivo}' não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")


# Exemplo de uso
_name_ = ""

if _name_ == "_main_":
    loja = Loja()

    # Criar clientes e veículos
    cliente1 = Cliente("Ana Silva", "12345678901")
    cliente2 = Cliente("João Pereira", "98765432100")

    veiculo1 = Veiculo("Toyota Corolla", 2020, 85000)
    veiculo2 = Veiculo("Honda Civic", 2019, 80000)

    # Adicionar clientes e veículos na loja
    loja.adicionar_cliente(cliente1)
    loja.adicionar_cliente(cliente2)

    loja.adicionar_veiculo(veiculo1)
    loja.adicionar_veiculo(veiculo2)

    # Listar informações
    print("\nVeículos disponíveis:")
    loja.listar_veiculos()

    print("\nClientes cadastrados:")
    loja.listar_clientes()

    # Remover veículo
    loja.remover_veiculo("Toyota Corolla")

    # Salvar e carregar dados
    loja.salvar_dados("loja.json")
    loja.carregar_dados("loja.json")
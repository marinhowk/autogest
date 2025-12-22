class Veiculo:
    veiculos = []
    codigo = 1

    def __init__(self, marca, modelo, ano, valor):
        self.codigo = Veiculo.codigo
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self._disponivel = True
        Veiculo.veiculos.append(self)
        Veiculo.codigo += 1

    def __str__(self):
        return f"{self.codigo} | {self.marca} | {self.modelo} | {self.ano} | {self.valor} | {self.disponivel}"

    @classmethod
    def listar_estoque(cls):
        print(f"\n{"Código".ljust(15)} | {"Marca".ljust(15)} | {"Modelo".ljust(15)} | {"Ano".ljust(15)} | {"Valor".ljust(15)} | {"Disponibilidade"}")
        for veiculo in cls.veiculos:
            print(f"{str(veiculo.codigo).ljust(15)} | {veiculo.marca.ljust(15)} | {veiculo.modelo.ljust(15)} | {veiculo.ano.ljust(15)} | {str(veiculo.valor).ljust(15)} | {veiculo.disponivel}")

    @property
    def disponivel(self):
        return "Em estoque" if self._disponivel else "Vendido"

    def alterar_disponibilidade(self):
        self._disponivel = not self._disponivel

from models.models import Veiculo, Vendedor

def nome_do_sistema():
    print("=" * 30)
    print(("Autogest").center(30))
    print("=" * 30)

def subtitulo(texto):
    print("=" * 50)
    print((texto).center(50))
    print("=" * 50)

def opcao_invalida_menu_principal():
    print("Opção inválida")
    opcoes_menu_principal(Veiculo)

def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal. ")
    main()

def menu_principal():
    print("1. Adicionar veículo ao estoque")
    print("2. Lançar venda")
    print("3. Listar estoque")
    print("4. Cadastrar vendedor")
    print("5. Listar vendedores")

def adicionar_veiculo(Veiculo):
    subtitulo("Registre um novo veículo")
    marca = input("\nMarca: ")
    modelo = input ("Modelo: ")
    ano = input("Ano: ")
    valor = int(input("Valor: "))

    Veiculo(marca, modelo, ano, valor)

    voltar_ao_menu_principal()

def lancar_venda():
    subtitulo("Lançamento de Venda")

    codigo_veiculo = int(input("Insira o código do veículo: "))
    nome_vendedor = input("Insira o nome do vendedor: ")
    porcentagem = float(input("Informe a porcentagem da comissão: "))

    veiculo_encontrado = None
    vendedor_encontrado = None

    for veiculo in Veiculo.veiculos:
        if veiculo.codigo == codigo_veiculo:
            veiculo_encontrado = veiculo
            break

    for vendedor in Vendedor.vendedores:
        if vendedor.nome == nome_vendedor:
            vendedor_encontrado = vendedor
            break

    if not veiculo_encontrado:
        print("Veículo não encontrado.")
        return

    if not vendedor_encontrado:
        print("Vendedor não encontrado.")
        return

    veiculo_encontrado.alterar_disponibilidade()
    vendedor_encontrado.registrar_comissao(
        veiculo_encontrado,
        porcentagem
    )

    print("Venda e comissão registradas com sucesso!")

    voltar_ao_menu_principal()

def cadastrar_vendedor(Vendedor):
    subtitulo("Cadastre um Novo Vendedor")
    nome = str(input("Nome do Vendedor: "))
    print(f"O cadastro do(a) vendedor(a) {nome} foi realizado com sucesso!")

    Vendedor(nome)

    voltar_ao_menu_principal()

def opcoes_menu_principal(Veiculo):
    try:
        opcao_escolhida = int(input("\nEscolha uma opção: "))

        match opcao_escolhida:
            case 1:
                adicionar_veiculo(Veiculo)
            case 2:
                lancar_venda()
            case 3:
                subtitulo("Estoque - Disponíveis / Vendidos")
                Veiculo.listar_estoque()
                voltar_ao_menu_principal()
            case 4:
                cadastrar_vendedor(Vendedor)
            case 5:
                subtitulo("Vendedores Vinculados a Loja")
                Vendedor.listar_vendedores()
                voltar_ao_menu_principal()
            case _:
                print("Opção inválida")
    except:
        opcao_invalida_menu_principal()

def main():
    nome_do_sistema()
    menu_principal()
    opcoes_menu_principal(Veiculo)

if __name__ == "__main__":
    main()
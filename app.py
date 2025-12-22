from models.models import Veiculo

def nome_do_sistema():
    print("=" * 30)
    print(("Autogest").center(30))
    print("=" * 30)

def subtitulo(texto):
    print("=" * 50)
    print((texto).center(50))
    print("=" * 50)

def opcao_invalida_mprincipal():
    print("Opção inválida")
    opcoes_menu_principal(Veiculo)

def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal. ")
    main()

def menu_principal():
    print("1. Adicionar veículo ao estoque")
    print("2. Lançar venda")
    print("3. Listar estoque")

def adicionar_veiculo(Veiculo):
    subtitulo("Registre um novo veículo")
    marca = input("\nMarca: ")
    modelo = input ("Modelo: ")
    ano = input("Ano: ")
    valor = input("Valor: ")

    Veiculo(marca, modelo, ano, valor)

    voltar_ao_menu_principal()

def lancar_venda(Veiculo):
    subtitulo("Lançamento de Venda")
    codigo_do_veiculo = int(input("\nDigite o código do veículo:"))

    for Veiculo in Veiculo.veiculos:
        if codigo_do_veiculo == Veiculo.codigo:
            Veiculo.alterar_disponibilidade()
            print("Venda lançada com sucesso!")
        else:
            print("O veículo não foi encontrado")
            lancar_venda(Veiculo)

    voltar_ao_menu_principal()

def opcoes_menu_principal(Veiculo):
    try:
        opcao_escolhida = int(input("\nEscolha uma opção: "))

        match opcao_escolhida:
            case 1:
                adicionar_veiculo(Veiculo)
            case 2:
                lancar_venda(Veiculo)
            case 3:
                subtitulo("Estoque - Disponíveis / Vendidos")
                Veiculo.listar_estoque()
                voltar_ao_menu_principal()
            case _:
                print("Opção inválida")
    except:
        opcao_invalida_mprincipal()

def main():
    nome_do_sistema()
    menu_principal()
    opcoes_menu_principal(Veiculo)

if __name__ == "__main__":
    main()
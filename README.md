# Autogest → Sistema de Gestão de Veículos e Vendas

Projeto desenvolvido em **Python** com foco no estudo de **Programação Orientada a Objetos (POO)**.  O sistema simula a gestão de **estoque de veículos**, **cadastro de vendedores** e **lançamento de vendas com cálculo de comissões**, utilizando interação via terminal.

---

## 📌 Funcionalidades

- Cadastro de veículos
- Listagem de veículos disponíveis e vendidos
- Cadastro de vendedores
- Listagem de vendedores e comissões
- Lançamento de vendas
- Cálculo automático de comissão
- Controle de disponibilidade do veículo

---

## 🧠 Conceitos Utilizados

- Programação Orientada a Objetos
- Classes e Objetos
- Métodos de classe (`@classmethod`)
- Encapsulamento (`@property`)
- Estrutura de menu no terminal

---

## Descrição das Classes
### Classe Veiculo

Responsável por representar os veículos do estoque.

Principais atributos:

- codigo: Identificador único do veículo
- marca
- modelo
- ano
- valor
- _disponivel: Controle interno de disponibilidade

Principais métodos:

- listar_estoque() → Lista todos os veículos cadastrados
- alterar_disponibilidade() → Marca o veículo como vendido
- disponivel (property) → Retorna o status do veículo

### Classe Vendedor

Responsável por representar os vendedores da loja.

Principais atributos:

- nome
- comissao

Principais métodos:

- registrar_comissao() → Calcula e acumula a comissão do vendedor
- listar_vendedores() → Lista todos os vendedores cadastrados




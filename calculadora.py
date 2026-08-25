def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if b == 0:
        return None

    returna / b

def potencia(a,b):
    return a ** b

def mostrar_menu():
    print("\n==========================")
    print("      CALCULADORA")
    print("==========================")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Histórico")
    print("0 - Sair")
    print("==========================")

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um número válido.")


def mostrar_historico(historico):
    if not historico:
        print("\nNenhuma operação realizada.")
        return

    print("\n========== HISTÓRICO ==========")

    for operacao in historico:
        print(operacao)


def main():
    historico = []

    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("\nPrograma encerrado.")
            break

        if opcao == "6":
            mostrar_historico(historico)
            continue

        if opcao not in ["1", "2", "3", "4", "5"]:
            print("\nOpção inválida.")
            continue

        numero1 = ler_numero("Digite o primeiro número: ")
        numero2 = ler_numero("Digite o segundo número: ")

        if opcao == "1":
            resultado = soma(numero1, numero2)
            simbolo = "+"

        elif opcao == "2":
            resultado = subtracao(numero1, numero2)
            simbolo = "-"

        elif opcao == "3":
            resultado = multiplicacao(numero1, numero2)
            simbolo = "*"

        elif opcao == "4":
            resultado = divisao(numero1, numero2)
            simbolo = "/"

            if resultado is None:
                print("\nErro: não é possível dividir por zero.")
                continue

        elif opcao == "5":
            resultado = potencia(numero1, numero2)
            simbolo = "^"

        operacao = f"{numero1:g} {simbolo} {numero2:g} = {resultado:g}"

        print(f"\nResultado: {operacao}")

        historico.append(operacao)


if __name__ == "__main__":
    main()
    









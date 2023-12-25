while True:
    print("Calculadora aritmética:\n")
    print("Operadores aritméticos válidos:")
    print("     somar [+] subtrair [-]")
    print("     multiplicar [*] dividir [/]")
    print("     potenciação [**] radiciação [**0.5]]")
    print("     resto da divisão [%] quociente da divisão [//]")

    try:
        expressao = input("\nDigite a sua expressão [exemplo: 2+2]: ")
        operacao = eval(expressao)

        print(f'\nO resultado da expressão {expressao} é igual a {operacao}')
    except Exception:
        print('Operação inválida, tente novamente.')
        continue
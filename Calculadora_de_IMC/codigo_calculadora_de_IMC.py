while True:
    nome = input('Qual é o seu nome? ').strip().capitalize()

    if nome.isalpha():
        nome.capitalize()
    else:
        print('Atenção, o nome deve conter apenas letras.')
        continue

    altura = input('Qual é a sua altura? [em metros]: ').replace(',', '.').strip()

    if altura.replace('.', '').isdigit():
        altura = float(altura)
    else:
        print('Atenção, a altura deve conter apenas números, ponto ou virgula.')
        continue

    peso = input('Qual é o seu peso? [em quilos]: ').replace(',', '.').strip()

    if peso.replace('.', '').isdigit():
        peso = float(peso)
    else:
        print('Atenção, o peso deve conter apenas números, ponto ou virgula.')
        continue

    imc = peso / altura ** 2

    print('')

    print(f'{nome} tem {altura} de altura e pesa {peso}Kg!')
    print(f'Logo, o seu IMC é {imc:.2f}')

    if imc<=18.5:
        print(f'Seu imc cujo valor é "{imc:.2f}" está abaixo da média desejada "18.5".')
    elif imc<=24.9:
        print(f'Seu imc cujo valor é "{imc:.2f}" está normal "entre 18.5 e 24.9".')
    else:
        print(f'Seu imc cujo valor é "{imc:.2f}" está classificado como sobrepeso "acima de 24.9"')

    print('')
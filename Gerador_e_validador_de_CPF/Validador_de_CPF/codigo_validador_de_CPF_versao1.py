"""
Projeto: Validador de CPF
"""

while True:
    try:
        cpf_enviado_usuario = input('CPF: ').replace('.', '').replace('-', '').replace(' ', '')

        entrada_e_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)
        if entrada_e_sequencial:
            print('Dados sequenciais não são valores válidos como CPF.')
            continue

        """
        Calculo do primeiro dígito do CPF
        CPF: 746.824.890-70
        Colete a soma dos 9 primeiros dígitos do CPF
        multiplicando cada um dos valores por uma
        contagem regressiva começando de 10
        Ex.:  746.824.890-70 (746824890)
        10  9  8  7  6  5  4  3  2
        *  7   4  6  8  2  4  8  9  0
        70  36 48 56 12 20 32 27 0
        Somar todos os resultados: 
        70+36+48+56+12+20+32+27+0 = 301
        Multiplicar o resultado anterior por 10
        301 * 10 = 3010
        Obter o resto da divisão da conta anterior por 11
        3010 % 11 = 7
        Se o resultado anterior for maior que 9:
            resultado é 0
        contrário disso:
            resultado é o valor da conta
        O primeiro dígito do CPF é 7
        """

        nove_digitos = cpf_enviado_usuario[:9]
        contador_regressivo_1 = 10
        resultado_digito_1 = 0
        for digito in nove_digitos:
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        """
        Calculo do segundo dígito do CPF
        CPF: 746.824.890-70
        Colete a soma dos 9 primeiros dígitos do CPF,
        MAIS O PRIMEIRO DIGITO,
        multiplicando cada um dos valores por uma
        contagem regressiva começando de 11
        Ex.:  746.824.890-70 (7468248907)
        11 10  9  8  7  6  5  4  3  2
        *  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
        77 40 54 64 14 24 40 36  0 14
        Somar todos os resultados:
        77+40+54+64+14+24+40+36+0+14 = 363
        Multiplicar o resultado anterior por 10
        363 * 10 = 3630
        Obter o resto da divisão da conta anterior por 11
        3630 % 11 = 0
        Se o resultado anterior for maior que 9:
            resultado é 0
        contrário disso:
            resultado é o valor da conta
        O segundo dígito do CPF é 0
        """

        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11
        resultado_digito_2 = 0
        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        """
        Validador que compara o CPF fornecido com o CPF gerado

        """

        cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
        if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
            print(f'{cpf_enviado_usuario} é válido')
        else:
            print('CPF inválido')

    except ValueError:
        print('Por favor, digite apenas caracteres válidos (0-9) (.) (-) ( ).')
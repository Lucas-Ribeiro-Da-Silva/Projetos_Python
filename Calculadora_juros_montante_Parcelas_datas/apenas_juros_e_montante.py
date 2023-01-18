
def calcula_juros_e_montante():
    capital = float(input("Qual o seu capital inicial? R$").replace(',','.'))
    tipo_tempo = input("calculo em anos [1], meses [2] ou dias [3]? ")
    if tipo_tempo == '1':
        tempo = int(input("Quantos anos? "))
    elif tipo_tempo == '2':
        tempo = int(input("Quantos meses? "))
    else:
        tempo = int(input("Quantos dias? "))
    tipo_juros = input("juros simples [1] ou juros composto [2]? ")
    juros = float(input("Qual a taxa de juros [exemplo: 0.1 equivale a 10%]? ").replace(',','.'))
    if tipo_juros=='1':
        montante_simples = capital*(1+(juros*tempo))
        print(f'montante = R${montante_simples:.2f}')
        print(f'o total de juros foi de R${montante_simples-capital:.2f}')
        return montante_simples
    montante_composto = capital*((1+juros)**tempo)
    print(f'montante = R${montante_composto:.2f}')
    print(f'o total de juros foi de R${montante_composto-capital:.2f}')
    return montante_composto

calcula_juros_e_montante()